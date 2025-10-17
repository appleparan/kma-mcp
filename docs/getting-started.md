# Getting Started

This guide will help you set up and start using kma-mcp to access Korean weather data.

## Prerequisites

- Python 3.13+
- Git
- KMA API Hub account and API key

## Installation

### 1. Install uv

First, install uv if you haven't already:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Setup Project

```bash
# Clone the repository
git clone https://github.com/appleparan/kma-mcp.git
cd kma-mcp

# Install Python 3.13
uv python install 3.13
uv python pin 3.13

# Install dependencies
uv sync

# Install with dev tools (for development)
uv sync --group dev --group docs
```

### 3. Get API Key

1. Visit [KMA API Hub](https://apihub.kma.go.kr/)
2. Create an account (requires Korean mobile phone verification)
3. Navigate to "API 신청" (API Application)
4. Request an API key for the services you need
5. Once approved, copy your API key

### 4. Configure API Key

Set your API key as an environment variable:

```bash
# Method 1: Environment variable
export KMA_API_KEY='your_key_here'

# Method 2: .env file (recommended)
echo "KMA_API_KEY=your_key_here" > .env
```

### 5. Verify Installation

Test the installation:

```bash
# Run tests
uv run pytest

# You should see: 198 passed
```

## Quick Start Examples

### Example 1: Get Current Weather

```python
from kma_mcp.surface.asos_client import ASOSClient
import os

# Get API key from environment
api_key = os.getenv('KMA_API_KEY')

# Get current weather for Seoul (station 108)
with ASOSClient(api_key) as client:
    data = client.get_hourly_data(tm='202501011200', stn=108)
    print(data)
```

### Example 2: Get Weather Period Data

```python
from kma_mcp.surface.asos_client import ASOSClient
from datetime import datetime

with ASOSClient(api_key) as client:
    # Get hourly data for last 24 hours
    data = client.get_hourly_period(
        tm1='202501010000',
        tm2='202501020000',
        stn=108  # Seoul
    )
    print(f"Retrieved {len(data)} hours of data")
```

### Example 3: Using Async Client

```python
import asyncio
from kma_mcp.surface.async_asos_client import AsyncASOSClient

async def get_weather():
    async with AsyncASOSClient(api_key) as client:
        data = await client.get_hourly_data(tm='202501011200', stn=108)
        return data

# Run async function
data = asyncio.run(get_weather())
```

### Example 4: Multiple Concurrent Requests

```python
import asyncio
from kma_mcp.surface.async_asos_client import AsyncASOSClient

async def get_multiple_stations():
    async with AsyncASOSClient(api_key) as client:
        # Get weather for multiple cities concurrently
        tasks = [
            client.get_hourly_data(tm='202501011200', stn=108),  # Seoul
            client.get_hourly_data(tm='202501011200', stn=159),  # Busan
            client.get_hourly_data(tm='202501011200', stn=184),  # Jeju
        ]
        results = await asyncio.gather(*tasks)
        return results

data = asyncio.run(get_multiple_stations())
print(f"Retrieved data for {len(data)} stations")
```

### Example 5: Using Korean Weather Utilities

```python
from kma_mcp.surface.asos_client import ASOSClient
from kma_mcp.utils.weather_codes import (
    enhance_weather_data,
    format_weather_summary
)

with ASOSClient(api_key) as client:
    data = client.get_hourly_data(tm='202501011200', stn=108)

    # Add Korean language fields
    enhanced = enhance_weather_data(data)

    # Generate human-readable summary
    summary = format_weather_summary(enhanced)
    print(summary)
    # Output: "기온 15.2°C, 날씨 맑음, 풍향 서풍, 풍속 3.2m/s"
```

## Running the MCP Server

### Start the Server

```bash
uv run python scripts/start_mcp_server.py
```

### Configure in Claude Desktop

Add to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "kma-weather": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "/path/to/kma-mcp/scripts/start_mcp_server.py"
      ],
      "env": {
        "KMA_API_KEY": "your_key_here"
      }
    }
  }
}
```

## Common Station IDs

| Station ID | Location | Korean Name |
|------------|----------|-------------|
| 108 | Seoul | 서울 |
| 112 | Incheon | 인천 |
| 133 | Daejeon | 대전 |
| 143 | Daegu | 대구 |
| 156 | Gwangju | 광주 |
| 159 | Busan | 부산 |
| 184 | Jeju | 제주 |
| 0 | All stations | 모든 지점 |

For a complete list, use:

```python
from kma_mcp.surface.station_client import StationClient

with StationClient(api_key) as client:
    stations = client.get_asos_stations()
    for station in stations:
        print(f"{station['stn_id']}: {station['stn_ko']}")
```

## Time Format Guide

### String Formats

- **Hourly data**: `YYYYMMDDHHmm` (e.g., `202501011200` = 2025-01-01 12:00)
- **Daily data**: `YYYYMMDD` (e.g., `20250101` = 2025-01-01)

### Python datetime Objects

All clients accept Python datetime objects:

```python
from datetime import datetime

# These are equivalent
data1 = client.get_hourly_data(tm='202501011200', stn=108)
data2 = client.get_hourly_data(tm=datetime(2025, 1, 1, 12, 0), stn=108)
```

## API Categories

kma-mcp provides access to 11 major categories:

1. **Surface Observations** - Ground weather stations (ASOS, AWS, etc.)
2. **Marine Observations** - Ocean buoy data
3. **Upper-Air Observations** - Atmospheric vertical profiles (radiosondes)
4. **Radar** - Precipitation detection and tracking
5. **Satellite** - GK2A satellite imagery
6. **Earthquakes** - Seismic activity monitoring
7. **Typhoon** - Tropical cyclone tracking
8. **Forecasts & Warnings** - Weather predictions and alerts
9. **Global Meteorology** - GTS worldwide data
10. **Aviation Meteorology** - Airport and aircraft weather
11. **Integrated Meteorology** - Lightning and wind profiler data

See [API Categories](api-categories.md) for detailed documentation of each category.

## Development Workflow

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check --fix .

# Type checking
uv run mypy src/

# Run pre-commit hooks
uvx pre-commit run --all-files
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=kma_mcp

# Run specific test file
uv run pytest tests/surface/test_asos_client.py

# Run verbose
uv run pytest -v
```

### Documentation

```bash
# Serve documentation locally (with auto-reload)
uv run mkdocs serve

# Build documentation
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy
```

## Configuration

### Environment Variables

- `KMA_API_KEY` - Your KMA API Hub key (required)
- `KMA_TIMEOUT` - Request timeout in seconds (default: 30.0)

### .env File Example

```bash
# .env
KMA_API_KEY=your_key_here
KMA_TIMEOUT=60.0
```

Load automatically with:

```python
from dotenv import load_dotenv
load_dotenv()
```

## Error Handling

### Common Errors

**401 Unauthorized**
```python
# Invalid API key
# Solution: Check your API key in .env file
```

**429 Too Many Requests**
```python
# Rate limit exceeded
# Solution: Wait or upgrade to premium tier
```

**404 Not Found**
```python
# Invalid endpoint or parameters
# Solution: Check station ID and time format
```

### Error Handling Example

```python
import httpx
from kma_mcp.surface.asos_client import ASOSClient

try:
    with ASOSClient(api_key) as client:
        data = client.get_hourly_data(tm='202501011200', stn=108)
except httpx.HTTPStatusError as e:
    print(f"HTTP error {e.response.status_code}: {e.response.text}")
except httpx.RequestError as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Tips

### Use Async for Multiple Requests

```python
# BAD: Sequential (slow)
with ASOSClient(api_key) as client:
    data1 = client.get_hourly_data(tm='202501011200', stn=108)
    data2 = client.get_hourly_data(tm='202501011200', stn=159)

# GOOD: Concurrent (fast)
async with AsyncASOSClient(api_key) as client:
    data1, data2 = await asyncio.gather(
        client.get_hourly_data(tm='202501011200', stn=108),
        client.get_hourly_data(tm='202501011200', stn=159)
    )
```

### Cache Frequently Accessed Data

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_station_list(api_key):
    with StationClient(api_key) as client:
        return client.get_asos_stations()
```

### Respect Rate Limits

```python
import time

# Add delay between requests if needed
for stn in station_ids:
    data = client.get_hourly_data(tm='202501011200', stn=stn)
    time.sleep(0.1)  # 100ms delay
```

## Troubleshooting

### Import Errors

```bash
# Error: No module named 'kma_mcp'
# Solution: Ensure dependencies are installed
uv sync
```

### API Key Issues

```bash
# Error: 401 Unauthorized
# Solution: Check API key is set correctly
echo $KMA_API_KEY
```

### Timeout Errors

```python
# Increase timeout for slow connections
client = ASOSClient(api_key, timeout=60.0)
```

## Next Steps

- [Overview](overview.md) - Understand the architecture and features
- [API Categories](api-categories.md) - Explore all available APIs
- [API Reference](reference/) - Detailed API documentation
- [GitHub Repository](https://github.com/appleparan/kma-mcp) - Source code and issues

## Getting Help

- **Documentation**: [https://appleparan.github.io/kma-mcp/](https://appleparan.github.io/kma-mcp/)
- **Issues**: [GitHub Issues](https://github.com/appleparan/kma-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/appleparan/kma-mcp/discussions)
- **KMA API Hub**: [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/)
