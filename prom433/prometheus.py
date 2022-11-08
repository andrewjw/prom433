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
    "prom433_last_message": {}
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

FREQ_HELP = "The frequency the last message was received on."
FREQ_TYPE = "guage"

RSSI_HELP = "The RSSI of the last message."
RSSI_TYPE = "guage"

SNR_HELP = "The Signal to noise ratio of the last message."
SNR_TYPE = "guage"

NOISE_HELP = "The noise level of the last message."
NOISE_TYPE = "guage"

METRICS_PREFIXES = {
    "prom433_battery_ok": [BATTERY_HELP, BATTERY_TYPE],
    "prom433_temperature": [TEMP_HELP, TEMP_TYPE],
    "prom433_humidity": [HUMIDITY_HELP, HUMIDITY_TYPE],
    "prom433_wind_dir_deg": [WIND_DIR_HELP, WIND_DIR_TYPE],
    "prom433_wind_avg": [WIND_AVG_HELP, WIND_AVG_TYPE],
    "prom433_wind_max": [WIND_MAX_HELP, WIND_MAX_TYPE],
    "prom433_rain": [RAIN_HELP, RAIN_TYPE],
    "prom433_last_message": [LAST_MESSAGE_HELP, LAST_MESSAGE_TYPE],
    "prom433_freq": [FREQ_HELP, FREQ_TYPE],
    "prom433_rssi": [RSSI_HELP, RSSI_TYPE],
    "prom433_snr": [SNR_HELP, SNR_TYPE],
    "prom433_noise": [NOISE_HELP, NOISE_TYPE]
}

TAG_KEYS = {"id", "channel", "model"}

IGNORE_TAGS = {
    "*": {"mic", "mod"},
    "Fineoffset-WHx080": {"subtype"}
}

METRIC_NAME = {
    "battery_ok": "prom433_battery_ok",
    "temperature_C": "prom433_temperature",
    "humidity": "prom433_humidity",
    "wind_dir_deg": "prom433_wind_dir_deg",
    "wind_avg_km_h": "prom433_wind_avg",
    "wind_max_km_h": "prom433_wind_max",
    "rain_mm": "prom433_rain",
    "last_message": "prom433_last_message",
    "freq": "prom433_freq",
    "rssi": "prom433_rssi",
    "snr": "prom433_snr",
    "noise": "prom433_noise"
}

# {"time" : "2021-05-08 15:27:58", "model" : "Fineoffset-WHx080",
# "subtype" : 0, "id" : 202, "battery_ok" : 0, "temperature_C" : 6.900,
# "humidity" : 63, "wind_dir_deg" : 158, "wind_avg_km_h" : 4.896,
# "wind_max_km_h" : 8.568, "rain_mm" : 2.400, "mic" : "CRC"}
# {"time" : "2021-05-08 15:28:02", "model" : "Nexus-TH", "id" : 177,
# "channel" : 3, "battery_ok" : 0, "temperature_C" : 21.300, "humidity" : 39}
# {"time":"2022-11-08 14:54:14","model":"Eurochron-EFTH800",
# "id":3672,"channel":6,"battery_ok":1,"temperature_C":20.5,"humidity":60,"mic":"CRC",
# "mod":"ASK","freq":433.91904,"rssi":-0.117409,"snr":20.23702,"noise":-20.3544}


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

    METRICS["prom433_last_message"][tag_value] = time_value
    for key in data:
        metric = METRIC_NAME[key]
        if metric not in METRICS:
            METRICS[metric] = {}
        METRICS[metric][tag_value] = payload[key]

    unknown = {key: value for (key, value) in unknown.items() if key not in
               (IGNORE_TAGS["*"] | IGNORE_TAGS.get(tags["model"], set()))}

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
