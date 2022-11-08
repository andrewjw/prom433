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

from datetime import datetime
import json
import logging

METRICS = {
    "prom433_last_messsage": {}
}

HELP_FORMAT = "#HELP %s %s"
TYPE_FORMAT = "#TYPE %s %s "
METRIC_FORMAT = "%s{%s} %f"

TEMP_HELP = \
    "The temperature in degrees celcius."
TEMP_TYPE = "gauge"

HUMIDITY_HELP = "The humidity in %."
HUMIDITY_TYPE = "gauge"

WIND_AVG_HELP = "The average windspeed in km/h."
WIND_AVG_TYPE = "gauge"
WIND_MAX_HELP = "The maximum windspeed in km/h."
WIND_MAX_TYPE = "gauge"
WIND_DIR_HELP = "The wind direction in degrees."
WIND_DIR_TYPE = "gauge"

RAIN_HELP = "The total rainfall in mm."
RAIN_TYPE = "counter"

BATTERY_HELP = "The battery status."
BATTERY_TYPE = "gauge"

LAST_MESSAGE_HELP = "The time the last message was received."
LAST_MESSAGE_TYPE = "counter"

METRICS_PREFIXES = {
    "prom433_battery_ok": [BATTERY_HELP, BATTERY_TYPE],
    "prom433_temperature": [TEMP_HELP, TEMP_TYPE],
    "prom433_humidity": [HUMIDITY_HELP, HUMIDITY_TYPE],
    "prom433_wind_dir_deg": [WIND_DIR_HELP, WIND_DIR_TYPE],
    "prom433_wind_avg": [WIND_AVG_HELP, WIND_AVG_TYPE],
    "prom433_wind_max": [WIND_MAX_HELP, WIND_MAX_TYPE],
    "prom433_rain": [RAIN_HELP, RAIN_TYPE],
    "prom433_last_messsage": [LAST_MESSAGE_HELP, LAST_MESSAGE_TYPE]
}

TAG_KEYS = {"id", "channel", "model"}

METRIC_NAME = {
    "battery_ok": "prom433_battery_ok",
    "temperature_C": "prom433_temperature",
    "humidity": "prom433_humidity",
    "wind_dir_deg": "prom433_wind_dir_deg",
    "wind_avg_km_h": "prom433_wind_avg",
    "wind_max_km_h": "prom433_wind_max",
    "rain_mm": "prom433_rain",
    "last_message": "prom433_last_message"
}

# {"time" : "2021-05-08 15:27:58", "model" : "Fineoffset-WHx080",
# "subtype" : 0, "id" : 202, "battery_ok" : 0, "temperature_C" : 6.900,
# "humidity" : 63, "wind_dir_deg" : 158, "wind_avg_km_h" : 4.896,
# "wind_max_km_h" : 8.568, "rain_mm" : 2.400, "mic" : "CRC"}
# {"time" : "2021-05-08 15:28:02", "model" : "Nexus-TH", "id" : 177,
# "channel" : 3, "battery_ok" : 0, "temperature_C" : 21.300, "humidity" : 39}


def prometheus(message):
    payload = json.loads(message)

    tags, data, unknown = {}, {}, {}

    for key, value in payload.items():
        if key == "time":
            time_value = datetime.strptime(payload[key], "%Y-%m-%d %H:%M:%S") \
                        .timestamp()
        elif key in TAG_KEYS:
            tags[key] = value
        elif key in METRIC_NAME:
            data[key] = value
        else:
            unknown[key] = value

    tag_value = ", ".join(["%s=\"%s\"" % (k, payload[k])
                           for k in sorted(tags)])

    METRICS["prom433_last_messsage"][tag_value] = time_value
    for key in data:
        metric = METRIC_NAME[key]
        if metric not in METRICS:
            METRICS[metric] = {}
        METRICS[metric][tag_value] = payload[key]

    if len(unknown) > 0:
        logging.warn(f"Message has unknown tags ({unknown}): {message}")


def get_metrics():
    lines = []
    for metric_name in sorted(METRICS.keys()):
        lines.append(HELP_FORMAT
                     % (metric_name, METRICS_PREFIXES[metric_name][0]))
        lines.append(TYPE_FORMAT
                     % (metric_name, METRICS_PREFIXES[metric_name][1]))
        for (tags, values) in METRICS[metric_name].items():
            lines.append(METRIC_FORMAT % (metric_name, tags, values))

    return "\n".join(lines)
