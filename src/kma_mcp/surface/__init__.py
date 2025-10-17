"""Surface observation clients for KMA API.

This package contains all surface observation API clients including:
- ASOS (Automated Synoptic Observing System)
- AWS (Automated Weather Station)
- Climate Statistics
- North Korea Meteorological Observation
- Yellow Dust (PM10) Observation
- UV Radiation Observation
- Snow Depth Observation
- AWS Objective Analysis
- Seasonal Observation
- Station Information
"""

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

__all__ = [
    'ASOSClient',
    'AWSClient',
    'AWSOAClient',
    'ClimateClient',
    'DustClient',
    'NKClient',
    'SeasonClient',
    'SnowClient',
    'StationClient',
    'UVClient',
]
