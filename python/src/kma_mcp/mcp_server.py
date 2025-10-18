"""FastMCP server for KMA Weather APIs.

This module provides an MCP (Model Context Protocol) server that exposes
KMA weather observation data through standardized tools, including:
- ASOS (Automated Synoptic Observing System)
- AWS (Automated Weather Station)
"""

import logging
import os
from datetime import UTC, datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from kma_mcp.earthquake.earthquake_client import EarthquakeClient
from kma_mcp.forecast.forecast_client import ForecastClient
from kma_mcp.forecast.warning_client import WarningClient
from kma_mcp.marine.buoy_client import BuoyClient
from kma_mcp.radar.radar_client import RadarClient
from kma_mcp.satellite.satellite_client import SatelliteClient
from kma_mcp.surface.asos_client import ASOSClient
from kma_mcp.surface.aws_client import AWSClient
from kma_mcp.surface.aws_oa_client import AWSOAClient
from kma_mcp.surface.climate_client import ClimateClient
from kma_mcp.surface.dust_client import DustClient
from kma_mcp.surface.nk_client import NKClient
from kma_mcp.surface.season_client import SeasonClient
from kma_mcp.surface.snow_client import SnowClient
from kma_mcp.surface.station_client import StationClient
from kma_mcp.surface.uv_client import UVClient
from kma_mcp.typhoon.typhoon_client import TyphoonClient
from kma_mcp.upper_air.radiosonde_client import RadiosondeClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
# Look for .env in project root (parent of parent of this file)
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize FastMCP server
mcp = FastMCP('KMA ASOS Weather Data')

# Get API key from environment (from .env file or environment variable)
API_KEY = os.getenv('KMA_API_KEY', '')


def validate_api_key(api_key: str) -> bool:
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
        with AWSClient(api_key) as client:
            # Get data from 10 minutes ago to ensure data availability
            test_time = datetime.now(UTC) - timedelta(minutes=10)
            # Test with a single station (104 = Bukgangneung)
            result = client.get_minutely_data(tm=test_time, stn=104)

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
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
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
    except Exception as e:  # noqa: BLE001
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
    except Exception as e:  # noqa: BLE001
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
    except Exception as e:  # noqa: BLE001
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
# AWS (Automated Weather Station) Tools
# ============================================================================


@mcp.tool()
def get_aws_current_weather(station_id: int = 0) -> str:
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
        with AWSClient(API_KEY) as client:
            # Get current time (rounded to nearest minute)
            now = datetime.now(UTC)
            current_minute = now.replace(second=0, microsecond=0)

            data = client.get_minutely_data(tm=current_minute, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS weather data: {e!s}'


@mcp.tool()
def get_aws_minutely_weather(
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
        with AWSClient(API_KEY) as client:
            data = client.get_minutely_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS minutely weather data: {e!s}'


@mcp.tool()
def get_aws_hourly_weather(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get AWS hourly weather observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: AWS station ID (0 for all stations)

    Returns:
        Hourly AWS weather observation data for the period in JSON format

    Example:
        get_aws_hourly_weather('202501011200', '202501020000', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with AWSClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS hourly weather data: {e!s}'


@mcp.tool()
def get_aws_daily_weather(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get AWS daily weather observation data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: AWS station ID (0 for all stations)

    Returns:
        Daily AWS weather observation data for the period in JSON format

    Example:
        get_aws_daily_weather('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with AWSClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS daily weather data: {e!s}'


# ============================================================================
# Climate Statistics Tools
# ============================================================================


@mcp.tool()
def get_climate_daily_normals(
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
        with ClimateClient(API_KEY) as client:
            data = client.get_daily_normals(start_month, start_day, end_month, end_day, station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily climate normals: {e!s}'


@mcp.tool()
def get_climate_monthly_normals(
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
        with ClimateClient(API_KEY) as client:
            data = client.get_monthly_normals(start_month, end_month, station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching monthly climate normals: {e!s}'


@mcp.tool()
def get_climate_annual_normals(station_id: int = 0) -> str:
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
        with ClimateClient(API_KEY) as client:
            data = client.get_annual_normals(station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching annual climate normals: {e!s}'


# ============================================================================
# Yellow Dust (PM10) Observation Tools
# ============================================================================


@mcp.tool()
def get_dust_current_pm10(station_id: int = 0) -> str:
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
        with DustClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching PM10 data: {e!s}'


@mcp.tool()
def get_dust_hourly_pm10(
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
        with DustClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly PM10 data: {e!s}'


@mcp.tool()
def get_dust_daily_pm10(
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
        with DustClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily PM10 data: {e!s}'


# ============================================================================
# UV Radiation Observation Tools
# ============================================================================


@mcp.tool()
def get_uv_current_index(station_id: int = 0) -> str:
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
        with UVClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching UV index data: {e!s}'


@mcp.tool()
def get_uv_hourly_index(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get hourly UV radiation index data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Hourly UV index data for the period in JSON format

    Example:
        get_uv_hourly_index('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with UVClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly UV index data: {e!s}'


@mcp.tool()
def get_uv_daily_index(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get daily UV radiation index data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily UV index data for the period in JSON format

    Example:
        get_uv_daily_index('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with UVClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily UV index data: {e!s}'


# ============================================================================
# Snow Depth Observation Tools
# ============================================================================


@mcp.tool()
def get_snow_current_depth(station_id: int = 0) -> str:
    """Get current snow depth observation data.

    Snow depth observations monitor snow accumulation for winter
    weather analysis, transportation safety, and disaster prevention.

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Current snow depth observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with SnowClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching snow depth data: {e!s}'


@mcp.tool()
def get_snow_hourly_depth(
    start_time: str,
    end_time: str,
    station_id: int = 0,
) -> str:
    """Get hourly snow depth observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Hourly snow depth data for the period in JSON format

    Example:
        get_snow_hourly_depth('202501011200', '202501011800', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with SnowClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly snow depth data: {e!s}'


@mcp.tool()
def get_snow_daily_depth(
    start_date: str,
    end_date: str,
    station_id: int = 0,
) -> str:
    """Get daily snow depth observation data for a date range.

    Args:
        start_date: Start date in 'YYYYMMDD' format (e.g., '20250101')
        end_date: End date in 'YYYYMMDD' format
        station_id: Weather station ID (0 for all stations)

    Returns:
        Daily snow depth data for the period in JSON format

    Example:
        get_snow_daily_depth('20250101', '20250131', 108)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with SnowClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily snow depth data: {e!s}'


# ============================================================================
# North Korea Meteorological Observation Tools
# ============================================================================


@mcp.tool()
def get_nk_current_weather(station_id: int = 0) -> str:
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
        with NKClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_hourly_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching North Korea weather data: {e!s}'


@mcp.tool()
def get_nk_hourly_weather(
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
        with NKClient(API_KEY) as client:
            data = client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly North Korea weather data: {e!s}'


@mcp.tool()
def get_nk_daily_weather(
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
        with NKClient(API_KEY) as client:
            data = client.get_daily_period(tm1=start_date, tm2=end_date, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching daily North Korea weather data: {e!s}'


# ============================================================================
# AWS Objective Analysis Tools
# ============================================================================


@mcp.tool()
def get_aws_oa_current(longitude: float, latitude: float) -> str:
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
        with AWSOAClient(API_KEY) as client:
            # Get current time (rounded to nearest hour)
            now = datetime.now(UTC)
            current_hour = now.replace(minute=0, second=0, microsecond=0)

            data = client.get_analysis_data(tm=current_hour, x=longitude, y=latitude)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS objective analysis data: {e!s}'


@mcp.tool()
def get_aws_oa_period(
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
        with AWSOAClient(API_KEY) as client:
            data = client.get_analysis_period(tm1=start_time, tm2=end_time, x=longitude, y=latitude)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS objective analysis data: {e!s}'


# ============================================================================
# Seasonal Observation Tools
# ============================================================================


@mcp.tool()
def get_season_current_year(station_id: int = 0) -> str:
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
        with SeasonClient(API_KEY) as client:
            # Get current year
            current_year = datetime.now(UTC).year

            data = client.get_observation_data(year=current_year, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


@mcp.tool()
def get_season_by_year(year: int, station_id: int = 0) -> str:
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
        with SeasonClient(API_KEY) as client:
            data = client.get_observation_data(year=year, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


@mcp.tool()
def get_season_period(
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
        with SeasonClient(API_KEY) as client:
            data = client.get_observation_period(
                start_year=start_year, end_year=end_year, stn=station_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching seasonal observation data: {e!s}'


# ============================================================================
# Station Information Tools
# ============================================================================


@mcp.tool()
def get_asos_station_list(station_id: int = 0) -> str:
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
        with StationClient(API_KEY) as client:
            data = client.get_asos_stations(stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching ASOS station information: {e!s}'


@mcp.tool()
def get_aws_station_list(station_id: int = 0) -> str:
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
        with StationClient(API_KEY) as client:
            data = client.get_aws_stations(stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS station information: {e!s}'


# ============================================================================
# Weather Forecast Tools
# ============================================================================


@mcp.tool()
def get_short_term_forecast(forecast_time: str, region_id: int = 0) -> str:
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
        with ForecastClient(API_KEY) as client:
            data = client.get_short_term_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching short-term forecast: {e!s}'


@mcp.tool()
def get_medium_term_forecast(forecast_time: str, region_id: int = 0) -> str:
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
        with ForecastClient(API_KEY) as client:
            data = client.get_medium_term_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching medium-term forecast: {e!s}'


@mcp.tool()
def get_weekly_forecast(forecast_time: str, region_id: int = 0) -> str:
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
        with ForecastClient(API_KEY) as client:
            data = client.get_weekly_forecast(tm_fc=forecast_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching weekly forecast: {e!s}'


# ============================================================================
# Weather Warning Tools
# ============================================================================


@mcp.tool()
def get_current_weather_warnings(region_id: int = 0) -> str:
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
        with WarningClient(API_KEY) as client:
            data = client.get_current_warnings(stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching current warnings: {e!s}'


@mcp.tool()
def get_weather_warning_history(
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
        with WarningClient(API_KEY) as client:
            data = client.get_warning_history(
                start_date=start_date, end_date=end_date, stn=region_id
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching warning history: {e!s}'


@mcp.tool()
def get_special_weather_report(report_time: str, region_id: int = 0) -> str:
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
        with WarningClient(API_KEY) as client:
            data = client.get_special_weather_report(tm=report_time, stn=region_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching special weather report: {e!s}'


# ============================================================================
# Weather Radar Tools
# ============================================================================


@mcp.tool()
def get_radar_image(observation_time: str, radar_id: str = 'ALL') -> str:
    """Get weather radar image data.

    Provides weather radar image data showing precipitation intensity
    and distribution for monitoring storms and rainfall.

    Args:
        observation_time: Observation time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        radar_id: Radar station ID (default: 'ALL' for composite image)
                 Common radar IDs:
                 - 'ALL': Composite of all radars
                 - 'KSN': Gangneung
                 - 'KWK': Gwangdeoksan
                 - 'PSN': Baengnyeongdo

    Returns:
        Weather radar image data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with RadarClient(API_KEY) as client:
            data = client.get_radar_image(tm=observation_time, radar_id=radar_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching radar image data: {e!s}'


@mcp.tool()
def get_radar_image_sequence(
    start_time: str,
    end_time: str,
    radar_id: str = 'ALL',
) -> str:
    """Get weather radar image sequence for animation.

    Provides a sequence of radar images over a time period for creating
    animated displays of precipitation movement.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        radar_id: Radar station ID (default: 'ALL' for composite)

    Returns:
        Sequence of radar images in JSON format

    Example:
        get_radar_image_sequence('202501011200', '202501011300', 'ALL')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with RadarClient(API_KEY) as client:
            data = client.get_radar_image_sequence(tm1=start_time, tm2=end_time, radar_id=radar_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching radar image sequence: {e!s}'


@mcp.tool()
def get_radar_reflectivity_at_location(
    observation_time: str,
    longitude: float,
    latitude: float,
) -> str:
    """Get radar reflectivity data for a specific location.

    Provides radar reflectivity measurements at a specific geographic
    location for precise precipitation intensity estimates.

    Args:
        observation_time: Observation time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        longitude: Longitude coordinate (e.g., 127.0 for Seoul)
        latitude: Latitude coordinate (e.g., 37.5 for Seoul)

    Returns:
        Radar reflectivity data in JSON format

    Example:
        get_radar_reflectivity_at_location('202501011200', 127.0, 37.5)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with RadarClient(API_KEY) as client:
            data = client.get_radar_reflectivity(tm=observation_time, x=longitude, y=latitude)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching radar reflectivity data: {e!s}'


# ============================================================================
# Typhoon Information Tools
# ============================================================================


@mcp.tool()
def get_current_typhoons() -> str:
    """Get information on currently active typhoons.

    Provides real-time information about active tropical cyclones including
    position, intensity, movement, and current status.

    Returns:
        Current active typhoon information in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with TyphoonClient(API_KEY) as client:
            data = client.get_current_typhoons()
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching current typhoon data: {e!s}'


@mcp.tool()
def get_typhoon_details(typhoon_id: str) -> str:
    """Get detailed information for a specific typhoon.

    Provides comprehensive data about a specific typhoon including
    position history, intensity, size, and movement patterns.

    Args:
        typhoon_id: Typhoon identification number (e.g., '2501' for first typhoon of 2025)

    Returns:
        Detailed typhoon information in JSON format

    Example:
        get_typhoon_details('2501')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with TyphoonClient(API_KEY) as client:
            data = client.get_typhoon_by_id(typhoon_id=typhoon_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching typhoon details: {e!s}'


@mcp.tool()
def get_typhoon_forecast_track(typhoon_id: str) -> str:
    """Get forecast track for a specific typhoon.

    Provides predicted future path and intensity of a typhoon for
    disaster preparedness and planning.

    Args:
        typhoon_id: Typhoon identification number (e.g., '2501')

    Returns:
        Typhoon forecast track data in JSON format

    Example:
        get_typhoon_forecast_track('2501')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with TyphoonClient(API_KEY) as client:
            data = client.get_typhoon_forecast(typhoon_id=typhoon_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching typhoon forecast: {e!s}'


@mcp.tool()
def get_typhoon_history_by_year(year: int) -> str:
    """Get typhoon history for a specific year.

    Provides historical data on all typhoons that occurred during
    a specific year for climatological analysis.

    Args:
        year: Year in YYYY format (e.g., 2024)

    Returns:
        Typhoon history data for the year in JSON format

    Example:
        get_typhoon_history_by_year(2024)
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with TyphoonClient(API_KEY) as client:
            data = client.get_typhoon_history(year=year)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching typhoon history: {e!s}'


# ============================================================================
# Marine Observation (Buoy) Tools
# ============================================================================


@mcp.tool()
def get_marine_buoy_data(observation_time: str, station_id: int = 0) -> str:
    """Get marine buoy observation data.

    Provides marine meteorological data from buoys including wave height,
    water temperature, wind, and atmospheric conditions.

    Args:
        observation_time: Observation time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        station_id: Buoy station ID (0 for all stations, default: 0)

    Returns:
        Marine buoy observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with BuoyClient(API_KEY) as client:
            data = client.get_buoy_data(tm=observation_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching marine buoy data: {e!s}'


@mcp.tool()
def get_marine_buoy_period(start_time: str, end_time: str, station_id: int = 0) -> str:
    """Get marine buoy observation data for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        end_time: End time in 'YYYYMMDDHHmm' format
        station_id: Buoy station ID (0 for all stations, default: 0)

    Returns:
        Marine buoy observation data for the period in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with BuoyClient(API_KEY) as client:
            data = client.get_buoy_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching marine buoy data: {e!s}'


# ============================================================================
# Upper-Air Observations (Radiosonde) Tools
# ============================================================================


@mcp.tool()
def get_upper_air_data(
    observation_time: str, station_id: int = 0, pressure_level: float | None = None
) -> str:
    """Get upper-air radiosonde observation data.

    Provides atmospheric profile data including temperature, humidity,
    and wind at various altitude levels.

    Args:
        observation_time: UTC observation time in 'YYYYMMDDHHmm' format
        station_id: Station ID (0 for all stations, default: 0)
        pressure_level: Pressure level in hPa (optional, e.g., 850, 500, 250)

    Returns:
        Upper-air observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with RadiosondeClient(API_KEY) as client:
            data = client.get_upper_air_data(tm=observation_time, stn=station_id, pa=pressure_level)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching upper-air data: {e!s}'


@mcp.tool()
def get_atmospheric_stability_indices(start_time: str, end_time: str, station_id: int = 0) -> str:
    """Get atmospheric stability indices for convective forecasting.

    Provides stability indices including CAPE, K-index, lifted index,
    and cloud layer information for severe weather analysis.

    Args:
        start_time: Start UTC time in 'YYYYMMDDHHmm' format
        end_time: End UTC time in 'YYYYMMDDHHmm' format
        station_id: Station ID (0 for all stations, default: 0)

    Returns:
        Atmospheric stability indices in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with RadiosondeClient(API_KEY) as client:
            data = client.get_stability_indices(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching stability indices: {e!s}'


# ============================================================================
# Earthquake Monitoring Tools
# ============================================================================


@mcp.tool()
def get_recent_earthquake_info() -> str:
    """Get the most recent earthquake information.

    Provides information on the most recent earthquake or earthquakes
    within the past 10 days.

    Returns:
        Recent earthquake data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with EarthquakeClient(API_KEY) as client:
            data = client.get_recent_earthquake()
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching recent earthquake data: {e!s}'


@mcp.tool()
def get_earthquake_list(start_time: str, end_time: str) -> str:
    """Get earthquake list for a time period.

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501010000')
        end_time: End time in 'YYYYMMDDHHmm' format

    Returns:
        List of earthquakes during the period in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with EarthquakeClient(API_KEY) as client:
            data = client.get_earthquake_list(tm1=start_time, tm2=end_time)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching earthquake list: {e!s}'


# ============================================================================
# Satellite Imagery Tools
# ============================================================================


@mcp.tool()
def get_satellite_file_list(
    satellite: str = 'GK2A',
    variables: str = 'L1B',
    area: str = 'FD',
    file_format: str = 'NetCDF',
    time_filter: str | None = None,
) -> str:
    """Get list of available GK2A satellite files.

    Provides a list of available satellite imagery files from the
    GEO-KOMPSAT-2A satellite.

    Args:
        satellite: Satellite identifier (default: 'GK2A')
        variables: Product type (default: 'L1B')
                  Options: L1B, L2, etc.
        area: Region code (default: 'FD' for Full Disk)
             Options: FD, KO (Korea), EA (East Asia), etc.
        file_format: File format (default: 'NetCDF')
        time_filter: Time filter in 'YYYYMMDDHHmm' format (optional)

    Returns:
        List of available satellite files in JSON format

    Example:
        get_satellite_file_list('GK2A', 'L1B', 'KO')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with SatelliteClient(API_KEY) as client:
            data = client.get_satellite_file_list(
                sat=satellite, vars=variables, area=area, fmt=file_format, tm=time_filter
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching satellite file list: {e!s}'


@mcp.tool()
def get_satellite_imagery(
    level: str,
    product: str,
    area: str,
    observation_time: str,
) -> str:
    """Get GK2A satellite imagery data.

    Provides satellite imagery from the GEO-KOMPSAT-2A satellite including
    various spectral channels and derived products.

    Args:
        level: Data level ('l1b' or 'l2')
        product: Product type/channel
                For L1B: NR016, SW038, etc. (16 channels)
                For L2: CI (Cloud Imagery), SST, etc.
        area: Area code (FD, KO, EA, ELA, TP)
        observation_time: Time in 'YYYYMMDDHHmm' format (e.g., '202501011200')

    Returns:
        Satellite imagery data in JSON format

    Example:
        get_satellite_imagery('l1b', 'NR016', 'KO', '202501011200')
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        with SatelliteClient(API_KEY) as client:
            data = client.get_satellite_imagery(
                level=level, product=product, area=area, tm=observation_time
            )
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching satellite imagery: {e!s}'

def main() -> None:
    """Initialize and run the MCP server with API key validation."""
    logger.info('Starting KMA MCP server...')

    # Validate API key on startup
    if not API_KEY:
        logger.warning('KMA_API_KEY environment variable not set')
        logger.warning('Server will start but API calls will fail')
    else:
        logger.info('Validating API key...')
        if validate_api_key(API_KEY):
            logger.info('API key is valid and working')
        else:
            logger.error('API key validation failed - API calls may not work properly')
            logger.error('Please check your API key at https://apihub.kma.go.kr/')

    # Initialize and run the server
    logger.info('Server initialized successfully')
    mcp.run(transport='stdio')

if __name__ == '__main__':
    # Run the MCP server
    main()
