"""Async forecast and warning tools for MCP server.

This module contains async tool functions for weather forecasts and warnings including:
- Short-term forecasts (up to 3 days)
- Medium-term forecasts (3-10 days)
- Weekly forecasts
- Weather warnings and alerts
- Special weather reports
"""

from kma_mcp.forecast.async_forecast_client import AsyncForecastClient
from kma_mcp.forecast.async_warning_client import AsyncWarningClient

# API key will be set by the main server
API_KEY: str = ''


def set_api_key(api_key: str) -> None:
    """Set the API key for all tools in this module."""
    global API_KEY
    API_KEY = api_key


# ============================================================================
# Weather Forecast Tools
# ============================================================================


async def get_short_term_forecast(forecast_time: str, region_code: str | None = None) -> str:
    """Get short-term weather forecast (up to 3 days) by region.

    Provides weather predictions for the next 3 days including
    temperature, precipitation probability, sky conditions, and wind.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_code: Forecast region code (None for all regions)

    Returns:
        Short-term weather forecast in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_short_term_region(tmfc=forecast_time, reg=region_code)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching short-term forecast: {e!s}'


async def get_medium_term_forecast(forecast_time: str, region_code: str | None = None) -> str:
    """Get medium-term weather forecast (3-10 days) by region.

    Provides weather predictions for 3-10 days ahead including
    general weather trends and temperature ranges.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_code: Forecast region code (None for all regions)

    Returns:
        Medium-term weather forecast in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_medium_term_region(tmfc=forecast_time, reg=region_code)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching medium-term forecast: {e!s}'


async def get_short_term_overview(forecast_time: str, region_code: str | None = None) -> str:
    """Get short-term weather overview.

    Provides overview of short-term weather forecast.

    Args:
        forecast_time: Forecast time in 'YYYYMMDDHHmm' format (e.g., '202501011200')
        region_code: Forecast region code (None for all regions)

    Returns:
        Short-term weather overview in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncForecastClient(API_KEY) as client:
            data = await client.get_short_term_overview(tmfc=forecast_time, reg=region_code)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching short-term overview: {e!s}'


# ============================================================================
# Weather Warning Tools
# ============================================================================


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
