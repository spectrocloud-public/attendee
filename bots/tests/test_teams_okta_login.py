import itertools
from unittest.mock import MagicMock, PropertyMock, patch

from django.test import SimpleTestCase, override_settings

from bots.teams_bot_adapter.teams_ui_methods import TeamsUIMethods
from bots.web_bot_adapter.okta_authenticator import OktaMfaError
from bots.web_bot_adapter.ui_methods import UiLoginAttemptFailedException


@override_settings(USE_OKTA_LOGIN_FOR_SIGNED_IN_TEAMS_BOTS=True, OKTA_BOT_LOGIN_DOMAIN="example.okta.com")
class TestTeamsOktaLogin(SimpleTestCase):
    def make_ui(self, urls):
        ui = TeamsUIMethods(MagicMock(), "https://teams.microsoft.com/l/meetup-join/x", "bot")
        type(ui.driver).current_url = PropertyMock(side_effect=urls)
        ui.establish_okta_session = MagicMock()
        ui.submit_microsoft_login_username = MagicMock()
        ui.find_element_by_selector = MagicMock(return_value=None)
        ui._clear_cached_okta_session = MagicMock()
        ui.send_screenshot_and_mhtml_file_message = MagicMock()
        return ui

    def test_retries_wrapper_routes_to_okta_login(self):
        ui = TeamsUIMethods(MagicMock(), "https://teams.microsoft.com/l/meetup-join/x", "bot")
        ui.login_to_microsoft_account = MagicMock()
        ui.login_to_microsoft_account_with_okta = MagicMock()

        ui.login_to_microsoft_account_with_retries()

        ui.login_to_microsoft_account_with_okta.assert_called_once()
        ui.login_to_microsoft_account.assert_not_called()

    @patch("bots.teams_bot_adapter.teams_ui_methods.time")
    def test_completes_once_redirected_off_sign_in_hosts(self, mock_time):
        mock_time.time.return_value = 0
        ui = self.make_ui(["https://login.microsoftonline.com/x", "https://example.okta.com/app/office365", "https://www.office.com/", "https://www.office.com/"])

        ui.login_to_microsoft_account_with_okta()

        ui.establish_okta_session.assert_called_once()
        ui._clear_cached_okta_session.assert_not_called()

    @patch("bots.teams_bot_adapter.teams_ui_methods.time")
    def test_times_out_while_stuck_on_okta(self, mock_time):
        mock_time.time.side_effect = [0, 0, 61]
        ui = self.make_ui(itertools.repeat("https://example.okta.com/signin/verify"))

        with self.assertRaises(UiLoginAttemptFailedException):
            ui.login_to_microsoft_account_with_okta()

        ui._clear_cached_okta_session.assert_called_once()
        ui.send_screenshot_and_mhtml_file_message.assert_called_once()

    def test_okta_errors_surface_as_login_failures(self):
        ui = self.make_ui([])
        ui.establish_okta_session.side_effect = OktaMfaError("TOTP code was rejected")

        with self.assertRaises(UiLoginAttemptFailedException):
            ui.login_to_microsoft_account_with_okta()

        ui.submit_microsoft_login_username.assert_not_called()
