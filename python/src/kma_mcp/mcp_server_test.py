"""Test MCP server with modular tools."""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from kma_mcp.tools import forecast_tools, surface_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path(__file__).resolve().parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
logger.info('Loading environment from: %s', env_path)

# Initialize FastMCP server
mcp = FastMCP('KMA Weather Data - Test')

# Get API key and set it in tools modules
API_KEY = os.getenv('KMA_API_KEY', '')
surface_tools.set_api_key(API_KEY)
forecast_tools.set_api_key(API_KEY)

# Register surface tools
# AWS
mcp.tool(surface_tools.get_aws_current_weather)
mcp.tool(surface_tools.get_aws_minutely_weather)
# UV
mcp.tool(surface_tools.get_uv_current_index)
# Snow
mcp.tool(surface_tools.get_snow_current_depth)
mcp.tool(surface_tools.get_snow_period_depth)
# North Korea
mcp.tool(surface_tools.get_nk_current_weather)
mcp.tool(surface_tools.get_nk_hourly_weather)
mcp.tool(surface_tools.get_nk_daily_weather)
# AWS Objective Analysis
mcp.tool(surface_tools.get_aws_oa_current)
mcp.tool(surface_tools.get_aws_oa_period)
# Season
mcp.tool(surface_tools.get_season_current_year)
mcp.tool(surface_tools.get_season_by_year)
mcp.tool(surface_tools.get_season_period)
# Station Info
mcp.tool(surface_tools.get_asos_station_list)
mcp.tool(surface_tools.get_aws_station_list)

# Register forecast tools
# Forecasts
mcp.tool(forecast_tools.get_short_term_forecast)
mcp.tool(forecast_tools.get_medium_term_forecast)
mcp.tool(forecast_tools.get_weekly_forecast)
# Weather Warnings
mcp.tool(forecast_tools.get_current_weather_warnings)
mcp.tool(forecast_tools.get_weather_warning_history)
mcp.tool(forecast_tools.get_special_weather_report)

if __name__ == '__main__':
    mcp.run()
