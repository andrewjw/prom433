# rtl_433
# Copyright (C) 2021 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import logging

METRICS = {}

WEATHER_METRIC = "%s{id=\"%i\"} %f"

WEATHER_TEMP_HELP = \
    "# HELP weather_temperature The temperature in degrees celcius."
WEATHER_TEMP_TYPE = "# TYPE weather_temperature gauge"

WEATHER_HUM_HELP = "# HELP weather_humidity The humidity in %."
WEATHER_HUM_TYPE = "# TYPE weather_humidity gauge"

WEATHER_WIND_AVG_HELP = \
    "# HELP weather_wind_avg The average windspeed in km/h."
WEATHER_WIND_AVG_TYPE = "# TYPE weather_wind_avg gauge"
WEATHER_WIND_MAX_HELP = \
    "# HELP weather_wind_max The maximum windspeed in km/h."
WEATHER_WIND_MAX_TYPE = "# TYPE weather_wind_max gauge"
WEATHER_WIND_DIR_HELP = \
    "# HELP weather_wind_dir The wind direction in degrees."
WEATHER_WIND_DIR_TYPE = "# TYPE weather_wind_dir gauge"

WEATHER_RAIN_HELP = "# HELP weather_rain The total rainfall in mm."
WEATHER_RAIN_TYPE = "# TYPE weather_rain counter"

WEATHER_BATTERY_HELP = "# HELP weather_rain The battery status."
WEATHER_BATTERY_TYPE = "# TYPE weather_battery gauge"

NEXUS_METRIC = "%s{id=\"%i\", channel=\"%i\"} %f"

NEXUS_TEMP_HELP = \
    "# HELP nexus_temperature The temperature in degrees celcius."
NEXUS_TEMP_TYPE = "# TYPE nexus_temperature gauge"
NEXUS_HUM_HELP = "# HELP nexus_humidity The humidity in %."
NEXUS_HUM_TYPE = "# TYPE nexus_humidity gauge"
NEXUS_BATTERY_HELP = "# HELP nexus_battery The battery status."
NEXUS_BATTERY_TYPE = "# TYPE nexus_battery gauge"

METRICS_PREFIXES = {
    "weather_temperature": [WEATHER_TEMP_HELP, WEATHER_TEMP_TYPE],
    "nexus_temperature": [NEXUS_TEMP_HELP, NEXUS_TEMP_TYPE],
}

METRIC_FORMATS = {
    "weather_temperature": WEATHER_METRIC,
    "nexus_temperature": NEXUS_METRIC
}

# {"time" : "2021-05-08 15:27:58", "model" : "Fineoffset-WHx080",
# "subtype" : 0, "id" : 202, "battery_ok" : 0, "temperature_C" : 6.900,
# "humidity" : 63, "wind_dir_deg" : 158, "wind_avg_km_h" : 4.896,
# "wind_max_km_h" : 8.568, "rain_mm" : 2.400, "mic" : "CRC"}
# {"time" : "2021-05-08 15:28:02", "model" : "Nexus-TH", "id" : 177,
# "channel" : 3, "battery_ok" : 0, "temperature_C" : 21.300, "humidity" : 39}


def prometheus(line):
    payload = json.loads(line)

    if payload["model"] == "Fineoffset-WHx080":
        weather(payload)
    elif payload["model"] == "Nexus-TH":
        nexus(payload)
    else:
        model = payload["model"]
        logging.warn(f"Unknown message model {model}")


def get_metrics():
    lines = []
    for metric_name in sorted(set([m[0] for m in METRICS])):
        lines.extend(METRICS_PREFIXES[metric_name])
        for metric_key, value in METRICS.items():
            if metric_key[0] == metric_name:
                lines.append(METRIC_FORMATS[metric_name]
                             % (metric_key + (value, )))

    return "\n".join(lines)


def weather(payload):
    METRICS[("weather_temperature", payload["id"])] = payload["temperature_C"]


def nexus(payload):
    METRICS[("nexus_temperature", payload["id"], payload["channel"])] = \
        payload["temperature_C"]
