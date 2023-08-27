# prom433

[![Pipeline](https://github.com/andrewjw/prom433/actions/workflows/build.yaml/badge.svg)](https://github.com/andrewjw/prom433/actions/workflows/build.yaml)
[![PyPI version](https://badge.fury.io/py/prom433.svg)](https://pypi.org/project/prom433/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/prom433)](https://pypi.org/project/prom433/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/andrewjw/prom433)](https://hub.docker.com/r/andrewjw/prom433)
[![Docker Pulls](https://img.shields.io/docker/pulls/andrewjw/prom433)](https://hub.docker.com/r/andrewjw/prom433)
[![Coverage Status](https://coveralls.io/repos/github/andrewjw/prom433/badge.svg?branch=main)](https://coveralls.io/github/andrewjw/prom433?branch=master)

Exposes Prometheus metrics based on data received by `rtl_433`.

To use this you need to also be running [`rtl_433`](https://github.com/merbanan/rtl_433)
and an MQTT broker. Configure rtl_433 to report its messages to MQTT (by running `rtl_433 -F mqtt://mqttbroker:1883`)
and then point `prom433` to the same broker (`prom433 --mqtt mqtt://mqttbroker:1883`)

You may find it useful to pass `-M level` to `rtl_433`, which will add frequency
and signal strength details to the messages received. These will be exposed as
additional metrics.

```
usage: prom433 [-h] [-q] [--bind [BIND]] [--mqtt [MQTT]] [--drop-after [DROP_AFTER]]

Listens to messages from rtl_433 and exposes them as prometheus metrics

options:
  -h, --help            show this help message and exit
  -q, --quiet           don't log HTTP requests
  --bind [BIND]         the ip address and port to bind to. Default: *:9100
  --mqtt [MQTT]         the mqtt host to connect to. Default: mqtt:1883
  --drop-after [DROP_AFTER]
                        drop metrics this many seconds after the device was last seen. 0 disables
                        dropping metrics
```

By default the metrics are exposed on port 9100 (configure using `--bind`). To
scrape the metrics with Prometheus, add the following to your `promethus.cfg` file.

```
scrape_configs:
  - job_name: 'prom433'
    static_configs:
      - targets: ['hostname:9100']
```

What metrics are exposed depends on what devices are detected by `rtl_433`. Below
is an example of the metrics that could be exposed. If you have other devices, 
please free to raise an issue so we can add more supported device types.

```
#HELP prom433_battery_ok The battery status.
#TYPE prom433_battery_ok gauge 
prom433_battery_ok{id="250", model="Fineoffset-WHx080"} 1.000000
prom433_battery_ok{channel="3", id="91", model="Nexus-TH"} 1.000000
prom433_battery_ok{channel="6", id="3672", model="Eurochron-EFTH800"} 1.000000
prom433_battery_ok{channel="4", id="1864", model="Eurochron-EFTH800"} 1.000000
prom433_battery_ok{channel="1", id="146", model="Nexus-TH"} 0.000000
prom433_battery_ok{channel="2", id="480", model="Eurochron-EFTH800"} 1.000000
prom433_battery_ok{channel="5", id="2492", model="Eurochron-EFTH800"} 1.000000
prom433_battery_ok{channel="E", id="11922", model="Acurite-3n1"} 0.000000
#HELP prom433_freq The frequency the last message was received on.
#TYPE prom433_freq guage 
prom433_freq{id="250", model="Fineoffset-WHx080"} 433.936990
prom433_freq{channel="3", id="91", model="Nexus-TH"} 433.936990
prom433_freq{channel="6", id="3672", model="Eurochron-EFTH800"} 433.929380
prom433_freq{channel="4", id="1864", model="Eurochron-EFTH800"} 433.929090
prom433_freq{channel="1", id="146", model="Nexus-TH"} 434.127870
prom433_freq{channel="2", id="480", model="Eurochron-EFTH800"} 433.926750
prom433_freq{channel="5", id="2492", model="Eurochron-EFTH800"} 433.925700
prom433_freq{id="225212", model="Akhan-100F14"} 434.023230
prom433_freq{channel="E", id="11922", model="Acurite-3n1"} 433.929090
#HELP prom433_humidity The humidity in %.
#TYPE prom433_humidity gauge 
prom433_humidity{id="250", model="Fineoffset-WHx080"} 61.000000
prom433_humidity{channel="3", id="91", model="Nexus-TH"} 53.000000
prom433_humidity{channel="6", id="3672", model="Eurochron-EFTH800"} 60.000000
prom433_humidity{channel="4", id="1864", model="Eurochron-EFTH800"} 60.000000
prom433_humidity{channel="1", id="146", model="Nexus-TH"} 55.000000
prom433_humidity{channel="2", id="480", model="Eurochron-EFTH800"} 61.000000
prom433_humidity{channel="5", id="2492", model="Eurochron-EFTH800"} 60.000000
prom433_humidity{channel="E", id="11922", model="Acurite-3n1"} 52.000000
#HELP prom433_last_message The time the last message was received.
#TYPE prom433_last_message counter 
prom433_last_message{id="250", model="Fineoffset-WHx080"} 1668007594.000000
prom433_last_message{channel="3", id="91", model="Nexus-TH"} 1668007594.000000
prom433_last_message{channel="6", id="3672", model="Eurochron-EFTH800"} 1668007521.000000
prom433_last_message{channel="4", id="1864", model="Eurochron-EFTH800"} 1668007563.000000
prom433_last_message{channel="1", id="146", model="Nexus-TH"} 1668007581.000000
prom433_last_message{channel="2", id="480", model="Eurochron-EFTH800"} 1668007586.000000
prom433_last_message{channel="5", id="2492", model="Eurochron-EFTH800"} 1668007306.000000
prom433_last_message{id="225212", model="Akhan-100F14"} 1668001774.000000
prom433_last_message{channel="E", id="11922", model="Acurite-3n1"} 1668007563.000000
#HELP prom433_noise The noise level of the last message.
#TYPE prom433_noise guage 
prom433_noise{id="250", model="Fineoffset-WHx080"} -18.526900
prom433_noise{channel="3", id="91", model="Nexus-TH"} -18.526900
prom433_noise{channel="6", id="3672", model="Eurochron-EFTH800"} -18.564800
prom433_noise{channel="4", id="1864", model="Eurochron-EFTH800"} -19.449100
prom433_noise{channel="1", id="146", model="Nexus-TH"} -18.720000
prom433_noise{channel="2", id="480", model="Eurochron-EFTH800"} -18.526900
prom433_noise{channel="5", id="2492", model="Eurochron-EFTH800"} -18.360200
prom433_noise{id="225212", model="Akhan-100F14"} -14.399000
prom433_noise{channel="E", id="11922", model="Acurite-3n1"} -19.449100
#HELP prom433_rain The total rainfall in mm.
#TYPE prom433_rain counter 
prom433_rain{id="250", model="Fineoffset-WHx080"} 863.700010
#HELP prom433_rssi The RSSI of the last message.
#TYPE prom433_rssi guage 
prom433_rssi{id="250", model="Fineoffset-WHx080"} -0.112511
prom433_rssi{channel="3", id="91", model="Nexus-TH"} -0.112511
prom433_rssi{channel="6", id="3672", model="Eurochron-EFTH800"} -0.186035
prom433_rssi{channel="4", id="1864", model="Eurochron-EFTH800"} -0.117409
prom433_rssi{channel="1", id="146", model="Nexus-TH"} -1.056520
prom433_rssi{channel="2", id="480", model="Eurochron-EFTH800"} -0.126133
prom433_rssi{channel="5", id="2492", model="Eurochron-EFTH800"} -0.143085
prom433_rssi{id="225212", model="Akhan-100F14"} -6.768530
prom433_rssi{channel="E", id="11922", model="Acurite-3n1"} -0.117409
#HELP prom433_snr The Signal to noise ratio of the last message.
#TYPE prom433_snr guage 
prom433_snr{id="250", model="Fineoffset-WHx080"} 18.414410
prom433_snr{channel="3", id="91", model="Nexus-TH"} 18.414410
prom433_snr{channel="6", id="3672", model="Eurochron-EFTH800"} 18.378820
prom433_snr{channel="4", id="1864", model="Eurochron-EFTH800"} 19.331660
prom433_snr{channel="1", id="146", model="Nexus-TH"} 17.663450
prom433_snr{channel="2", id="480", model="Eurochron-EFTH800"} 18.400790
prom433_snr{channel="5", id="2492", model="Eurochron-EFTH800"} 18.217140
prom433_snr{id="225212", model="Akhan-100F14"} 7.630500
prom433_snr{channel="E", id="11922", model="Acurite-3n1"} 19.331660
#HELP prom433_temperature The temperature in degrees celcius.
#TYPE prom433_temperature gauge 
prom433_temperature{id="250", model="Fineoffset-WHx080"} 13.600000
prom433_temperature{channel="3", id="91", model="Nexus-TH"} 20.000000
prom433_temperature{channel="6", id="3672", model="Eurochron-EFTH800"} 19.000000
prom433_temperature{channel="4", id="1864", model="Eurochron-EFTH800"} 19.600000
prom433_temperature{channel="1", id="146", model="Nexus-TH"} 20.400000
prom433_temperature{channel="2", id="480", model="Eurochron-EFTH800"} 18.700000
prom433_temperature{channel="5", id="2492", model="Eurochron-EFTH800"} 20.000000
#HELP prom433_wind_avg The average windspeed in km/h.
#TYPE prom433_wind_avg gauge 
prom433_wind_avg{id="250", model="Fineoffset-WHx080"} 3.672000
#HELP prom433_wind_dir_deg The wind direction in degrees.
#TYPE prom433_wind_dir_deg gauge 
prom433_wind_dir_deg{id="250", model="Fineoffset-WHx080"} 270.000000
#HELP prom433_wind_max The maximum windspeed in km/h.
#TYPE prom433_wind_max gauge 
prom433_wind_max{id="250", model="Fineoffset-WHx080"} 4.896000
```
