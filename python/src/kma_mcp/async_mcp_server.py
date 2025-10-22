"""Async FastMCP server for KMA Weather APIs.

This module provides an async MCP (Model Context Protocol) server that exposes
KMA weather observation data through standardized async tools, including:
- Surface observations (ASOS, AWS, Climate, Dust, UV, Snow, etc.)
- Weather forecasts and warnings
"""

import logging
import os
from datetime import UTC, datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from kma_mcp.surface.async_aws_client import AsyncAWSClient
from kma_mcp.tools import async_forecast_tools, async_surface_tools

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
mcp = FastMCP('KMA Weather Data (Async)')

# Get API key from environment (from .env file or environment variable)
API_KEY = os.getenv('KMA_API_KEY', '')

# Set API key in modular tools
async_surface_tools.set_api_key(API_KEY)
async_forecast_tools.set_api_key(API_KEY)


# Register surface tools
# AWS
mcp.tool(async_surface_tools.get_aws_current_weather)
mcp.tool(async_surface_tools.get_aws_minutely_weather)
# UV
mcp.tool(async_surface_tools.get_uv_current_index)
# Snow
mcp.tool(async_surface_tools.get_snow_current_depth)
mcp.tool(async_surface_tools.get_snow_period_depth)
# North Korea
mcp.tool(async_surface_tools.get_nk_current_weather)
mcp.tool(async_surface_tools.get_nk_hourly_weather)
mcp.tool(async_surface_tools.get_nk_daily_weather)
# AWS Objective Analysis
mcp.tool(async_surface_tools.get_aws_oa_current)
mcp.tool(async_surface_tools.get_aws_oa_period)
# Season
mcp.tool(async_surface_tools.get_season_current_year)
mcp.tool(async_surface_tools.get_season_by_year)
mcp.tool(async_surface_tools.get_season_period)
# Station Info
mcp.tool(async_surface_tools.get_asos_station_list)
mcp.tool(async_surface_tools.get_aws_station_list)

# Register forecast tools
# Forecasts
mcp.tool(async_forecast_tools.get_short_term_forecast)
mcp.tool(async_forecast_tools.get_short_term_overview)
mcp.tool(async_forecast_tools.get_medium_term_forecast)
# Weather Warnings
mcp.tool(async_forecast_tools.get_current_weather_warnings)
mcp.tool(async_forecast_tools.get_weather_warning_history)
mcp.tool(async_forecast_tools.get_special_weather_report)


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
