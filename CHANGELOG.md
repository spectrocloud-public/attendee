# Changelog

## [1.86.1-sp.2](https://github.com/spectrocloud-public/attendee/compare/v1.86.1-sp.1...v1.86.1-sp.2) (2026-10-29)


### Features

* add start_time_lt and attendee_email filters to calendar_events ([9ea38c9](https://github.com/spectrocloud-public/attendee/commit/9ea38c9e0f7b9099d149387f88e3aad7c1bc83c1))


### Bug Fixes

* add start_time_lt and attendee_email filters to calendar_events ([#22](https://github.com/spectrocloud-public/attendee/issues/22)) ([bac7c0d](https://github.com/spectrocloud-public/attendee/commit/bac7c0d47092c5f4ee66d8a294b974ebbaf48d0f))

## [1.86.1-sp.1](https://github.com/spectrocloud-public/attendee/compare/v1.82.3-sp.1...v1.86.1-sp.1) (2026-10-27)


### Features

* add gladia model, custom vocabulary and custom spelling settings ([985b1ac](https://github.com/spectrocloud-public/attendee/commit/985b1ac80bd7631a49841371a0b2be4a88328ea3))
* assemblyai multi-language support ([#1072](https://github.com/spectrocloud-public/attendee/issues/1072)) ([183bf35](https://github.com/spectrocloud-public/attendee/commit/183bf35b88f77a9e6b35977a010ab5a188ca8c8b))
* Gladia language config ([#1096](https://github.com/spectrocloud-public/attendee/issues/1096)) ([9ca1e16](https://github.com/spectrocloud-public/attendee/commit/9ca1e1696b97c17fb5c82183fc99c1c5076c464c))
* Gladia vocabulary spelling model ([#1097](https://github.com/spectrocloud-public/attendee/issues/1097)) ([5acfb99](https://github.com/spectrocloud-public/attendee/commit/5acfb995494dc03f15a4bf9ca39aca73cb716b64))
* screenshare ([#699](https://github.com/spectrocloud-public/attendee/issues/699)) ([57dd873](https://github.com/spectrocloud-public/attendee/commit/57dd87368c71923aabf455757f350029d0ff6cd2))
* send gladia language settings as language_config and store the detected language ([3d0b00a](https://github.com/spectrocloud-public/attendee/commit/3d0b00a1a553eb02c62eecf0e50b93c210d6cb1d))


### Bug Fixes

* accept RTMS websocket messages over 1 MiB ([6626809](https://github.com/spectrocloud-public/attendee/commit/66268093642fda8a4cdcdf574087a7fab0ec12b5))
* accept RTMS websocket messages over 1 MiB ([#1085](https://github.com/spectrocloud-public/attendee/issues/1085)) ([e60de7b](https://github.com/spectrocloud-public/attendee/commit/e60de7bc2ab6d1bd3ac7f88cc7243a7d3e208e43))
* add additional entries to google domain allowlist ([#1068](https://github.com/spectrocloud-public/attendee/issues/1068)) ([a47e084](https://github.com/spectrocloud-public/attendee/commit/a47e0841f4dbd9c017c33b913f77b02d63b59297))
* bump certifi ([#1103](https://github.com/spectrocloud-public/attendee/issues/1103)) ([b62cce3](https://github.com/spectrocloud-public/attendee/commit/b62cce3b46859bebfc41d9f7027afd61c4660e4c))
* fix env var name OTKA_DOMAIN -&gt; OKTA_BOT_LOGIN_DOMAIN ([#1083](https://github.com/spectrocloud-public/attendee/issues/1083)) ([cddeef2](https://github.com/spectrocloud-public/attendee/commit/cddeef207bccdb00d0a001926a8ca267e1e85ca1))
* Handle captions and translation variant for gmeet ([#1089](https://github.com/spectrocloud-public/attendee/issues/1089)) ([2a519be](https://github.com/spectrocloud-public/attendee/commit/2a519bebc379e431054ec0fc699ac58b5ecfb46b))
* keep the meeting code for meet.google.com/meet/&lt;code&gt; links ([c8dae2d](https://github.com/spectrocloud-public/attendee/commit/c8dae2d5bd544923b3139252baad60f3905ba3a2))
* keep the meeting code for meet.google.com/meet/&lt;code&gt; links ([#1094](https://github.com/spectrocloud-public/attendee/issues/1094)) ([a8ca651](https://github.com/spectrocloud-public/attendee/commit/a8ca651b0d2f6555e3d5776281d5977abf45c58a))
* let the OS assign the websocket server port ([#1084](https://github.com/spectrocloud-public/attendee/issues/1084)) ([292f318](https://github.com/spectrocloud-public/attendee/commit/292f318fe4d0dcb3ffed0888ca2ca238894f1a38))
* Look for disabled incoming video confirmation earlier in the join ([#1066](https://github.com/spectrocloud-public/attendee/issues/1066)) ([4246315](https://github.com/spectrocloud-public/attendee/commit/42463152f82d0c828697c13ff58acba2abb00359))
* Look for meeting not found in name input step gmeet ([#1065](https://github.com/spectrocloud-public/attendee/issues/1065)) ([3cbeb69](https://github.com/spectrocloud-public/attendee/commit/3cbeb69fb838bbcb9ef6915f4c1e04b5a1c08e2c))
* lower send rate for mixed audio via rtms ([#1060](https://github.com/spectrocloud-public/attendee/issues/1060)) ([ce53d04](https://github.com/spectrocloud-public/attendee/commit/ce53d04ebe736bbcc57690c8355e61dbf30478ba))
* remove parens from teams bot names ([#1090](https://github.com/spectrocloud-public/attendee/issues/1090)) ([94976b9](https://github.com/spectrocloud-public/attendee/commit/94976b9dca695a0dae82d8d2a79b53d24052fe42))
* report the waiting room for web bots ([#990](https://github.com/spectrocloud-public/attendee/issues/990)) ([6e8ad6f](https://github.com/spectrocloud-public/attendee/commit/6e8ad6fed79879a990ec1a1e2c7a724ab1bd5505))
* request RTMS audio and chat with a media type Zoom accepts ([f363c2c](https://github.com/spectrocloud-public/attendee/commit/f363c2c31e902cabd72cad72e4ce9fb6c0176bcc))
* RTMS media type handshake and utterance splitting at pauses ([#1059](https://github.com/spectrocloud-public/attendee/issues/1059)) ([f246561](https://github.com/spectrocloud-public/attendee/commit/f2465610430261699628b47c9510a3a40f8f2fe9))
* split per-participant utterances at real pauses ([c59cabf](https://github.com/spectrocloud-public/attendee/commit/c59cabf9100a75d2952a32243ba3555199488004))
* sync upstream main into spectrocloud ([#18](https://github.com/spectrocloud-public/attendee/issues/18)) ([14791db](https://github.com/spectrocloud-public/attendee/commit/14791db402d999ce18ec943c6ef3764061bb0eb0))
* When deleting audio chunks in bulk, do not load the audio blob data into memory ([#1086](https://github.com/spectrocloud-public/attendee/issues/1086)) ([b89e8cc](https://github.com/spectrocloud-public/attendee/commit/b89e8cc6373a2b615e88de1861f6029f640de0a5))


### Documentation

* remove ambiguity in voice agent docs around simultaneous screenshare and webcam ([#1087](https://github.com/spectrocloud-public/attendee/issues/1087)) ([bda8ce4](https://github.com/spectrocloud-public/attendee/commit/bda8ce438b0980b454805a87d647bb949db47a13))

## [1.82.3-sp.1](https://github.com/spectrocloud-public/attendee/compare/v1.81.1-sp.2...v1.82.3-sp.1) (2026-10-05)


### Bug Fixes

* Add robustness for concurrent credit transactions ([#1056](https://github.com/spectrocloud-public/attendee/issues/1056)) ([d9c4773](https://github.com/spectrocloud-public/attendee/commit/d9c47735b7cce6f2b8c63fc9601ec7982a122979))
* sync upstream main into spectrocloud ([de7f8e5](https://github.com/spectrocloud-public/attendee/commit/de7f8e5dc1a3a4218cb6955bcd8c5395ba08e3a8))

## [1.81.1-sp.2](https://github.com/spectrocloud-public/attendee/compare/v1.81.1-sp.1...v1.81.1-sp.2) (2026-10-03)


### Bug Fixes

* prefix tricorder redis data ([a66f5ec](https://github.com/spectrocloud-public/attendee/commit/a66f5ec80e3f1370930793283eaefbf5b03114db))
* prefix tricorder redis data ([a66f5ec](https://github.com/spectrocloud-public/attendee/commit/a66f5ec80e3f1370930793283eaefbf5b03114db))
* prefix tricorder redis data ([32ddcfa](https://github.com/spectrocloud-public/attendee/commit/32ddcfabc4e694e839f3d1f12283820af12dc6d2))

## [1.81.1-sp.1](https://github.com/spectrocloud-public/attendee/compare/v1.80.0-sp.1...v1.81.1-sp.1) (2026-09-29)


### Bug Fixes

* sync main into spectrocloud ([#8](https://github.com/spectrocloud-public/attendee/issues/8)) ([dc77ee7](https://github.com/spectrocloud-public/attendee/commit/dc77ee73755951a3be7efbde9f2b4253eb57ef0c))

## [1.80.0-sp.1](https://github.com/spectrocloud-public/attendee/compare/v1.79.4-sp.2...v1.80.0-sp.1) (2026-09-29)


### Bug Fixes

* updated fork ([#5](https://github.com/spectrocloud-public/attendee/issues/5)) ([6761154](https://github.com/spectrocloud-public/attendee/commit/67611542e435a13373de6bec4cde5a7631f77a9a))

## [1.79.4-sp.2](https://github.com/spectrocloud-public/attendee/compare/v1.79.4-sp.1...v1.79.4-sp.2) (2026-09-28)


### Bug Fixes

* add release CI/CD ([#3](https://github.com/spectrocloud-public/attendee/issues/3)) ([20d97e9](https://github.com/spectrocloud-public/attendee/commit/20d97e9cd148da8270b504d83632c42255d04e94))

## [1.79.4-sp.1](https://github.com/spectrocloud-public/attendee/compare/v1.79.4...v1.79.4-sp.1) (2026-09-25)


### Bug Fixes

* add release CI/CD ([2c2481d](https://github.com/spectrocloud-public/attendee/commit/2c2481dd411906b56c5de9f322f6043e10cfd099))
