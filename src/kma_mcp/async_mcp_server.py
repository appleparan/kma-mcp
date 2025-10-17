"""Async FastMCP server for KMA Weather APIs.

This module provides an async MCP (Model Context Protocol) server that exposes
KMA weather observation data through standardized async tools.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from kma_mcp.surface.async_asos_client import AsyncASOSClient

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize FastMCP server
mcp = FastMCP('KMA ASOS Weather Data (Async)')

# Get API key from environment
API_KEY = os.getenv('KMA_API_KEY', '')


# ============================================================================
# ASOS (Synoptic Observations) Tools - Async
# ============================================================================


@mcp.tool()
async def get_current_weather_async(station_id: int = 0) -> str:
    """Get current hourly weather observation data (async).

    Args:
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Current weather observation data in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncASOSClient(API_KEY) as client:
            from datetime import UTC, datetime

            current_time = datetime.now(UTC).strftime('%Y%m%d%H00')
            data = await client.get_hourly_data(tm=current_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching current weather: {e!s}'


@mcp.tool()
async def get_hourly_weather_async(start_time: str, end_time: str, station_id: int = 0) -> str:
    """Get hourly weather data for a time period (async).

    Args:
        start_time: Start time in 'YYYYMMDDHHmm' format (e.g., '202501010000')
        end_time: End time in 'YYYYMMDDHHmm' format (max 31 days from start)
        station_id: Weather station ID (0 for all stations, default: 0)

    Returns:
        Hourly weather data for the period in JSON format
    """
    if not API_KEY:
        return 'Error: KMA_API_KEY environment variable not set'

    try:
        async with AsyncASOSClient(API_KEY) as client:
            data = await client.get_hourly_period(tm1=start_time, tm2=end_time, stn=station_id)
            return str(data)
    except Exception as e:  # noqa: BLE001
        return f'Error fetching hourly weather: {e!s}'


# Add more async tools as needed...
# For brevity, I'm showing the pattern. You can add all the other tools following the same pattern.


if __name__ == '__main__':
    # Run the async MCP server
    mcp.run()
