import hashlib
import json
import logging
import os
import time
from urllib.parse import quote

import redis
from django.conf import settings

from bots.redis_utils import redis_key
from bots.web_bot_adapter.okta_authenticator import OktaAuthenticator, OktaSessionError

logger = logging.getLogger(__name__)


class OktaSessionMethods:
    """Okta browser-session helpers shared by every adapter that signs its bot in through Okta."""

    def _okta_session_redis_key(self):
        domain = settings.OKTA_BOT_LOGIN_DOMAIN or ""
        username = os.getenv("OKTA_BOT_LOGIN_USERNAME", "")
        totp_secret = os.getenv("OKTA_BOT_LOGIN_TOTP_SECRET", "")
        fingerprint = hashlib.sha256(f"{domain}|{username}|{totp_secret}".encode()).hexdigest()
        return redis_key(f"okta_session_cookie:{fingerprint}")

    def _clear_cached_okta_session(self, redis_client=None):
        """Remove the cached Okta session cookie and its usage counter from redis."""
        try:
            if redis_client is None:
                redis_client = redis.from_url(settings.REDIS_URL_WITH_PARAMS)
            cookie_key = self._okta_session_redis_key()
            redis_client.delete(cookie_key, f"{cookie_key}:uses")
        except Exception as e:
            logger.warning(f"Failed to clear cached Okta session from redis: {e}")

    def establish_okta_session(self):
        """Sets the Okta sid cookie. First looks in redis to see if one has already been set or is being set. If not, creates one.

        Cached cookies are also expired after being used MAX_OKTA_SESSION_USES times to limit the blast radius if Okta invalidates the session early.
        """
        redis_client = redis.from_url(settings.REDIS_URL_WITH_PARAMS)
        cookie_key = self._okta_session_redis_key()
        usage_key = f"{cookie_key}:uses"
        lock_key = f"{cookie_key}:lock"

        okta_domain = settings.OKTA_BOT_LOGIN_DOMAIN
        # Lock TTL must comfortably exceed the worst-case TOTP+navigation flow.
        lock_ttl_seconds = 120
        # Total time to wait for another bot to finish before giving up.
        max_wait_seconds = 180
        poll_interval_seconds = 3
        max_okta_session_uses = int(os.getenv("OKTA_BOT_LOGIN_MAX_SESSION_USES", "20"))
        deadline = time.time() + max_wait_seconds

        while True:
            cookie_data_raw = redis_client.get(cookie_key)
            # If cookie is in redis, inject it into the driver
            if cookie_data_raw:
                # Atomically increment the usage counter so concurrent bots agree on use count.
                use_count = redis_client.incr(usage_key)
                if use_count > max_okta_session_uses:
                    logger.info(f"Cached Okta session cookie has been used {use_count - 1} times (limit {max_okta_session_uses}). Discarding and regenerating.")
                    self._clear_cached_okta_session(redis_client)
                    continue

                try:
                    cookie_data = json.loads(cookie_data_raw)
                    logger.info(f"Found Okta session cookie in redis (use {use_count}/{max_okta_session_uses}). Injecting into driver.")
                    self.driver.get(f"https://{okta_domain}/")
                    self.driver.add_cookie(
                        {
                            "name": "sid",
                            "value": cookie_data["value"],
                            "domain": okta_domain,
                            "path": "/",
                            "secure": True,
                        },
                    )
                    return
                except Exception as e:
                    logger.warning(f"Failed to use cached Okta cookie from redis ({e}). Will regenerate.")
                    self._clear_cached_okta_session(redis_client)

            # If no cookie in redis, acquire a lock to generate one.
            lock_acquired = redis_client.set(lock_key, "1", nx=True, ex=lock_ttl_seconds)
            if lock_acquired:
                try:
                    logger.info("Acquired lock to generate Okta session. Running TOTP flow.")
                    self.save_valid_okta_session_token_in_redis()
                    return
                finally:
                    redis_client.delete(lock_key)

            if time.time() >= deadline:
                raise OktaSessionError(f"Timed out after {max_wait_seconds}s waiting for another bot to generate the Okta session.")

            logger.info(f"Another bot is generating the Okta session. Waiting {poll_interval_seconds}s before retrying.")
            time.sleep(poll_interval_seconds)

    def save_valid_okta_session_token_in_redis(self):
        okta_domain = settings.OKTA_BOT_LOGIN_DOMAIN
        okta_authenticator = OktaAuthenticator(
            okta_domain=okta_domain,
            username=os.getenv("OKTA_BOT_LOGIN_USERNAME"),
            password=os.getenv("OKTA_BOT_LOGIN_PASSWORD"),
            totp_secret=os.getenv("OKTA_BOT_LOGIN_TOTP_SECRET"),
        )
        session_token = okta_authenticator.authenticate()

        redirect_url = quote(f"https://{okta_domain}", safe="")
        url = f"https://{okta_domain}/login/sessionCookieRedirect?token={session_token}&redirectUrl={redirect_url}"

        logger.info("Navigating to Okta sessionCookieRedirect")
        self.driver.get(url)

        # Wait for the sid cookie to appear
        start = time.time()
        timeout = 30
        while True:
            cookies = self.driver.get_cookies()
            cookie_names = {c.get("name") for c in cookies if c.get("name")}
            if "sid" in cookie_names:
                logger.info("Okta session cookie (sid) established")
                sid_cookie = next((c for c in cookies if c.get("name") == "sid"), None)
                if not sid_cookie:
                    raise OktaSessionError("Okta 'sid' cookie was reported present but could not be retrieved from the driver.")
                try:
                    redis_client = redis.from_url(settings.REDIS_URL_WITH_PARAMS)
                    cookie_key = self._okta_session_redis_key()
                    # Cache for 30 minutes; well below typical Okta session lifetime so we never serve a stale cookie.
                    redis_client.setex(cookie_key, 60 * 30, json.dumps(sid_cookie))
                    # Reset the usage counter so it tracks uses of this freshly minted cookie only.
                    redis_client.delete(f"{cookie_key}:uses")
                    logger.info("Okta session cookie cached in redis")
                except Exception as e:
                    raise OktaSessionError(f"Failed to cache Okta session cookie in redis: {e}") from e
                return
            if time.time() - start > timeout:
                logger.error(f"Okta session cookie not found after {timeout}s. Cookies present: {cookie_names}")
                raise OktaSessionError(f"Failed to establish Okta browser session. No 'sid' cookie after {timeout}s. Ensure {okta_domain} is a trusted origin in Okta Admin.")
            time.sleep(1)
