# Changelog

<!--next-version-placeholder-->

## v2.3.0 (2023-03-09)
### Feature
* Add time parser ([#17](https://github.com/andrewjw/prom433/issues/17)) ([`023ee63`](https://github.com/andrewjw/prom433/commit/023ee63ee986c87d6e9a00a493cd7b98101d4cca))

## v2.2.0 (2023-02-28)
### Feature
* Add metrics ([`f804439`](https://github.com/andrewjw/prom433/commit/f804439ce30dfbbcde4726a1aa78398ff1454fcf))
* Add --quiet to suppress server logging ([`9770f43`](https://github.com/andrewjw/prom433/commit/9770f433f2e2bb2825aabceaefc2b73660e99234))

## v2.1.2 (2023-02-27)
### Fix
* Allow OS to choose Python version ([`bc56611`](https://github.com/andrewjw/prom433/commit/bc566119735500c546bc54aed1d4cd08a97b39cc))

## v2.1.1 (2023-02-23)
### Fix
* Treat all radio clocks as UTC so we return the correct time, regardless of the host's timezone (fix #11). ([`be71083`](https://github.com/andrewjw/prom433/commit/be7108383651c78f85d9d6e42f20c9e57ac74789))

## v2.1.0 (2023-01-20)
### Feature
* Add support for radio clock values. ([`525191a`](https://github.com/andrewjw/prom433/commit/525191a1b421c70fbd2f8bb4d24cdbce2861e038))

## v2.0.0 (2022-11-10)
### Feature
* Drop metrics after a configurable timeout (default 1 hour), so we don't continually report devices we've only seen once. ([`1197e2d`](https://github.com/andrewjw/prom433/commit/1197e2d1018264c938ca6e3756e459cdb11fa970))

### Breaking
* Metrics will be dropped after 1 hour if not updated. Add --drop-after 0 to keep the old behaviour.  ([`1197e2d`](https://github.com/andrewjw/prom433/commit/1197e2d1018264c938ca6e3756e459cdb11fa970))

## v1.1.4 (2022-11-09)
### Fix
* Since we switched to mqtt there is no need to install rtl_433 in our Docker image. ([`5f2c147`](https://github.com/andrewjw/prom433/commit/5f2c147008b049e8bb6a0400b1f36c1725e6640d))

## v1.1.3 (2022-11-09)
### Fix
* Handle exceptions when processing messages and keep running. ([`a3295fe`](https://github.com/andrewjw/prom433/commit/a3295fe25b78286c752e7525195e537b9d07bbfc))

## v1.1.2 (2022-11-08)
### Fix
* Fix typo in last message metric name. ([`f6d5288`](https://github.com/andrewjw/prom433/commit/f6d52886cce06c2d4a4d7f22e6edca4d081b14c8))

## v1.1.1 (2022-11-08)
### Fix
* Don't warn on tag values we known we should ignore. ([`b6f7c77`](https://github.com/andrewjw/prom433/commit/b6f7c77acae7b3ce924d854134ef395ce1b9de8f))

## v1.1.0 (2022-11-08)
### Feature
* Handle extra values about frequency and noise that are added to messages sent by rtl_433 with -M level. ([`36aa076`](https://github.com/andrewjw/prom433/commit/36aa076774b8eb35c7590f70e1ce338eb3643651))

## v1.0.0 (2022-11-08)
### Feature
* Rework metrics so we can handle more types of messages, and record the last time a message was seen for a device. ([`57d68ec`](https://github.com/andrewjw/prom433/commit/57d68ec69e2c63486ea6466b043eef274e3e68ef))

### Breaking
* All metrics have been renamed.  ([`57d68ec`](https://github.com/andrewjw/prom433/commit/57d68ec69e2c63486ea6466b043eef274e3e68ef))

## v0.4.2 (2022-04-27)
### Fix
* Handle correct type for mqtt messages. ([`01d91ac`](https://github.com/andrewjw/prom433/commit/01d91ac20de8a955e2e981ced0682b2eaaef6661))

## v0.4.1 (2022-04-27)
### Fix
* Fix message handler prototype. ([`2998de3`](https://github.com/andrewjw/prom433/commit/2998de3bf25c3edbd9bdebbf4628bbca4ec152c3))

## v0.4.0 (2022-04-27)
### Feature
* Switch to listening to MQTT messages rather than running rtl_433 directly. ([`1d81a6f`](https://github.com/andrewjw/prom433/commit/1d81a6fd6ad789ba0f195c0fd673b253130c6a45))

## v0.3.4 (2022-02-11)
### Fix
* Use correct parameter for setting rtl_433 output to Json. ([`464dd07`](https://github.com/andrewjw/prom433/commit/464dd079d3af4b8446c2d5f5ebb60d6e9ff7e455))

## v0.3.3 (2022-02-10)
### Fix
* Use correct package name for rtl-433. ([`3589181`](https://github.com/andrewjw/prom433/commit/3589181eff90d74f4f0dab18273ec99c87cfddcb))

## v0.3.2 (2022-02-08)
### Fix
* Add universe repo to allow us to install rtl_433. ([`ca4835e`](https://github.com/andrewjw/prom433/commit/ca4835e6a07be60799fca41253ba9c7a2af3bbce))

## v0.3.1 (2022-02-07)
### Fix
* Add universe repository. ([`f77c19c`](https://github.com/andrewjw/prom433/commit/f77c19c9367bc741323dcf643d497e3c50a328b3))

## v0.3.0 (2022-02-03)
### Feature
* Switch to Python slim image so we can install Python packages more easily. ([`e9e652e`](https://github.com/andrewjw/prom433/commit/e9e652eff0037a29503c89d113d7a5f1d34eb4c2))

## v0.2.5 (2022-01-03)
### Fix
* Use a docker image with rtl_433 installed. ([`7184aed`](https://github.com/andrewjw/prom433/commit/7184aed72c6a742727299c7818318b243471f7ef))

## v0.2.4 (2021-12-09)
### Fix
* Fix imports in main script. ([`6fa43c8`](https://github.com/andrewjw/prom433/commit/6fa43c88cd05a962c2a9434b061eb9c74ab6f5a1))

## v0.2.3 (2021-12-09)
### Fix
* Fix build of docker container. ([`4797dde`](https://github.com/andrewjw/prom433/commit/4797dde8aedd6eb42ebbefc1ecc889467317477b))

## v0.2.2 (2021-11-24)
### Fix
* Test commit to trigger docker build. ([`bfd3537`](https://github.com/andrewjw/prom433/commit/bfd353798af106b54f770d8b547c5c68ef88f16a))

## v0.2.1 (2021-11-11)
### Fix
* Fix branch name in coveralls link. ([`2803ebe`](https://github.com/andrewjw/prom433/commit/2803ebeb1570e7ef577d84f98bf2719646655db7))

## v0.2.0 (2021-11-11)
### Feature
* Add dockerfile. ([`dff1cd4`](https://github.com/andrewjw/prom433/commit/dff1cd480d5ec274b3dfb8867835ab933ec3454c))

## v0.1.0 (2021-11-11)
### Feature
* Add tests for the http server. ([`ba317ae`](https://github.com/andrewjw/prom433/commit/ba317ae393f34546b9b5ccb664b287fda6367e1b))

## v0.0.5 (2021-09-30)
### Fix
* Fix tagging docker image. ([`4824509`](https://github.com/andrewjw/prom433/commit/48245091ee591facd2fcc65aa1d9c915d071624e))

## v0.0.4 (2021-09-30)
### Fix
* Make docker_push.sh executable. ([`384ef6b`](https://github.com/andrewjw/prom433/commit/384ef6bcbb689ddc57aaaac311b1ac0829fb0006))

## v0.0.3 (2021-09-30)
### Fix
* Fix copy and paste error in setup.py. ([`bf6c32b`](https://github.com/andrewjw/prom433/commit/bf6c32b297e2b1a4323caca06dd937a6b59752f0))

## v0.0.2 (2021-09-30)
### Fix
* Set semantic release to release from main. ([`04af98b`](https://github.com/andrewjw/prom433/commit/04af98b0c9b5a39bd4dd87ac5a2003a098894df8))
* Default branch is called main, not master. ([`d5bf17a`](https://github.com/andrewjw/prom433/commit/d5bf17a3aaeb97e8c0051602630433b936bc7736))
* Make the tests pass. ([`5ecfb35`](https://github.com/andrewjw/prom433/commit/5ecfb35721e6d0df1656dfb7feac25798656b7d0))
