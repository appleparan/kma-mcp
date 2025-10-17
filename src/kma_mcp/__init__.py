"""kma-mcp package.

MCP server for Korea Meteorological Administration API access
"""

from importlib.metadata import PackageNotFoundError, version

from kma_mcp.app import create_app

try:
    __version__ = version('kma_mcp')
except PackageNotFoundError:
    __version__ = 'unknown'

__author__ = """Jongsu Liam Kim"""
__email__ = 'jongsukim8@gmail.com'

__all__ = ['create_app']
