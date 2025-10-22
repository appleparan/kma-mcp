"""Async FastMCP server for KMA Weather APIs.

This module provides an async MCP (Model Context Protocol) server that exposes
KMA weather observation data through standardized async tools, including:
- ASOS (Automated Synoptic Observing System)
- AWS (Automated Weather Station)
- Climate Statistics
- Dust, UV, Snow observations
- North Korea observations
- Forecast and warnings
- Radar and satellite imagery
- Typhoon tracking
- Marine buoy data
- Upper-air observations
- Earthquake monitoring
"""

import logging
import os
from datetime import UTC, datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from kma_mcp.forecast.async_forecast_client import AsyncForecastClient
from kma_mcp.forecast.async_warning_client import AsyncWarningClient
from kma_mcp.surface.async_asos_client import AsyncASOSClient
from kma_mcp.surface.async_aws_client import AsyncAWSClient
from kma_mcp.surface.async_aws_oa_client import AsyncAWSOAClient
from kma_mcp.surface.async_climate_client import AsyncClimateClient
from kma_mcp.surface.async_dust_client import AsyncDustClient
from kma_mcp.surface.async_nk_client import AsyncNKClient
from kma_mcp.surface.async_season_client import AsyncSeasonClient
from kma_mcp.surface.async_snow_client import AsyncSnowClient
from kma_mcp.surface.async_station_client import AsyncStationClient
from kma_mcp.surface.async_uv_client import AsyncUVClient

# Configure logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
# Look for .env in project root
# Path structure: python/src/kma_mcp/async_mcp_server.py -> go up 4 levels to project root
env_path = Path(__file__).resolve().parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
logger.info('Loading environment from: %s', env_path)

# Initialize FastMCP server
mcp = FastMCP('KMA ASOS Weather Data (Async)')

# Get API key from environment (from .env file or environment variable)
API_KEY = os.getenv('KMA_API_KEY', '')


async def validate_api_key(api_key: str) -> bool:
    """Validate API key by making a simple API call.

    Uses AWS minutely data API as a lightweight validation endpoint.

    Args:
        api_key: KMA API key to validate

    Returns:
        True if API key is valid, False otherwise
    """
    if not api_key:
        logger.error('API key is empty')
        return False

    try:
        # Use AWS minutely data for validation (lightweight endpoint)
        async with AsyncAWSClient(api_key) as client:
            # Get data from 10 minutes ago to ensure data availability
            test_time = datetime.now(UTC) - timedelta(minutes=10)
            # Test with a single station (104 = Bukgangneung)
            result = await client.get_minutely_data(tm2=test_time, stn=104)

            # Check if we got valid data back
            if result and not isinstance(result, str):
                logger.info('API key validation successful')
                return True
            else:
                logger.error('API key validation failed: %s', result)
                return False

    except Exception as e:  # noqa: BLE001
        logger.error('API key validation error: %s', e)
        return False


# ============================================================================
# ASOS (Synoptic Observations) Tools - Async
# ============================================================================


@mcp.tool()
async def get_current_weather(station_id: int = 0) -> str:
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
        async with AsyncASOSClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching weather data: {e!s}'


@mcp.tool()
async def get_hourly_weather(
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
        async with AsyncASOSClient(API_KEY) as client:
            data = await client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly weather data: {e!s}'


@mcp.tool()
async def get_daily_weather(
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
        async with AsyncASOSClient(API_KEY) as client:
            data = await client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily weather data: {e!s}'


@mcp.tool()
async def get_temperature_data(
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
        async with AsyncASOSClient(API_KEY) as client:
            # TA is the code for temperature (기온)
            data = await client.get_element_data(
                tm1=start_time, tm2=end_time, obs='TA', stn=station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching temperature data: {e!s}'


@mcp.tool()
async def get_precipitation_data(
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
        async with AsyncASOSClient(API_KEY) as client:
            # RN is the code for precipitation (강수량)
            data = await client.get_element_data(
                tm1=start_time, tm2=end_time, obs='RN', stn=station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
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


# ============================================================================
# AWS (Automated Weather Station) Tools - Async
# ============================================================================


@mcp.tool()
async def get_aws_current_weather(station_id: int = 0) -> str:
    """Get current AWS real-time weather observation data.

    AWS provides real-time weather data from automated weather stations
    for disaster prevention monitoring.

    Args:
        station_id: AWS station ID (0 for all stations, default: 0)

    Returns:
        Current AWS weather observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncAWSClient(API_KEY) as client:
            # Get current time (rounded to nearest minute)
            now = datetime.now(UTC)
            current_minute = now.replace(second=0, microsecond=0)

            data = await client.get_minutely_data(
                tm1=current_minute, tm2=current_minute, stn=station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS weather data: {e!s}'


@mcp.tool()
async def get_aws_minutely_weather(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get AWS minutely weather observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: AWS station ID (0 for all stations)

    Returns:
        Minutely AWS weather observation data for the period in JSON format

    Example:
        get_aws_minutely_weather('202501011200', '202501011300', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncAWSClient(API_KEY) as client:
            data = await client.get_minutely_data(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS minutely weather data: {e!s}'


# ============================================================================
# Climate Statistics Tools - Async
# ============================================================================


@mcp.tool()
async def get_climate_daily_normals(
    start_month: int,
    start_day: int,
    end_month: int,
    end_day: int,
    station_id: int = 0,
) -> str:
    """Get daily climate normal values (30-year averages).

    Climate normals provide long-term average values calculated over
    30-year reference periods (e.g., 1991-2020).

    Args:
        start_month: Start month (1-12)
        start_day: Start day (1-31)
        end_month: End month (1-12)
        end_day: End day (1-31)
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily climate normal values in JSON format

    Example:
        get_climate_daily_normals(1, 1, 1, 31, 108)  # January normals for Seoul
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncClimateClient(API_KEY) as client:
            data = await client.get_daily_normals(
                start_month, start_day, end_month, end_day, station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily climate normals: {e!s}'


@mcp.tool()
async def get_climate_monthly_normals(
    start_month: int,
    end_month: int,
    station_id: int = 0,
) -> str:
    """Get monthly climate normal values (30-year averages).

    Args:
        start_month: Start month (1-12)
        end_month: End month (1-12)
        station_id: Weather station ID (0 for all stations)

    Returns:
        Monthly climate normal values in JSON format

    Example:
        get_climate_monthly_normals(1, 12, 108)  # Full year normals for Seoul
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncClimateClient(API_KEY) as client:
            data = await client.get_monthly_normals(start_month, end_month, station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching monthly climate normals: {e!s}'


@mcp.tool()
async def get_climate_annual_normals(station_id: int = 0) -> str:
    """Get annual climate normal values (30-year averages).

    Args:
        station_id: Weather station ID (0 for all stations)

    Returns:
        Annual climate normal values in JSON format

    Example:
        get_climate_annual_normals(108)  # Annual normals for Seoul
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncClimateClient(API_KEY) as client:
            data = await client.get_annual_normals(station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching annual climate normals: {e!s}'


# ============================================================================
# Yellow Dust (PM10) Observation Tools - Async
# ============================================================================


@mcp.tool()
async def get_dust_current_pm10(station_id: int = 0) -> str:
    """Get current PM10 (yellow dust) observation data.

    Yellow dust observations monitor PM10 particulate matter from
    Asian dust storms and air quality conditions.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Current PM10 observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncDustClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching PM10 data: {e!s}'


@mcp.tool()
async def get_dust_hourly_pm10(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get hourly PM10 observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Hourly PM10 observation data for the period in JSON format

    Example:
        get_dust_hourly_pm10('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncDustClient(API_KEY) as client:
            data = await client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly PM10 data: {e!s}'


@mcp.tool()
async def get_dust_daily_pm10(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get daily PM10 observation data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily PM10 observation data for the period in JSON format

    Example:
        get_dust_daily_pm10('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncDustClient(API_KEY) as client:
            data = await client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily PM10 data: {e!s}'


# ============================================================================
# UV Radiation Observation Tools - Async
# ============================================================================


@mcp.tool()
async def get_uv_current_index(station_id: int = 0) -> str:
    """Get current UV radiation index observation data.

    UV radiation observations monitor ultraviolet radiation levels
    for public health protection and sun safety guidance.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Current UV index observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncUVClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_observation_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching UV index data: {e!s}'


# ============================================================================
# Snow Depth Observation Tools - Async
# ============================================================================


@mcp.tool()
async def get_snow_current_depth() -> str:
    """Get current snow depth observation data.

    Snow depth observations monitor snow accumulation for winter
    weather analysis, transportation safety, and disaster prevention.

    Returns:
        Current snow depth observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncSnowClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_snow_depth(tm=current_hour)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching snow depth data: {e!s}'


@mcp.tool()
async def get_snow_period_depth(
    start_time: str,
    end_time: str,
) -> str:
    """Get snow depth observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format

    Returns:
        Snow depth data for the period in JSON format

    Example:
        get_snow_period_depth('202501011200', '202501011800')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncSnowClient(API_KEY) as client:
            data = await client.get_snow_period(tm=end_time, tm_st=start_time)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching snow period depth data: {e!s}'


# ============================================================================
# North Korea Meteorological Observation Tools - Async
# ============================================================================


@mcp.tool()
async def get_nk_current_weather(station_id: int = 0) -> str:
    """Get current North Korea meteorological observation data.

    North Korea observations provide meteorological data from weather
    stations in North Korea for regional weather analysis and monitoring.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Current North Korea meteorological observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncNKClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching North Korea weather data: {e!s}'


@mcp.tool()
async def get_nk_hourly_weather(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get hourly North Korea meteorological observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Hourly North Korea weather data for the period in JSON format

    Example:
        get_nk_hourly_weather('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncNKClient(API_KEY) as client:
            data = await client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly North Korea weather data: {e!s}'


@mcp.tool()
async def get_nk_daily_weather(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get daily North Korea meteorological observation data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily North Korea weather data for the period in JSON format

    Example:
        get_nk_daily_weather('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncNKClient(API_KEY) as client:
            data = await client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily North Korea weather data: {e!s}'


# ============================================================================
# AWS Objective Analysis Tools - Async
# ============================================================================


@mcp.tool()
async def get_aws_oa_current(longitude: float, latitude: float) -> str:
    """Get current AWS objective analysis data for a location.

    AWS Objective Analysis provides gridded meteorological data derived
    from AWS observations through objective analysis techniques.

    Args:
        longitude: Longitude coordinate (e.g., 127.0 for Seoul)
        latitude: Latitude coordinate (e.g., 37.5 for Seoul)

    Returns:
        Current AWS objective analysis data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncAWSOAClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = await client.get_analysis_data(tm=current_hour, x=longitude, y=latitude)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS objective analysis data: {e!s}'


@mcp.tool()
async def get_aws_oa_period(
    start_time: str,
    end_time: str,
    longitude: float,
    latitude: float,
) -> str:
    """Get AWS objective analysis data for a location over a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        longitude: Longitude coordinate
        latitude: Latitude coordinate

    Returns:
        AWS objective analysis data for the period in JSON format

    Example:
        get_aws_oa_period('202501011200', '202501011800', 127.0, 37.5)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncAWSOAClient(API_KEY) as client:
            data = await client.get_analysis_period(
                tm1=start_time, tm2=end_time, x=longitude, y=latitude
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS objective analysis data: {e!s}'


# ============================================================================
# Seasonal Observation Tools - Async
# ============================================================================


@mcp.tool()
async def get_season_current_year(station_id: int = 0) -> str:
    """Get seasonal observation data for the current year.

    Seasonal observations monitor phenological events such as cherry
    blossom flowering, autumn foliage, and other seasonal indicators.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Seasonal observation data for the current year in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncSeasonClient(API_KEY) as client:
            # Get current year
            current_year = datetime.now(UTC).year

            data = await client.get_observation_data(year=current_year, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


@mcp.tool()
async def get_season_by_year(year: int, station_id: int = 0) -> str:
    """Get seasonal observation data for a specific year.

    Args:
        year: Year (e.g., 2025)
        station_id: Weather station ID (0 for all stations)

    Returns:
        Seasonal observation data for the year in JSON format

    Example:
        get_season_by_year(2025, 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncSeasonClient(API_KEY) as client:
            data = await client.get_observation_data(year=year, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


@mcp.tool()
async def get_season_period(
    start_year: int,
    end_year: int,
    station_id: int = 0,
) -> str:
    """Get seasonal observation data for a year range.

    Args:
        start_year: Start year (e.g., 2020)
        end_year: End year (e.g., 2025)
        station_id: Weather station ID (0 for all stations)

    Returns:
        Seasonal observation data for the period in JSON format

    Example:
        get_season_period(2020, 2025, 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncSeasonClient(API_KEY) as client:
            data = await client.get_observation_period(
                start_year=start_year, end_year=end_year, stn=station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


# ============================================================================
# Station Information Tools - Async
# ============================================================================


@mcp.tool()
async def get_asos_station_list(station_id: int = 0) -> str:
    """Get ASOS (synoptic) station information.

    Provides metadata about ASOS observation stations including
    location, altitude, and operational status.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        ASOS station information in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncStationClient(API_KEY) as client:
            data = await client.get_asos_stations(stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching ASOS station information: {e!s}'


@mcp.tool()
async def get_aws_station_list(station_id: int = 0) -> str:
    """Get AWS station information.

    Provides metadata about AWS observation stations including
    location, altitude, and operational status.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        AWS station information in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncStationClient(API_KEY) as client:
            data = await client.get_aws_stations(stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS station information: {e!s}'


# ============================================================================
# Weather Forecast Tools - Async
# ============================================================================


@mcp.tool()
async def get_short_term_forecast(forecast_time: str, region_id: int = 0) -> str:
    """Get short-term weather forecast (up to 3 days).

    Provides weather predictions for the next 3 days including
    temperature, precipitation probability, sky conditions, and wind.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Short-term weather forecast in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_short_term_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching short-term forecast: {e!s}'


@mcp.tool()
async def get_medium_term_forecast(forecast_time: str, region_id: int = 0) -> str:
    """Get medium-term weather forecast (3-10 days).

    Provides weather predictions for 3-10 days ahead including
    general weather trends and temperature ranges.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Medium-term weather forecast in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_medium_term_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching medium-term forecast: {e!s}'


@mcp.tool()
async def get_weekly_forecast(forecast_time: str, region_id: int = 0) -> str:
    """Get weekly weather forecast.

    Provides week-long weather predictions for planning purposes.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Weekly weather forecast in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_weekly_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching weekly forecast: {e!s}'


# ============================================================================
# Weather Warning Tools - Async
# ============================================================================


@mcp.tool()
async def get_current_weather_warnings(region_id: int = 0) -> str:
    """Get current active weather warnings and alerts.

    Provides information about active severe weather warnings including
    heavy rain, strong winds, heavy snow, and other hazards.

    Args:
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Current active weather warnings in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncWarningClient(API_KEY) as client:
            data = await client.get_current_warnings(stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching current warnings: {e!s}'


@mcp.tool()
async def get_weather_warning_history(
    start_date: str,
    end_date: str,
    region_id: int = 0,
) -> str:
    """Get weather warning history for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Weather warning history in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncWarningClient(API_KEY) as client:
            data = await client.get_warning_history(
                start_date=start_date, end_date=end_date, stn=region_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching warning history: {e!s}'


@mcp.tool()
async def get_special_weather_report(report_time: str, region_id: int = 0) -> str:
    """Get special weather report.

    Provides special weather reports for significant weather events.

    Args:
        report_time: Report time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_id: Region code (0 for all regions, default: 0)

    Returns:
        Special weather report in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncWarningClient(API_KEY) as client:
            data = await client.get_special_weather_report(tm=report_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching special weather report: {e!s}'



async def main() -> None:
    """Initialize and run the async MCP server with API key validation."""
    logger.info('Starting KMA Async MCP server...')

    # Validate API key on startup
    if not API_KEY:
        logger.warning('KMA_API_KEY environment variable not set')
        logger.warning('Server will start but API calls will fail')
    else:
        logger.info('Validating API key...')
        if await validate_api_key(API_KEY):
            logger.info('API key is valid and working')
        else:
            logger.error('API key validation failed - API calls may not work properly')
            logger.error('Please check your API key at https://apihub.kma.go.kr/')

    # Initialize and run the server
    logger.info('Server initialized successfully')
    mcp.run(transport='stdio')


if __name__ == '__main__':
    # Run the async MCP server
    import asyncio

    asyncio.run(main())
