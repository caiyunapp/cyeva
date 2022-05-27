"""
This is the module to store wind directions constants.

* DIRECTION8_CENTER_ANGLE: Wind 8 cardinal directions central angles.
* DIRECTION16_CENTER_ANGLE: Wind 16 cardinal directions central angles.
* DIRECTION8_ABBR: Wind 8 cardinal directions abbreviation.
* DIRECTION16_ABBR: Wind 16 cardinal directions abbreviation.
"""

DIRECTION8_CENTER_ANGLE = {0: 0, 1: 45, 2: 90, 3: 135, 4: 180, 5: 225, 6: 270, 7: 315}
DIRECTION16_CENTER_ANGLE = {
    0: 0,
    1: 22.5,
    2: 45,
    3: 67.5,
    4: 90,
    5: 112.5,
    6: 135,
    7: 157.5,
    8: 180,
    9: 202.5,
    10: 225,
    11: 247.5,
    12: 270,
    13: 292.5,
    14: 315,
    15: 337.5,
}

DIRECTION8_ABBR = {0: "N", 1: "NE", 2: "E", 3: "SE", 4: "S", 5: "SW", 6: "W", 7: "NW"}
DIRECTION16_ABBR = {
    0: "N",
    1: "NNE",
    2: "NE",
    3: "ENE",
    4: "E",
    5: "ESE",
    6: "SE",
    7: "SSE",
    8: "S",
    9: "SSW",
    10: "SW",
    11: "WSW",
    12: "W",
    13: "WNW",
    14: "NW",
    15: "NNW",
}
