# CHANGELOG

<!-- version list -->

## v3.1.1 (2026-01-16)

### Bug Fixes

- Fix python_requires in setup.py
  ([`ed34dd2`](https://github.com/andrewjw/prom433/commit/ed34dd230bea790b0a1c1cd7905d4264aa1f0070))

### Chores

- Switch to using black for code styling. ([#196](https://github.com/andrewjw/prom433/pull/196),
  [`1fbee79`](https://github.com/andrewjw/prom433/commit/1fbee799d598c1e09afdbc80905c4ff7b9f84032))


## v3.1.0 (2026-01-16)

### Chores

- Add support for Python 3.13 and drop Python 3.8.
  ([#100](https://github.com/andrewjw/prom433/pull/100),
  [`2b54b3c`](https://github.com/andrewjw/prom433/commit/2b54b3cdf0cee3b7e56f7addb0b3356449ee7661))

- Switch the Coveralls GitHub action for coverage.
  ([#100](https://github.com/andrewjw/prom433/pull/100),
  [`2b54b3c`](https://github.com/andrewjw/prom433/commit/2b54b3cdf0cee3b7e56f7addb0b3356449ee7661))

- **config**: Migrate config renovate.json ([#148](https://github.com/andrewjw/prom433/pull/148),
  [`7e4a55f`](https://github.com/andrewjw/prom433/commit/7e4a55fa0eec25feff10f40c9dc0a161b94906a6))

### Features

- Add sentry.io integration to allow optional tracking of runtime errors.
  ([#100](https://github.com/andrewjw/prom433/pull/100),
  [`2b54b3c`](https://github.com/andrewjw/prom433/commit/2b54b3cdf0cee3b7e56f7addb0b3356449ee7661))

- Drop support for Python 3.9 and add 3.14.
  ([`61c41fe`](https://github.com/andrewjw/prom433/commit/61c41fe571913860b18d92fb60abd2958686bb78))


## v3.0.0 (2025-05-29)

### Chores

- Revert change to coveralls as python-coveralls as other issues.
  ([`686dc9f`](https://github.com/andrewjw/prom433/commit/686dc9f7a8b145e5d3ecd19c1a397ecc3cdb737e))

- Switch to a different coveralls library so we support Python 3.13
  ([#147](https://github.com/andrewjw/prom433/pull/147),
  [`a30a1d0`](https://github.com/andrewjw/prom433/commit/a30a1d09fabc460acb451ecc7f86d34169e8a5d7))

### Features

- Drop support for Python 3.8
  ([`15310a9`](https://github.com/andrewjw/prom433/commit/15310a9ba717702ecce936b69329669c4846a91f))

### Breaking Changes

- Drop support for Python 3.8


## v2.7.0 (2024-11-06)

### Features

- Add sentry.io integration to allow optional tracking of runtime errors.
  ([`c515fec`](https://github.com/andrewjw/prom433/commit/c515fec0a4b317e9efec426c8c443d15ea7ed10c))


## v2.6.3 (2024-07-31)

### Bug Fixes

- Improve docker by building arm versions, and installing a local .tar.gz file.
  ([`37c8d96`](https://github.com/andrewjw/prom433/commit/37c8d96a0fe3f6d2aeed9249341959719d8bc7c0))


## v2.6.2 (2024-06-28)

### Bug Fixes

- Fix handling for connection failure to mqtt broker.
  ([`d0a6b4b`](https://github.com/andrewjw/prom433/commit/d0a6b4bcbe08130eed887a2c86cc42bbccce152f))


## v2.6.1 (2024-06-28)

### Bug Fixes

- Update code to be compatible with paho-mqtt>=2.0.0
  ([`c35886c`](https://github.com/andrewjw/prom433/commit/c35886c95af39f8f027fdb9a7b52bd6d23d81f26))


## v2.6.0 (2024-01-28)

### Features

- Add support for extra metrics from the Ecowitt / Fineoffset WS90 (Wittboy GW2001 station)
  ([#50](https://github.com/andrewjw/prom433/pull/50),
  [`12f5447`](https://github.com/andrewjw/prom433/commit/12f5447ae9cf693457c0a79e00535a2ccb39bbea))

- Add support for extra metrics from the Ecowitt / Fineoffset WS9…
  ([#50](https://github.com/andrewjw/prom433/pull/50),
  [`12f5447`](https://github.com/andrewjw/prom433/commit/12f5447ae9cf693457c0a79e00535a2ccb39bbea))


## v2.5.1 (2024-01-24)

### Bug Fixes

- Add missing metrix help text
  ([`44d1f2f`](https://github.com/andrewjw/prom433/commit/44d1f2feaad33b27647adf471ec5375d42df2e42))


## v2.5.0 (2024-01-24)

### Features

- Ignore newbattery tags for LaCrosse weather stations. Log multiple frequencies if using frequency
  hopping.
  ([`5a3b3d1`](https://github.com/andrewjw/prom433/commit/5a3b3d190d1cd7bbda919a4135b48fc566db3bfd))


## v2.4.0 (2023-11-15)

### Chores

- Add workflow badge.
  ([`ee9d896`](https://github.com/andrewjw/prom433/commit/ee9d896df429c9f46ac95dfdb114e26ef7f2930a))

- Don't automerge dockerfile changes, as they aren't tested.
  ([`18a0d46`](https://github.com/andrewjw/prom433/commit/18a0d4610e5098a6eabb0489dd162103d242f066))

- Fix badge link
  ([`aed1d4f`](https://github.com/andrewjw/prom433/commit/aed1d4f766c1586b79b32986ef40e5dbef0364e9))

- Fix badges.
  ([`961af4c`](https://github.com/andrewjw/prom433/commit/961af4c04e30a8e0c057b56e177549327f31f356))

- Restore run action on tags.
  ([`9b0fd68`](https://github.com/andrewjw/prom433/commit/9b0fd68c2c71ee135f20e2afd18a4aea371e236f))

- Test on Python 3.12
  ([`dfdaf38`](https://github.com/andrewjw/prom433/commit/dfdaf38c8fad6db4c3ba34423229c154e878adfc))

### Features

- Support Python 3.12
  ([`e70448f`](https://github.com/andrewjw/prom433/commit/e70448f1aecffd93cbfb74bfa4c5b9a4b21c6bf9))


## v2.3.9 (2023-08-27)

### Bug Fixes

- Switch back to building docker in main workflow.
  ([`1cf8e13`](https://github.com/andrewjw/prom433/commit/1cf8e137c73397e38009b451c9faa9d44f07a88b))

### Chores

- Add some more badges to the readme.
  ([`a7832bc`](https://github.com/andrewjw/prom433/commit/a7832bcd396a950f8464ca0471ef695b60d21160))


## v2.3.8 (2023-08-27)

### Bug Fixes

- Switch back to building docker in main workflow.
  ([`34d9be7`](https://github.com/andrewjw/prom433/commit/34d9be7fc4aa2126556a43b5766c153f7df5f3a9))


## v2.3.7 (2023-08-25)

### Bug Fixes

- Fix action
  ([`23aecd3`](https://github.com/andrewjw/prom433/commit/23aecd35f9c1373f0c680c496185a61399079b11))


## v2.3.6 (2023-08-25)

### Bug Fixes

- Only try to upload if a release was made
  ([`f213b42`](https://github.com/andrewjw/prom433/commit/f213b42426c6bb43f8afa09cd35545a3ee880e5a))

### Chores

- Fix workflow name
  ([`4657d10`](https://github.com/andrewjw/prom433/commit/4657d108eef12d9985051ff54d4c58152e6d305f))

- Require twine to upload to pypi
  ([`fdde550`](https://github.com/andrewjw/prom433/commit/fdde550e5b47f8588e8c19b107f09c5c0c5c8467))

- Upload to PyPi and GitHub
  ([`d5f0946`](https://github.com/andrewjw/prom433/commit/d5f09469fe7199a392bcb6891cb50fdebff6c900))


## v2.3.5 (2023-08-25)

### Bug Fixes

- Move to new semantic release config.
  ([`630e8ab`](https://github.com/andrewjw/prom433/commit/630e8abd02b1d40a1ac5ef548cd3765e1d388083))


## v2.3.4 (2023-08-25)

### Bug Fixes

- Publish docker image on tag creation.
  ([`40da6da`](https://github.com/andrewjw/prom433/commit/40da6dac2d3336e05956cbd8bf0bfe6a3393566c))


## v2.3.3 (2023-08-25)

### Bug Fixes

- Publish docker image on tag creation.
  ([`0960e2e`](https://github.com/andrewjw/prom433/commit/0960e2e208a402fa08d18b68719a89f144bce981))


## v2.3.2 (2023-08-25)

### Bug Fixes

- Fix release for semantic-release v8
  ([`35ac16f`](https://github.com/andrewjw/prom433/commit/35ac16fca03f53f3dbd73d34284dd91acf0d6b1d))

- Fix semantic-release --noop parameter order
  ([`611218a`](https://github.com/andrewjw/prom433/commit/611218a7fa5445863c04074833aa54b52f3c1812))

### Chores

- Add documentation about scraping with Prometheus.
  ([`854f331`](https://github.com/andrewjw/prom433/commit/854f3311334f865f4b5e0972499a86677cb15e3d))

- Automerge dependency updates that aren't a major version upgrade.
  ([`594018f`](https://github.com/andrewjw/prom433/commit/594018f39e11370912f77ae93a80016caeafc979))

- Handle mqtt on non-standard ports, and improve documentation.
  ([`9d2a77e`](https://github.com/andrewjw/prom433/commit/9d2a77ec10619243db257f1c04e8546f09f98934))

- Run action on pull requests.
  ([`3e0564d`](https://github.com/andrewjw/prom433/commit/3e0564d13eda5ae03f96f6329ad602be9ffbc789))

- Update systemd files to use new mqtt port selection
  ([`9b7a59e`](https://github.com/andrewjw/prom433/commit/9b7a59ee27ae2449e8411fc00fa9897b7c459610))


## v2.3.1 (2023-03-28)

### Bug Fixes

- Make error clearer when failing to connect to MQTT server.
  ([#21](https://github.com/andrewjw/prom433/pull/21),
  [`cc923b3`](https://github.com/andrewjw/prom433/commit/cc923b33dcb941be40e46ff32471a730d8ae0387))

### Chores

- Fix test for if a release is needed.
  ([`5684656`](https://github.com/andrewjw/prom433/commit/56846568bbfc23bbe909bc4dba5f9211479c36d7))

- Move to correct location.
  ([`fa6fd91`](https://github.com/andrewjw/prom433/commit/fa6fd9191767326ff83f9bb26eaac30cfbac95c8))

- Switch to GitHub actions for build, test and release.
  ([`32c619f`](https://github.com/andrewjw/prom433/commit/32c619f218ff32565475bf1a0b329ec43865ce7b))

- Trigger release on correct branch name.
  ([`a464b14`](https://github.com/andrewjw/prom433/commit/a464b14bca9370bf0c434f10af8b33362725ca5c))

- Update README with correct command line parameters.
  ([`2d1eaad`](https://github.com/andrewjw/prom433/commit/2d1eaadf807660859e321df9c6e2a2159bbb4b29))


## v2.3.0 (2023-03-09)

### Chores

- Don't deactivate last venv so buildbot can find coveralls.
  ([`fac51fe`](https://github.com/andrewjw/prom433/commit/fac51fe3e0e5158b0f734461662a8b85172966c3))

- Example systemd unit and environment files ([#16](https://github.com/andrewjw/prom433/pull/16),
  [`3b8c793`](https://github.com/andrewjw/prom433/commit/3b8c7938a5e411f917a055242de03b6438e9451b))

- Fix code style. ([#17](https://github.com/andrewjw/prom433/pull/17),
  [`023ee63`](https://github.com/andrewjw/prom433/commit/023ee63ee986c87d6e9a00a493cd7b98101d4cca))

- Test on multiple Python versions. ([#18](https://github.com/andrewjw/prom433/pull/18),
  [`7b90de3`](https://github.com/andrewjw/prom433/commit/7b90de3f2b216aabbc57f8a72795064753e75fce))

### Features

- Add generic date/time string parsing from python-dateutil
  ([#17](https://github.com/andrewjw/prom433/pull/17),
  [`023ee63`](https://github.com/andrewjw/prom433/commit/023ee63ee986c87d6e9a00a493cd7b98101d4cca))

- Add time parser ([#17](https://github.com/andrewjw/prom433/pull/17),
  [`023ee63`](https://github.com/andrewjw/prom433/commit/023ee63ee986c87d6e9a00a493cd7b98101d4cca))

### Testing

- Add tests for various forms of rtl_433 timestamps
  ([#17](https://github.com/andrewjw/prom433/pull/17),
  [`023ee63`](https://github.com/andrewjw/prom433/commit/023ee63ee986c87d6e9a00a493cd7b98101d4cca))


## v2.2.0 (2023-02-28)

### Features

- Add --quiet to suppress server logging
  ([`9770f43`](https://github.com/andrewjw/prom433/commit/9770f433f2e2bb2825aabceaefc2b73660e99234))

- Add metrics
  ([`f804439`](https://github.com/andrewjw/prom433/commit/f804439ce30dfbbcde4726a1aa78398ff1454fcf))


## v2.1.2 (2023-02-27)

### Bug Fixes

- Allow OS to choose Python version
  ([`bc56611`](https://github.com/andrewjw/prom433/commit/bc566119735500c546bc54aed1d4cd08a97b39cc))


## v2.1.1 (2023-02-23)

### Bug Fixes

- Treat all radio clocks as UTC so we return the correct time, regardless of the host's timezone
  (fix #11).
  ([`be71083`](https://github.com/andrewjw/prom433/commit/be7108383651c78f85d9d6e42f20c9e57ac74789))

### Chores

- Add CONTRIBUTING.md
  ([`98c61ce`](https://github.com/andrewjw/prom433/commit/98c61cecf9c190a7c133fb0600a4c6788e86497a))

- Fix style.
  ([`1230cfa`](https://github.com/andrewjw/prom433/commit/1230cfab302069abfcd7e506a96aacc7cdd2433c))


## v2.1.0 (2023-01-20)

### Chores

- Fix test.
  ([`efce366`](https://github.com/andrewjw/prom433/commit/efce366b92175a1864ab2a739cee9a208c7a626a))

- Style fixes.
  ([`bd74e6f`](https://github.com/andrewjw/prom433/commit/bd74e6f79991d4085ed793ef3e724b2af2e13162))

### Features

- Add support for radio clock values.
  ([`525191a`](https://github.com/andrewjw/prom433/commit/525191a1b421c70fbd2f8bb4d24cdbce2861e038))


## v2.0.0 (2022-11-10)

### Chores

- Switch coveralls library.
  ([`30476ec`](https://github.com/andrewjw/prom433/commit/30476ece831a20b15d900b4cfe0c36e9df47fe54))

- Update readme file.
  ([`29ca345`](https://github.com/andrewjw/prom433/commit/29ca3453463797b91a87181f74deda9502ab4ae0))

- Update readme to link to Docker Hub.
  ([`b1b10f0`](https://github.com/andrewjw/prom433/commit/b1b10f0434b858c4f7bfbe0d7230a71f28098123))

### Features

- Drop metrics after a configurable timeout (default 1 hour), so we don't continually report devices
  we've only seen once.
  ([`1197e2d`](https://github.com/andrewjw/prom433/commit/1197e2d1018264c938ca6e3756e459cdb11fa970))

### Breaking Changes

- Metrics will be dropped after 1 hour if not updated. Add --drop-after 0 to keep the old behaviour.


## v1.1.4 (2022-11-09)

### Bug Fixes

- Since we switched to mqtt there is no need to install rtl_433 in our Docker image.
  ([`5f2c147`](https://github.com/andrewjw/prom433/commit/5f2c147008b049e8bb6a0400b1f36c1725e6640d))


## v1.1.3 (2022-11-09)

### Bug Fixes

- Handle exceptions when processing messages and keep running.
  ([`a3295fe`](https://github.com/andrewjw/prom433/commit/a3295fe25b78286c752e7525195e537b9d07bbfc))


## v1.1.2 (2022-11-08)

### Bug Fixes

- Fix typo in last message metric name.
  ([`f6d5288`](https://github.com/andrewjw/prom433/commit/f6d52886cce06c2d4a4d7f22e6edca4d081b14c8))


## v1.1.1 (2022-11-08)

### Bug Fixes

- Don't warn on tag values we known we should ignore.
  ([`b6f7c77`](https://github.com/andrewjw/prom433/commit/b6f7c77acae7b3ce924d854134ef395ce1b9de8f))


## v1.1.0 (2022-11-08)

### Features

- Handle extra values about frequency and noise that are added to messages sent by rtl_433 with -M
  level.
  ([`36aa076`](https://github.com/andrewjw/prom433/commit/36aa076774b8eb35c7590f70e1ce338eb3643651))


## v1.0.0 (2022-11-08)

### Features

- Rework metrics so we can handle more types of messages, and record the last time a message was
  seen for a device.
  ([`57d68ec`](https://github.com/andrewjw/prom433/commit/57d68ec69e2c63486ea6466b043eef274e3e68ef))

### Breaking Changes

- All metrics have been renamed.


## v0.4.2 (2022-04-27)

### Bug Fixes

- Handle correct type for mqtt messages.
  ([`01d91ac`](https://github.com/andrewjw/prom433/commit/01d91ac20de8a955e2e981ced0682b2eaaef6661))


## v0.4.1 (2022-04-27)

### Bug Fixes

- Fix message handler prototype.
  ([`2998de3`](https://github.com/andrewjw/prom433/commit/2998de3bf25c3edbd9bdebbf4628bbca4ec152c3))


## v0.4.0 (2022-04-27)

### Features

- Switch to listening to MQTT messages rather than running rtl_433 directly.
  ([`1d81a6f`](https://github.com/andrewjw/prom433/commit/1d81a6fd6ad789ba0f195c0fd673b253130c6a45))


## v0.3.4 (2022-02-11)

### Bug Fixes

- Use correct parameter for setting rtl_433 output to Json.
  ([`464dd07`](https://github.com/andrewjw/prom433/commit/464dd079d3af4b8446c2d5f5ebb60d6e9ff7e455))


## v0.3.3 (2022-02-10)

### Bug Fixes

- Use correct package name for rtl-433.
  ([`3589181`](https://github.com/andrewjw/prom433/commit/3589181eff90d74f4f0dab18273ec99c87cfddcb))


## v0.3.2 (2022-02-08)

### Bug Fixes

- Add universe repo to allow us to install rtl_433.
  ([`ca4835e`](https://github.com/andrewjw/prom433/commit/ca4835e6a07be60799fca41253ba9c7a2af3bbce))


## v0.3.1 (2022-02-07)

### Bug Fixes

- Add universe repository.
  ([`f77c19c`](https://github.com/andrewjw/prom433/commit/f77c19c9367bc741323dcf643d497e3c50a328b3))


## v0.3.0 (2022-02-03)

### Features

- Switch to Python slim image so we can install Python packages more easily.
  ([`e9e652e`](https://github.com/andrewjw/prom433/commit/e9e652eff0037a29503c89d113d7a5f1d34eb4c2))


## v0.2.5 (2022-01-03)

### Bug Fixes

- Use a docker image with rtl_433 installed.
  ([`7184aed`](https://github.com/andrewjw/prom433/commit/7184aed72c6a742727299c7818318b243471f7ef))


## v0.2.4 (2021-12-09)

### Bug Fixes

- Fix imports in main script.
  ([`6fa43c8`](https://github.com/andrewjw/prom433/commit/6fa43c88cd05a962c2a9434b061eb9c74ab6f5a1))


## v0.2.3 (2021-12-09)

### Bug Fixes

- Fix build of docker container.
  ([`4797dde`](https://github.com/andrewjw/prom433/commit/4797dde8aedd6eb42ebbefc1ecc889467317477b))


## v0.2.2 (2021-11-24)

### Bug Fixes

- Test commit to trigger docker build.
  ([`bfd3537`](https://github.com/andrewjw/prom433/commit/bfd353798af106b54f770d8b547c5c68ef88f16a))


## v0.2.1 (2021-11-11)

### Bug Fixes

- Fix branch name in coveralls link.
  ([`2803ebe`](https://github.com/andrewjw/prom433/commit/2803ebeb1570e7ef577d84f98bf2719646655db7))


## v0.2.0 (2021-11-11)

### Features

- Add dockerfile.
  ([`dff1cd4`](https://github.com/andrewjw/prom433/commit/dff1cd480d5ec274b3dfb8867835ab933ec3454c))


## v0.1.0 (2021-11-11)

### Features

- Add tests for the http server.
  ([`ba317ae`](https://github.com/andrewjw/prom433/commit/ba317ae393f34546b9b5ccb664b287fda6367e1b))


## v0.0.5 (2021-09-30)

### Bug Fixes

- Fix tagging docker image.
  ([`4824509`](https://github.com/andrewjw/prom433/commit/48245091ee591facd2fcc65aa1d9c915d071624e))


## v0.0.4 (2021-09-30)

### Bug Fixes

- Make docker_push.sh executable.
  ([`384ef6b`](https://github.com/andrewjw/prom433/commit/384ef6bcbb689ddc57aaaac311b1ac0829fb0006))


## v0.0.3 (2021-09-30)

### Bug Fixes

- Fix copy and paste error in setup.py.
  ([`bf6c32b`](https://github.com/andrewjw/prom433/commit/bf6c32b297e2b1a4323caca06dd937a6b59752f0))


## v0.0.2 (2021-09-30)

- Initial Release
