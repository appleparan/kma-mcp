"""Weather code conversion utilities for Korean descriptions.

This module provides functions to convert weather codes and values
to human-readable Korean descriptions.
"""

import contextlib
from typing import Any

# Wind direction mapping (English to Korean)
WIND_DIRECTION_KR = {
    'N': '북',
    'NNE': '북북동',
    'NE': '북동',
    'ENE': '동북동',
    'E': '동',
    'ESE': '동남동',
    'SE': '남동',
    'SSE': '남남동',
    'S': '남',
    'SSW': '남남서',
    'SW': '남서',
    'WSW': '서남서',
    'W': '서',
    'WNW': '서북서',
    'NW': '북서',
    'NNW': '북북서',
}

# Degree to direction mapping (0-360 degrees)
DEGREE_TO_DIRECTION = {
    0: 'N',
    22.5: 'NNE',
    45: 'NE',
    67.5: 'ENE',
    90: 'E',
    112.5: 'ESE',
    135: 'SE',
    157.5: 'SSE',
    180: 'S',
    202.5: 'SSW',
    225: 'SW',
    247.5: 'WSW',
    270: 'W',
    292.5: 'WNW',
    315: 'NW',
    337.5: 'NNW',
    360: 'N',
}

# Precipitation type codes (강수형태)
PRECIPITATION_TYPE = {
    0: '강수 없음',
    1: '비',
    2: '비/눈',
    3: '눈',
    4: '소나기',
    5: '빗방울',
    6: '진눈깨비',
    7: '눈날림',
}

# Sky condition codes (하늘상태)
SKY_CONDITION = {
    1: '맑음',
    3: '구름많음',
    4: '흐림',
}

# Weather phenomenon codes (기상현상)
WEATHER_PHENOMENON = {
    0: '없음',
    1: '비',
    2: '비/눈',
    3: '눈',
    4: '소나기',
}


def deg_to_direction(degree: float) -> str:
    """Convert degree (0-360) to wind direction code (N, NE, E, etc.).

    Args:
        degree: Wind direction in degrees (0-360)

    Returns:
        Direction code (e.g., 'N', 'NE', 'E')

    Example:
        >>> deg_to_direction(0)
        'N'
        >>> deg_to_direction(45)
        'NE'
        >>> deg_to_direction(90)
        'E'
    """
    # Normalize degree to 0-360 range
    degree = degree % 360

    # Find closest direction
    directions = list(DEGREE_TO_DIRECTION.keys())
    closest = min(directions, key=lambda x: min(abs(degree - x), abs(degree - x + 360)))

    return DEGREE_TO_DIRECTION[closest]


def deg_to_direction_kr(degree: float) -> str:
    """Convert degree (0-360) to Korean wind direction.

    Args:
        degree: Wind direction in degrees (0-360)

    Returns:
        Korean direction (e.g., '북', '북동', '동')

    Example:
        >>> deg_to_direction_kr(0)
        '북'
        >>> deg_to_direction_kr(45)
        '북동'
        >>> deg_to_direction_kr(90)
        '동'
    """
    direction = deg_to_direction(degree)
    return WIND_DIRECTION_KR[direction]


def direction_to_kr(direction: str) -> str:
    """Convert English wind direction to Korean.

    Args:
        direction: Wind direction in English (e.g., 'N', 'NE', 'E')

    Returns:
        Korean direction (e.g., '북', '북동', '동')

    Example:
        >>> direction_to_kr('N')
        '북'
        >>> direction_to_kr('NE')
        '북동'
    """
    return WIND_DIRECTION_KR.get(direction.upper(), direction)


def precipitation_type_to_kr(code: int) -> str:
    """Convert precipitation type code to Korean description.

    Args:
        code: Precipitation type code (0-7)

    Returns:
        Korean precipitation type description

    Example:
        >>> precipitation_type_to_kr(0)
        '강수 없음'
        >>> precipitation_type_to_kr(1)
        '비'
        >>> precipitation_type_to_kr(3)
        '눈'
    """
    return PRECIPITATION_TYPE.get(code, f'알 수 없음 ({code})')


def sky_condition_to_kr(code: int) -> str:
    """Convert sky condition code to Korean description.

    Args:
        code: Sky condition code (1, 3, 4)

    Returns:
        Korean sky condition description

    Example:
        >>> sky_condition_to_kr(1)
        '맑음'
        >>> sky_condition_to_kr(3)
        '구름많음'
        >>> sky_condition_to_kr(4)
        '흐림'
    """
    return SKY_CONDITION.get(code, f'알 수 없음 ({code})')


def weather_phenomenon_to_kr(code: int) -> str:
    """Convert weather phenomenon code to Korean description.

    Args:
        code: Weather phenomenon code (0-4)

    Returns:
        Korean weather phenomenon description

    Example:
        >>> weather_phenomenon_to_kr(0)
        '없음'
        >>> weather_phenomenon_to_kr(1)
        '비'
    """
    return WEATHER_PHENOMENON.get(code, f'알 수 없음 ({code})')


def enhance_weather_data(data: dict[str, Any]) -> dict[str, Any]:
    """Enhance weather data with Korean descriptions.

    Adds Korean descriptions for wind direction, precipitation type,
    sky condition, and weather phenomena based on code values.

    Args:
        data: Weather data dictionary

    Returns:
        Enhanced data dictionary with Korean descriptions

    Example:
        >>> data = {'wdDeg': 45, 'pty': 1, 'sky': 3}
        >>> enhanced = enhance_weather_data(data)
        >>> enhanced['wdDeg_kr']
        '북동'
        >>> enhanced['pty_kr']
        '비'
        >>> enhanced['sky_kr']
        '구름많음'
    """
    enhanced = data.copy()

    # Wind direction from degrees
    if 'wdDeg' in data and data['wdDeg'] is not None:
        with contextlib.suppress(ValueError, TypeError):
            enhanced['wdDeg_kr'] = deg_to_direction_kr(float(data['wdDeg']))

    # Wind direction from code
    if 'wd' in data and isinstance(data['wd'], str):
        enhanced['wd_kr'] = direction_to_kr(data['wd'])

    # Precipitation type
    if 'pty' in data and data['pty'] is not None:
        with contextlib.suppress(ValueError, TypeError):
            enhanced['pty_kr'] = precipitation_type_to_kr(int(data['pty']))

    # Sky condition
    if 'sky' in data and data['sky'] is not None:
        with contextlib.suppress(ValueError, TypeError):
            enhanced['sky_kr'] = sky_condition_to_kr(int(data['sky']))

    # Weather phenomenon
    if 'wf' in data and data['wf'] is not None:
        with contextlib.suppress(ValueError, TypeError):
            enhanced['wf_kr'] = weather_phenomenon_to_kr(int(data['wf']))

    return enhanced


def format_weather_summary(data: dict[str, Any]) -> str:
    """Format weather data as a human-readable Korean summary.

    Args:
        data: Weather data dictionary

    Returns:
        Formatted Korean summary string

    Example:
        >>> data = {
        ...     'stnNm': '서울',
        ...     'ta': 15.5,
        ...     'hm': 65,
        ...     'wdDeg': 45,
        ...     'ws': 3.2,
        ...     'pty': 0,
        ...     'sky': 1
        ... }
        >>> print(format_weather_summary(data))
        [서울] 기온: 15.5°C, 습도: 65%, 풍향: 북동, 풍속: 3.2m/s, 강수: 강수 없음, 하늘: 맑음
    """
    enhanced = enhance_weather_data(data)
    parts = []

    # Station name
    if 'stnNm' in enhanced:
        parts.append(f'[{enhanced["stnNm"]}]')

    # Temperature
    if 'ta' in enhanced and enhanced['ta'] is not None:
        parts.append(f'기온: {enhanced["ta"]}°C')

    # Humidity
    if 'hm' in enhanced and enhanced['hm'] is not None:
        parts.append(f'습도: {enhanced["hm"]}%')

    # Wind direction
    if 'wdDeg_kr' in enhanced:
        parts.append(f'풍향: {enhanced["wdDeg_kr"]}')
    elif 'wd_kr' in enhanced:
        parts.append(f'풍향: {enhanced["wd_kr"]}')

    # Wind speed
    if 'ws' in enhanced and enhanced['ws'] is not None:
        parts.append(f'풍속: {enhanced["ws"]}m/s')

    # Precipitation type
    if 'pty_kr' in enhanced:
        parts.append(f'강수: {enhanced["pty_kr"]}')

    # Sky condition
    if 'sky_kr' in enhanced:
        parts.append(f'하늘: {enhanced["sky_kr"]}')

    # Precipitation amount
    if 'rn' in enhanced and enhanced['rn'] is not None and enhanced['rn'] != 0:
        parts.append(f'강수량: {enhanced["rn"]}mm')

    return ', '.join(parts)
