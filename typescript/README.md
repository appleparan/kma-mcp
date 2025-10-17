# KMA MCP Server (TypeScript)

TypeScript implementation of Model Context Protocol (MCP) server for Korea Meteorological Administration API.

## Features

* 🌦️ **ASOS Weather Data** - Access real-time and historical Korean weather observations
* ⚡ **TypeScript Implementation** - Full type safety with TypeScript SDK
* 🔧 **MCP Compatible** - Works with Claude Desktop and other MCP clients
* 📊 **Multiple Data Types** - Temperature, precipitation, wind, humidity, pressure, and more

## Prerequisites

* Node.js >= 18.0.0
* KMA API Key from [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/)

## Installation

```bash
cd typescript
bun install
bun run build:tsc  # or bun run build for bun's bundler
```

## Configuration

Set your KMA API key:

```bash
export KMA_API_KEY='your_key_here'
```

Or create a `.env` file:

```
KMA_API_KEY=your_key_here
```

## Usage

### Run Standalone

```bash
# With bun (recommended)
bun run src/index.ts

# Or compiled version
bun run build:tsc
bun run start
```

### Use with Claude Desktop

Add to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "kma-weather-ts": {
      "command": "bun",
      "args": [
        "run",
        "/path/to/kma-mcp/typescript/src/index.ts"
      ],
      "env": {
        "KMA_API_KEY": "your_key_here"
      }
    }
  }
}
```

## Available Tools

### get_current_weather

Get current hourly weather data from ASOS station.

**Parameters:**
* `tm` (string, required): Time in YYYYMMDDHHmm format (e.g., "202501011200")
* `stn` (number, optional): Station ID (default: 108 for Seoul, 0 for all)

**Example:**
```typescript
{
  "tm": "202501011200",
  "stn": 108
}
```

### get_hourly_weather

Get hourly weather data for a time period.

**Parameters:**
* `tm1` (string, required): Start time in YYYYMMDDHHmm format
* `tm2` (string, required): End time in YYYYMMDDHHmm format
* `stn` (number, optional): Station ID (default: 108)

**Example:**
```typescript
{
  "tm1": "202501010000",
  "tm2": "202501020000",
  "stn": 108
}
```

### get_daily_weather

Get daily weather data from ASOS station.

**Parameters:**
* `tm` (string, required): Date in YYYYMMDD format (e.g., "20250101")
* `stn` (number, optional): Station ID (default: 108)

**Example:**
```typescript
{
  "tm": "20250101",
  "stn": 108
}
```

### get_temperature_data

Get temperature data for a specific time period.

**Parameters:**
* `tm1` (string, required): Start time in YYYYMMDDHHmm format
* `tm2` (string, required): End time in YYYYMMDDHHmm format
* `stn` (number, required): Station ID

**Example:**
```typescript
{
  "tm1": "202501010000",
  "tm2": "202501020000",
  "stn": 108
}
```

## Common Station IDs

| ID | Location | Korean |
|----|----------|--------|
| 108 | Seoul | 서울 |
| 112 | Incheon | 인천 |
| 133 | Daejeon | 대전 |
| 143 | Daegu | 대구 |
| 156 | Gwangju | 광주 |
| 159 | Busan | 부산 |
| 184 | Jeju | 제주 |
| 0 | All stations | 전체 |

## Development

```bash
# Install dependencies
bun install

# Build (TypeScript compiler)
bun run build:tsc

# Build (Bun bundler)
bun run build

# Watch mode (hot reload)
bun run dev

# Lint
bun run lint

# Format
bun run format

# Test
bun test
```

## Project Structure

```
typescript/
├── src/
│   ├── clients/
│   │   ├── base.ts       # Base KMA API client
│   │   └── asos.ts       # ASOS client implementation
│   └── index.ts          # MCP server entry point
├── dist/                 # Compiled output
├── package.json
├── tsconfig.json
└── README.md
```

## API Response Structure

All tools return JSON data with Korean weather observations:

```typescript
[
  {
    "tm": "202501011200",     // Observation time
    "stnId": "108",            // Station ID
    "stnNm": "서울",           // Station name
    "ta": 15.2,                // Temperature (°C)
    "rn": 0.0,                 // Precipitation (mm)
    "ws": 3.2,                 // Wind speed (m/s)
    "wd": 270,                 // Wind direction (degrees)
    "hm": 65,                  // Humidity (%)
    "pa": 1013.5,              // Pressure (hPa)
    // ... more fields
  }
]
```

## Error Handling

The server returns error messages in the content when API calls fail:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Error: HTTP 401: Unauthorized"
    }
  ],
  "isError": true
}
```

## License

MIT License - See [LICENSE](../LICENSE) file for details.

## Related

* **Python Version**: [../README.md](../README.md)
* **KMA API Hub**: [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/)
* **MCP SDK**: [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
