"""Surface observation tools for MCP server.

This module contains tool functions for surface weather observations including:
- AWS (Automated Weather Station)
- ASOS (Automated Synoptic Observing System)
- UV radiation
- Snow depth
- North Korea observations
- AWS Open API
- Season observations
"""

from datetime import UTC, datetime

from kma_mcp.surface.aws_client import AWSClient
from kma_mcp.surface.aws_oa_client import AWSOAClient
from kma_mcp.surface.nk_client import NKClient
from kma_mcp.surface.season_client import SeasonClient
from kma_mcp.surface.snow_client import SnowClient
from kma_mcp.surface.station_client import StationClient
from kma_mcp.surface.uv_client import UVClient

# API key will be set by the main server
API_KEY: str = ''


def set_api_key(api_key: str) -> None:
    """Set the API key for all tools in this module."""
    global API_KEY
    API_KEY = api_key


# ============================================================================
# AWS (Automated Weather Station) Tools
# ============================================================================


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

            data = client.get_minutely_data(tm1=current_minute, tm2=current_minute, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS weather data: {e!s}'


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
            data = client.get_minutely_data(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching AWS minutely weather data: {e!s}'


# ============================================================================
# UV Radiation Tools
# ============================================================================


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

            data = client.get_observation_data(tm=current_hour, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching UV index data: {e!s}'


# ============================================================================
# Snow Depth Tools
# ============================================================================


def get_snow_current_depth() -> str:
    """Get current snow depth observation data.

    Snow depth observations monitor snow accumulation for winter
    weather analysis, transportation safety, and disaster prevention.

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

            data = client.get_snow_depth(tm=current_hour)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching snow depth data: {e!s}'


def get_snow_period_depth(
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
        with SnowClient(API_KEY) as client:
            data = client.get_snow_period(tm=end_time, tm_st=start_time)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching snow period depth data: {e!s}'


# ============================================================================
# North Korea Meteorological Observation Tools
# ============================================================================


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
