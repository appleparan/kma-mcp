# TypeScript Implementation

The TypeScript implementation of kma-mcp provides a type-safe MCP (Model Context Protocol) server for accessing the [Korea Meteorological Administration (KMA) API Hub](https://apihub.kma.go.kr/).

**All API implementations are based on the official [KMA API Hub](https://apihub.kma.go.kr/) specifications.** This ensures full compatibility with the official KMA weather services and provides access to the same comprehensive meteorological data available through the KMA API Hub portal at [https://apihub.kma.go.kr/api](https://apihub.kma.go.kr/api).

## Features

- **Type-Safe API Clients**: Full TypeScript support with strict typing
- **21 API Clients**: Complete coverage of all KMA API categories
- **Date Flexibility**: Support for both `Date` objects and string-formatted dates
- **Error Handling**: Comprehensive error handling with custom `KMAAPIError` class
- **MCP Integration**: Built with `@modelcontextprotocol/sdk`
- **Testing**: Comprehensive test suite with 53+ tests

## Installation

```bash
# Using npm
npm install @appleparan/kma-mcp-server

# Using bun
bun add @appleparan/kma-mcp-server
```

## Quick Start

First, obtain an API key from the [KMA API Hub](https://apihub.kma.go.kr/):
1. Visit [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/)
2. Create an account and navigate to "마이페이지" (My Page)
3. Generate an API key for the weather services

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: 'YOUR_KMA_API_KEY'  // API key from KMA API Hub
});

// Get hourly observation data
const data = await client.getHourlyData('202501011200', 108);
console.log(data);
```

## API Categories

### Surface Observations
- **ASOS**: Automated Synoptic Observing System (지상 관측)
- **AWS**: Automatic Weather Station (방재 기상 관측)
- **AWS OA**: Objective Analysis (방재 기상 관측 객관분석)
- **Dust**: PM10 Observations (황사/연무)
- **UV**: UV Index (자외선지수)
- **Snow**: Snow Depth (적설)
- **Climate**: Climate Normals (기후평년값)
- **NK**: North Korea Observations (북한 지상관측)
- **Season**: Phenological Observations (계절관측)
- **Station**: Station Information (관측지점정보)

### Aviation & Marine
- **AMOS**: Aviation Meteorology (항공 기상 관측)
- **Buoy**: Buoy Observations (해양 부이 관측)

### Disaster Monitoring
- **Earthquake**: Seismic Observations (지진 관측)
- **Typhoon**: Tropical Cyclone Data (태풍 정보)

### Forecasts & Warnings
- **Forecast**: Weather Forecasts (예보)
- **Warning**: Weather Warnings (특보)

### Remote Sensing
- **Radar**: Radar Imagery (레이더 영상)
- **Satellite**: Satellite Imagery (위성 영상)
- **Integrated**: Lightning & Wind Profiler (낙뢰, 윈드프로파일러)

### Upper Air
- **Radiosonde**: Upper Air Soundings (고층 기상 관측)

### Global Data
- **GTS**: Global Telecommunication System (전지구 기상통신망)

## Architecture

All API clients extend the `BaseKMAClient` abstract class, which provides:

- HTTP client configuration with axios
- Request/response handling
- Error management
- Date formatting utilities

```typescript
export abstract class BaseKMAClient {
  protected client: AxiosInstance;
  protected authKey: string;

  protected async makeRequest<T>(
    endpoint: string,
    params: Record<string, unknown>
  ): Promise<T[]>;

  protected formatDateTime(date: Date, includeTime?: boolean): string;
}
```

## Error Handling

The library provides a custom `KMAAPIError` class for handling API errors:

```typescript
try {
  const data = await client.getHourlyData('202501011200', 108);
} catch (error) {
  if (error instanceof KMAAPIError) {
    console.error(`API Error [${error.resultCode}]: ${error.message}`);
  }
}
```

## API Reference

For detailed API documentation, see:

- [TypeScript API Reference](reference-ts/README.md) - Complete TypeScript API documentation
- [Python API Reference](reference/) - Python implementation reference

## Development

### Building

```bash
# TypeScript compilation
bun run build:tsc

# Bundle for distribution
bun run build
```

### Testing

```bash
# Run all tests
bun test

# Run with coverage
bun test --coverage
```

### Code Quality

```bash
# Run linter
bun run lint

# Fix linting issues
bun run lint:fix

# Format code
bun run format

# Check formatting
bun run format:check
```

## Examples

### Getting Hourly ASOS Data

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

// Using string date
const data1 = await client.getHourlyData('202501011200', 108);

// Using Date object
const date = new Date('2025-01-01T12:00:00');
const data2 = await client.getHourlyData(date, 108);
```

### Getting Daily AWS Data

```typescript
import { AWSClient } from '@appleparan/kma-mcp-server';

const client = new AWSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get daily data for a specific date
const data = await client.getDailyData('20250101', 108);
```

### Getting Period Data

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get hourly data for a date range
const data = await client.getHourlyPeriod(
  '202501010000',
  '202501312300',
  108
);
```

### Typhoon Information

```typescript
import { TyphoonClient } from '@appleparan/kma-mcp-server';

const client = new TyphoonClient({
  authKey: process.env.KMA_API_KEY!
});

// Get current typhoons
const current = await client.getCurrentTyphoons('202501');

// Get specific typhoon details
const typhoon = await client.getTyphoonById('202501', 'T2501');
```

## Contributing

Contributions are welcome! Please see the main [repository](https://github.com/appleparan/kma-mcp) for contribution guidelines.

## License

MIT
