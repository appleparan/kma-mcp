"""FastMCP server for KMA ASOS API.

This module provides an MCP (Model Context Protocol) server that exposes
KMA ASOS weather observation data through standardized tools.
"""

import os
from datetime import datetime

from fastmcp import FastMCP

from kma_mcp.asos_client import ASOSClient

# Initialize FastMCP server
mcp = FastMCP('KMA ASOS Weather Data')

# Get API key from environment
API_KEY = os.getenv('KMA_API_KEY', '')


@mcp.tool()
def get_current_weather(station_id: int = 0) -> str:
    """Get current hourly weather observation data.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)
                   Common stations:
                   - 108: Seoul
                   - 112: Incheon
                   - 133: Daejeon
                   - 159: Busan
                   - 184: Jeju

    Returns:
        Current weather observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with ASOSClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now()
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:
        return f'Error fetching weather data: {e!s}'


@mcp.tool()
def get_hourly_weather(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get hourly weather observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format (max 31 days from start)
        station_id: Weather station ID (0 for all stations)

    Returns:
        Hourly weather observation data for the period in JSON format

    Example:
        get_hourly_weather('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with ASOSClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:
        return f'Error fetching hourly weather data: {e!s}'


@mcp.tool()
def get_daily_weather(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get daily weather observation data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily weather observation data for the period in JSON format

    Example:
        get_daily_weather('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with ASOSClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:
        return f'Error fetching daily weather data: {e!s}'


@mcp.tool()
def get_temperature_data(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get temperature observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Temperature data in JSON format

    Example:
        get_temperature_data('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with ASOSClient(API_KEY) as client:
            # TA is the code for temperature (기온)
            data = client.get_element_data(tm1=start_time, tm2=end_time, obs='TA', stn=station_id)
            return str(data)
    except Exception as e:
        return f'Error fetching temperature data: {e!s}'


@mcp.tool()
def get_precipitation_data(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get precipitation observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Precipitation data in JSON format

    Example:
        get_precipitation_data('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with ASOSClient(API_KEY) as client:
            # RN is the code for precipitation (강수량)
            data = client.get_element_data(tm1=start_time, tm2=end_time, obs='RN', stn=station_id)
            return str(data)
    except Exception as e:
        return f'Error fetching precipitation data: {e!s}'


@mcp.tool()
def list_station_info() -> str:
    """Get information about common weather stations.

    Returns:
        Dictionary of common weather station IDs and names
    """
    stations = {
        108: 'Seoul (서울)',
        112: 'Incheon (인천)',
        119: 'Suwon (수원)',
        133: 'Daejeon (대전)',
        143: 'Daegu (대구)',
        146: 'Jeonju (전주)',
        156: 'Gwangju (광주)',
        159: 'Busan (부산)',
        184: 'Jeju (제주)',
        185: 'Seogwipo (서귀포)',
        192: 'Jinju (진주)',
        202: 'Yangyang (양양)',
        203: 'Inje (인제)',
        211: 'Hongcheon (홍천)',
        216: 'Taebaek (태백)',
        226: 'Jecheon (제천)',
        235: 'Boeun (보은)',
        236: 'Cheonan (천안)',
        238: 'Boryeong (보령)',
        243: 'Buyeo (부여)',
        244: 'Geumsan (금산)',
        245: 'Seosan (서산)',
        247: 'Yeongju (영주)',
        248: 'Mungyeong (문경)',
        251: 'Yeongdeok (영덕)',
        252: 'Uiseong (의성)',
        253: 'Gumi (구미)',
        254: 'Yeongcheon (영천)',
        255: 'Geochang (거창)',
        257: 'Hapcheon (합천)',
        260: 'Miryang (밀양)',
        261: 'Sancheong (산청)',
        262: 'Geoje (거제)',
        263: 'Namhae (남해)',
        271: 'Buan (부안)',
        272: 'Jeongeup (정읍)',
        273: 'Namwon (남원)',
        276: 'Jangheung (장흥)',
        277: 'Haenam (해남)',
        278: 'Goheung (고흥)',
        279: 'Yeongam (영암)',
        281: 'Gangjin (강진)',
        294: 'Seongsan (성산)',
        295: 'Gosan (고산)',
    }

    return str(stations)


if __name__ == '__main__':
    # Run the MCP server
    mcp.run()
