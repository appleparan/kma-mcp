# kma-mcp

**Model Context Protocol (MCP) server for Korea Meteorological Administration API access**

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is kma-mcp?

kma-mcp is a comprehensive MCP (Model Context Protocol) server implementation that provides programmatic access to the [Korea Meteorological Administration (KMA) API Hub](https://apihub.kma.go.kr/). It enables developers and researchers to easily access real-time and historical Korean weather data through simple, consistent Python and TypeScript interfaces.

**All API implementations are based on the official [KMA API Hub](https://apihub.kma.go.kr/) specifications and documentation.** This ensures compatibility with the official KMA services and provides access to the same comprehensive meteorological data available through the KMA API Hub portal.

## Key Features

### 🌦️ Comprehensive Weather Data Access

* **21 API clients** covering surface observations, marine data, upper-air measurements, radar, satellite imagery, forecasts, warnings, typhoons, earthquakes, aviation weather, and global meteorological data
* **42 total clients** (sync + async versions) for flexible integration
* **198 comprehensive tests** ensuring reliability

### ⚡ Dual Client Support

* **Synchronous clients** for simple, straightforward operations
* **Asynchronous clients** for high-performance concurrent requests
* Context manager support for automatic resource cleanup

### 🌏 Korean Weather Specialization

* Korean weather code utilities (wind direction, precipitation types, sky conditions)
* Automatic enhancement of weather data with Korean-language fields
* Human-readable Korean weather summaries

### 📊 Implementation Status

**Coverage**: 85% of public KMA API Hub categories (11/13)

**Implemented Categories**:

* ✅ Surface Observations (지상관측) - 10 APIs
* ✅ Marine Observations (해양관측) - 1 API
* ✅ Upper-Air Observations (고층관측) - 1 API
* ✅ Radar (레이더) - 1 API
* ✅ Satellite (위성) - 1 API
* ✅ Earthquakes (지진/화산) - 1 API
* ✅ Typhoon (태풍) - 1 API
* ✅ Forecasts & Warnings (예특보) - 2 APIs
* ✅ Global Meteorology (세계기상) - 1 API
* ✅ Aviation Meteorology (항공기상) - 1 API
* ✅ Integrated Meteorology (융합기상) - 1 API

**Not Implemented** (no public endpoints):

* ❌ Numerical Models (수치모델)
* ❌ Industry-Specific APIs (산업특화)

## Quick Start

### Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repository
git clone https://github.com/appleparan/kma-mcp.git
cd kma-mcp

# Install dependencies
uv sync
```

### Get API Key

1. Visit the [KMA API Hub](https://apihub.kma.go.kr/) - the official source for all Korean meteorological data
2. Create an account and navigate to "마이페이지" (My Page)
3. Generate an API key from the API management section
4. Set your API key:

```bash
export KMA_API_KEY='your_key_here'
# Or create a .env file with:
# KMA_API_KEY=your_key_here
```

**Note**: The API key from KMA API Hub provides access to all weather data services. All APIs in this package correspond directly to the services available on the [KMA API Hub portal](https://apihub.kma.go.kr/api).

### Basic Usage

```python
from kma_mcp.surface.asos_client import ASOSClient

# Get current weather for Seoul (station 108)
with ASOSClient('your_api_key') as client:
    data = client.get_hourly_data(tm='202501011200', stn=108)
    print(data)
```

### Run MCP Server

```bash
uv run python scripts/start_mcp_server.py
```

## Project Structure

```
kma-mcp/
├── src/kma_mcp/
│   ├── surface/          # Surface observation clients (10 APIs)
│   ├── marine/           # Marine observation clients (1 API)
│   ├── upper_air/        # Upper-air observation clients (1 API)
│   ├── radar/            # Radar clients (1 API)
│   ├── satellite/        # Satellite clients (1 API)
│   ├── earthquake/       # Earthquake clients (1 API)
│   ├── typhoon/          # Typhoon clients (1 API)
│   ├── forecast/         # Forecast clients (2 APIs)
│   ├── global_met/       # Global meteorology clients (1 API)
│   ├── aviation/         # Aviation meteorology clients (1 API)
│   ├── integrated/       # Integrated meteorology clients (1 API)
│   ├── utils/            # Utility modules
│   └── mcp_server.py     # Main MCP server
├── tests/                # Comprehensive test suite (198 tests)
├── docs/                 # Documentation (MkDocs)
├── scripts/              # Helper scripts
├── API_STATUS.md         # Detailed API implementation status
├── llms.txt              # LLM-friendly project documentation
└── README.md             # Main documentation
```

## Use Cases

* **Weather Research**: Access historical and real-time Korean weather data
* **Climate Analysis**: Long-term climate statistics and trends
* **Disaster Monitoring**: Real-time tracking of typhoons, earthquakes, severe weather
* **Aviation Safety**: Airport weather observations and aircraft meteorological data
* **Marine Operations**: Ocean buoy data for maritime safety
* **Air Quality**: PM10 yellow dust monitoring
* **Public Health**: UV index tracking
* **Agricultural Planning**: Seasonal observations and phenological data

## Resources

### Official KMA Resources
* **KMA API Hub**: [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/) - Official API portal and documentation
* **KMA API Documentation**: [https://apihub.kma.go.kr/api](https://apihub.kma.go.kr/api) - Complete API specifications
* **Note**: All APIs in this package are implemented according to official KMA API Hub specifications

### This Project
* **Documentation**: [https://appleparan.github.io/kma-mcp/](https://appleparan.github.io/kma-mcp/)
* **GitHub**: [https://github.com/appleparan/kma-mcp](https://github.com/appleparan/kma-mcp)

### MCP Framework
* **Model Context Protocol**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
* **FastMCP (Python)**: [https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)
* **TypeScript SDK**: [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

## License

MIT License - See [LICENSE](https://github.com/appleparan/kma-mcp/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](https://github.com/appleparan/kma-mcp/blob/main/CONTRIBUTING.md) for guidelines.

---

**Built with**: Python 3.13+, FastMCP, httpx, uv
