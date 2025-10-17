#!/usr/bin/env python3
"""Start the KMA ASOS MCP server.

This script starts the FastMCP server that provides KMA ASOS weather data
through the Model Context Protocol.

Setup:
    1. Copy .env.example to .env in the project root
    2. Edit .env and set your KMA_API_KEY
    3. Run this script

Or set environment variable directly:
    export KMA_API_KEY='your_api_key_here'

The API key is automatically passed as 'authKey' parameter in all API requests.
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from kma_mcp.mcp_server import API_KEY, mcp  # noqa: E402


def main() -> None:
    """Start the MCP server."""
    print('Starting KMA ASOS MCP Server...')
    print('-' * 50)

    # Check if API key is loaded
    if not API_KEY:
        print('WARNING: KMA_API_KEY is not set!')
        print('Please set KMA_API_KEY in .env file or as environment variable.')
        print('See README.md for setup instructions.')
        print('-' * 50)
    else:
        print(f'API Key loaded: {API_KEY[:10]}...')
        print('API key will be passed as authKey parameter in requests.')
        print('-' * 50)

    print('Press Ctrl+C to stop the server.')
    print('-' * 50)

    # Run the server
    mcp.run()


if __name__ == '__main__':
    main()
