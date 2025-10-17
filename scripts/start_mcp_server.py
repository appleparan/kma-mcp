#!/usr/bin/env python3
"""Start the KMA ASOS MCP server.

This script starts the FastMCP server that provides KMA ASOS weather data
through the Model Context Protocol.

Before running, set the KMA_API_KEY environment variable:
    export KMA_API_KEY='your_api_key_here'

Or create a .env file in the project root with:
    KMA_API_KEY=your_api_key_here
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from kma_mcp.mcp_server import mcp  # noqa: E402


def main() -> None:
    """Start the MCP server."""
    print('Starting KMA ASOS MCP Server...')
    print('Make sure KMA_API_KEY environment variable is set.')
    print('Press Ctrl+C to stop the server.')
    print('-' * 50)

    # Run the server
    mcp.run()


if __name__ == '__main__':
    main()
