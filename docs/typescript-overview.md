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

## Detailed Examples

### Surface Observations

#### ASOS (Automated Synoptic Observing System)

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get hourly data with string format
const hourly = await client.getHourlyData('202501011200', 108);
console.log(`Temperature: ${hourly[0].ta}°C`);

// Get hourly data with Date object
const date = new Date('2025-01-01T12:00:00');
const data = await client.getHourlyData(date, 108);

// Get hourly period data (up to 31 days)
const period = await client.getHourlyPeriod(
  '202501010000',
  '202501312300',
  108  // Seoul station
);
console.log(`Retrieved ${period.length} hourly records`);

// Get daily data
const daily = await client.getDailyData('20250101', 108);

// Get daily period data
const dailyPeriod = await client.getDailyPeriod(
  '20250101',
  '20250131',
  108
);

// Get specific element data (e.g., temperature only)
const temperature = await client.getElementData(
  '202501010000',
  '202501012300',
  'TA',  // Temperature element code
  108
);
```

#### AWS (Automatic Weather Station)

```typescript
import { AWSClient } from '@appleparan/kma-mcp-server';

const client = new AWSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get minutely data for real-time monitoring
const minutely = await client.getMinutelyData('202501011200', 108);
console.log(`Wind speed: ${minutely[0].ws}m/s`);

// Get minutely period data
const minutelyPeriod = await client.getMinutelyPeriod(
  '202501011200',
  '202501011300',  // 1 hour range
  108
);

// Get hourly AWS data
const hourly = await client.getHourlyData('202501011200', 108);

// Get hourly period
const hourlyPeriod = await client.getHourlyPeriod(
  '202501010000',
  '202501020000',
  108
);

// Get daily data
const daily = await client.getDailyData('20250101', 108);

// Get daily period
const dailyPeriod = await client.getDailyPeriod(
  '20250101',
  '20250131',
  108
);
```

#### Climate Normals

```typescript
import { ClimateClient } from '@appleparan/kma-mcp-server';

const client = new ClimateClient({
  authKey: process.env.KMA_API_KEY!
});

// Get daily normals for a month
const dailyNormals = await client.getDailyNormals(
  1,   // start month
  1,   // start day
  1,   // end month
  31,  // end day
  108  // Seoul
);

// Get ten-day normals
const tenDayNormals = await client.getTenDayNormals(
  1,   // start month
  1,   // start ten-day period (1, 2, or 3)
  12,  // end month
  3,   // end ten-day period
  108
);

// Get monthly normals
const monthlyNormals = await client.getMonthlyNormals(
  1,   // start month
  12,  // end month
  108
);

// Get annual normals
const annualNormals = await client.getAnnualNormals(108);
```

### Specialized Observations

#### Yellow Dust (PM10) Monitoring

```typescript
import { DustClient } from '@appleparan/kma-mcp-server';

const client = new DustClient({
  authKey: process.env.KMA_API_KEY!
});

// Get hourly PM10 data
const hourly = await client.getHourlyPM10Data('202501011200', 108);
console.log(`PM10: ${hourly[0].pm10}μg/m³`);

// Get hourly period
const period = await client.getHourlyPM10Period(
  '202501010000',
  '202501020000',
  108
);

// Get daily average PM10
const daily = await client.getDailyPM10Data('20250101', 108);

// Get daily period
const dailyPeriod = await client.getDailyPM10Period(
  '20250101',
  '20250131',
  108
);
```

#### UV Index

```typescript
import { UVClient } from '@appleparan/kma-mcp-server';

const client = new UVClient({
  authKey: process.env.KMA_API_KEY!
});

// Get hourly UV index
const hourly = await client.getHourlyUVIndex('202501011200', 108);
console.log(`UV Index: ${hourly[0].uv}`);

// Get hourly period
const period = await client.getHourlyUVPeriod(
  '202501010000',
  '202501020000',
  108
);

// Get daily average UV index
const daily = await client.getDailyUVIndex('20250101', 108);

// Get daily period
const dailyPeriod = await client.getDailyUVPeriod(
  '20250101',
  '20250131',
  108
);
```

#### Snow Depth

```typescript
import { SnowClient } from '@appleparan/kma-mcp-server';

const client = new SnowClient({
  authKey: process.env.KMA_API_KEY!
});

// Get hourly snow depth
const hourly = await client.getHourlySnowDepth('202501011200', 108);
console.log(`Snow depth: ${hourly[0].sndp}cm`);

// Get hourly period
const period = await client.getHourlySnowPeriod(
  '202501010000',
  '202501020000',
  108
);

// Get daily snow depth
const daily = await client.getDailySnowDepth('20250101', 108);

// Get daily period
const dailyPeriod = await client.getDailySnowPeriod(
  '20250101',
  '20250131',
  108
);
```

### Marine and Upper Air

#### Buoy Observations

```typescript
import { BuoyClient } from '@appleparan/kma-mcp-server';

const client = new BuoyClient({
  authKey: process.env.KMA_API_KEY!
});

// Get buoy data
const data = await client.getBuoyData('202501011200', 22101);  // Buoy ID

// Get buoy period data
const period = await client.getBuoyPeriod(
  '202501010000',
  '202501020000',
  22101
);

// Get comprehensive marine data
const marine = await client.getComprehensiveMarineData(
  '202501011200',
  22101
);
```

#### Radiosonde (Upper Air)

```typescript
import { RadiosondeClient } from '@appleparan/kma-mcp-server';

const client = new RadiosondeClient({
  authKey: process.env.KMA_API_KEY!
});

// Get upper air sounding
const sounding = await client.getUpperAirSounding('202501010000', 47138);

// Get stability indices
const indices = await client.getStabilityIndices('202501010000', 47138);

// Get maximum altitude data
const maxAlt = await client.getMaxAltitudeData('202501010000', 47138);
```

### Disaster Monitoring

#### Earthquake Data

```typescript
import { EarthquakeClient } from '@appleparan/kma-mcp-server';

const client = new EarthquakeClient({
  authKey: process.env.KMA_API_KEY!
});

// Get recent earthquake (within 30 days)
const recent = await client.getRecentEarthquake();

// Get earthquake list for a period
const list = await client.getEarthquakeList(
  '202501010000',
  '202501312359'
);

// Filter significant earthquakes
const significant = list.filter(eq => eq.mag >= 3.0);
```

#### Typhoon Tracking

```typescript
import { TyphoonClient } from '@appleparan/kma-mcp-server';

const client = new TyphoonClient({
  authKey: process.env.KMA_API_KEY!
});

// Get current active typhoons
const current = await client.getCurrentTyphoons('202501');

if (current.length > 0) {
  console.log(`Active typhoons: ${current.length}`);

  // Get detailed info for first typhoon
  const typhoonId = current[0].typ_id;
  const details = await client.getTyphoonById('202501', typhoonId);

  // Get forecast track
  const forecast = await client.getTyphoonForecast('202501', typhoonId);

  console.log(`Typhoon ${details[0].typ_nm} forecast positions: ${forecast.length}`);
}

// Get historical typhoon data for a year
const history = await client.getTyphoonHistory(2024);
```

### Forecasts and Warnings

#### Weather Forecasts

```typescript
import { ForecastClient } from '@appleparan/kma-mcp-server';

const client = new ForecastClient({
  authKey: process.env.KMA_API_KEY!
});

// Get short-term forecast (up to 3 days)
const shortTerm = await client.getShortTermForecast('11B00000');  // Region code

// Get medium-term forecast (3-10 days)
const mediumTerm = await client.getMediumTermForecast('11B00000');

// Get weekly forecast
const weekly = await client.getWeeklyForecast();
```

#### Weather Warnings

```typescript
import { WarningClient } from '@appleparan/kma-mcp-server';

const client = new WarningClient({
  authKey: process.env.KMA_API_KEY!
});

// Get current active warnings
const current = await client.getCurrentWarnings();

if (current.length > 0) {
  console.log('Active weather warnings:');
  current.forEach(warning => {
    console.log(`- ${warning.wrn_nm}: ${warning.rgn_nm}`);
  });
}

// Get warning history
const history = await client.getWarningHistory(
  '202501010000',
  '202501312359'
);

// Get special weather reports
const special = await client.getSpecialReport('202501');
```

### Remote Sensing

#### Weather Radar

```typescript
import { RadarClient } from '@appleparan/kma-mcp-server';

const client = new RadarClient({
  authKey: process.env.KMA_API_KEY!
});

// Get radar image
const image = await client.getRadarImage('202501011200', 'KWK');  // Radar ID

// Get radar image sequence for animation
const sequence = await client.getRadarImageSequence(
  '202501011200',
  '202501011300',
  'ALL'  // All radars
);

// Get reflectivity at specific location
const reflectivity = await client.getRadarReflectivity(
  '202501011200',
  127.0,  // Longitude
  37.5    // Latitude
);
```

#### Satellite Imagery

```typescript
import { SatelliteClient } from '@appleparan/kma-mcp-server';

const client = new SatelliteClient({
  authKey: process.env.KMA_API_KEY!
});

// Get satellite file list
const fileList = await client.getSatelliteFileList(
  '202501011200',
  'IR1'  // Channel
);

// Get satellite imagery
const imagery = await client.getSatelliteImagery(
  '202501011200',
  'IR1',
  'FD'  // Full Disk
);
```

### Global and Aviation

#### GTS (Global Telecommunication System)

```typescript
import { GTSClient } from '@appleparan/kma-mcp-server';

const client = new GTSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get SYNOP observations
const synop = await client.getSynopObservations('202501011200');

// Get ship observations
const ship = await client.getShipObservations('202501011200');

// Get buoy GTS data
const buoy = await client.getBuoyObservations('202501011200');

// Get aircraft observations
const aircraft = await client.getAircraftObservations('202501011200');

// Get surface analysis chart
const surfaceChart = await client.getSurfaceAnalysisChart('202501011200');

// Get upper air chart
const upperAirChart = await client.getUpperAirChart('202501011200', '500');
```

#### Aviation Meteorology

```typescript
import { AMOSClient } from '@appleparan/kma-mcp-server';

const client = new AMOSClient({
  authKey: process.env.KMA_API_KEY!
});

// Get airport weather observations
const airport = await client.getAirportObservations('202501011200', 'RKSI');  // Incheon

// Get AMDAR (Aircraft Meteorological Data Relay) data
const amdar = await client.getAMDARData('202501011200');
```

### Integrated Meteorology

```typescript
import { IntegratedClient } from '@appleparan/kma-mcp-server';

const client = new IntegratedClient({
  authKey: process.env.KMA_API_KEY!
});

// Get lightning data
const lightning = await client.getLightningData('202501011200');

// Get wind profiler data
const windProfiler = await client.getWindProfilerData('202501011200', 108);
```

## Advanced Usage

### Date Handling

All clients accept both string and Date object formats:

```typescript
// String format
const data1 = await client.getHourlyData('202501011200', 108);

// Date object
const date = new Date('2025-01-01T12:00:00');
const data2 = await client.getHourlyData(date, 108);

// Current time
const now = new Date();
const data3 = await client.getHourlyData(now, 108);
```

### Error Handling Patterns

```typescript
import { ASOSClient, KMAAPIError } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

try {
  const data = await client.getHourlyData('202501011200', 108);
  console.log('Data retrieved successfully');
} catch (error) {
  if (error instanceof KMAAPIError) {
    console.error(`KMA API Error: ${error.message}`);
    console.error(`Result Code: ${error.resultCode}`);
    console.error(`Status Code: ${error.statusCode}`);
  } else if (error instanceof Error) {
    console.error(`Generic Error: ${error.message}`);
  }
}
```

### Configuration Options

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!,
  baseURL: 'https://apihub.kma.go.kr/api/typ01/url',  // Optional
  timeout: 30000  // 30 seconds, optional
});
```

### Working with Multiple Stations

```typescript
import { ASOSClient } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

const stations = [108, 112, 133, 143, 156, 159, 184];  // Major cities
const time = '202501011200';

// Sequential requests
const results = [];
for (const stn of stations) {
  const data = await client.getHourlyData(time, stn);
  results.push(data[0]);
}

// Or use Promise.all for concurrent requests
const promises = stations.map(stn =>
  client.getHourlyData(time, stn)
);
const allData = await Promise.all(promises);
```

### Type Safety

TypeScript provides full type information:

```typescript
import { ASOSClient, type ASOSObservation } from '@appleparan/kma-mcp-server';

const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!
});

// Type is inferred as ASOSObservation[]
const data = await client.getHourlyData('202501011200', 108);

// Access with full autocomplete
const observation: ASOSObservation = data[0];
console.log(`Temperature: ${observation.ta}°C`);
console.log(`Humidity: ${observation.hm}%`);
console.log(`Wind Speed: ${observation.ws}m/s`);
```

## Time Format Reference

| Data Type | Format | Example | Description |
|-----------|--------|---------|-------------|
| Hourly | YYYYMMDDHHmm | 202501011200 | Year-Month-Day-Hour-Minute |
| Daily | YYYYMMDD | 20250101 | Year-Month-Day |
| Year-Month | YYYYMM | 202501 | Year-Month |
| Year | YYYY | 2025 | Year |

## Performance Considerations

### Rate Limiting

The KMA API Hub has rate limits. Consider:

- Implementing request throttling
- Caching frequently accessed data
- Using period requests instead of multiple single requests

```typescript
// Good: Single period request
const period = await client.getHourlyPeriod(
  '202501010000',
  '202501312300',
  108
);

// Avoid: Multiple single requests
// Don't do this for large date ranges
for (let day = 1; day <= 31; day++) {
  const data = await client.getHourlyData(`202501${day}1200`, 108);
}
```

### Timeout Configuration

For slow networks or large data requests:

```typescript
const client = new ASOSClient({
  authKey: process.env.KMA_API_KEY!,
  timeout: 60000  // 60 seconds
});
```

## Contributing

Contributions are welcome! Please see the main [repository](https://github.com/appleparan/kma-mcp) for contribution guidelines.

## License

MIT
