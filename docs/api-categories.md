# API Categories

This page provides detailed information about all 21 API clients organized by category. For complete implementation status, see [API_STATUS.md](https://github.com/appleparan/kma-mcp/blob/main/API_STATUS.md).

## 1. Surface Observations (지상관측)

Ground-based meteorological observations from weather stations across Korea.

### ASOS (종관기상관측)
**Module**: `kma_mcp.surface.asos_client`

Standard synoptic observations from 96 stations.

- `get_hourly_data()` - Single hour observation
- `get_hourly_period()` - Multiple hours (max 31 days)
- `get_daily_data()` - Single day observation
- `get_daily_period()` - Multiple days
- `get_element_data()` - Specific weather element

**Data**: Temperature, precipitation, pressure, humidity, wind, solar radiation, sunshine duration

### AWS (방재기상관측)
**Module**: `kma_mcp.surface.aws_client`

Real-time disaster prevention monitoring from ~600 stations.

- `get_minutely_data()` - 1-minute resolution data
- `get_minutely_period()` - Minutely time series
- `get_hourly_data()` - Hourly observations
- `get_hourly_period()` - Hourly time series
- `get_daily_data()` - Daily summaries
- `get_daily_period()` - Daily time series

**Data**: Real-time temperature, precipitation, wind, humidity

### Additional Surface APIs

- **Climate Statistics** (`climate_client`) - 30-year climate normals (1991-2020)
- **North Korea Observations** (`nk_client`) - Cross-border weather data
- **Yellow Dust** (`dust_client`) - PM10 particulate matter monitoring
- **UV Radiation** (`uv_client`) - UV index measurements
- **Snow Depth** (`snow_client`) - Snow accumulation monitoring
- **AWS Objective Analysis** (`aws_oa_client`) - Gridded analysis data
- **Seasonal Observations** (`season_client`) - Phenological data (flowering, autumn leaves)
- **Station Information** (`station_client`) - Station metadata and locations

## 2. Marine Observations (해양관측)

Ocean weather data from buoys.

### Buoy Observations (해양기상부이)
**Module**: `kma_mcp.marine.buoy_client`

Marine meteorological data from ocean buoys.

- `get_buoy_data()` - Single time buoy observation
- `get_buoy_period()` - Time series buoy data
- `get_comprehensive_marine_data()` - Comprehensive marine observations

**Data**: Wave height, wave period, wave direction, sea temperature, wind, pressure

**Coverage**: Coastal waters and open seas around Korean Peninsula

## 3. Upper-Air Observations (고층관측)

Atmospheric vertical profiles.

### Radiosonde (고층기상관측)
**Module**: `kma_mcp.upper_air.radiosonde_client`

Upper-air soundings from radiosondes.

- `get_upper_air_data()` - Vertical profile data
- `get_stability_indices()` - Atmospheric stability indices (CAPE, CIN, K-index, etc.)
- `get_maximum_altitude_data()` - Maximum altitude observations

**Data**: Temperature, humidity, wind at various pressure levels (surface to ~30km)

**Use cases**: Weather forecasting, convection analysis, model verification

## 4. Radar (레이더)

Real-time precipitation detection and tracking.

### Weather Radar (기상레이더)
**Module**: `kma_mcp.radar.radar_client`

Precipitation radar imagery.

- `get_radar_image()` - Single radar image
- `get_radar_image_sequence()` - Radar animation sequence
- `get_radar_reflectivity()` - Reflectivity at specific location

**Data**: Reflectivity, precipitation intensity, storm movement

**Update frequency**: 10 minutes

## 5. Satellite (위성)

GEO-KOMPSAT-2A (GK2A) satellite imagery.

### GK2A Satellite (천리안위성)
**Module**: `kma_mcp.satellite.satellite_client`

Geostationary satellite observations.

- `get_satellite_file_list()` - Available satellite files
- `get_satellite_imagery()` - Satellite imagery data

**Data**:
- Level 1B: 16 spectral channels (NR016, SW038, etc.)
- Level 2: Derived products (cloud imagery, SST, etc.)
- Regions: Full Disk (FD), Korea (KO), East Asia (EA)

**Update frequency**: 10 minutes (full disk), 2 minutes (Korea)

## 6. Earthquakes (지진/화산)

Seismic activity monitoring.

### Earthquake Monitoring (지진관측)
**Module**: `kma_mcp.earthquake.earthquake_client`

Real-time earthquake information.

- `get_recent_earthquake()` - Most recent earthquake
- `get_earthquake_list()` - Earthquake list for period

**Data**: Magnitude, location (lat/lon), depth, time, intensity

**Coverage**: Korean Peninsula and surrounding regions

## 7. Typhoon (태풍)

Tropical cyclone tracking.

### Typhoon Information (태풍정보)
**Module**: `kma_mcp.typhoon.typhoon_client`

Typhoon tracking and forecasting.

- `get_current_typhoons()` - Currently active typhoons
- `get_typhoon_by_id()` - Detailed information for specific typhoon
- `get_typhoon_forecast()` - Forecast track and intensity
- `get_typhoon_history()` - Historical typhoon data by year

**Data**: Position, central pressure, maximum wind speed, forecast track, wind radii

**Coverage**: Northwest Pacific region

**Historical data**: 1951-present

## 8. Forecasts & Warnings (예특보)

Official weather forecasts and severe weather alerts.

### Weather Forecasts (기상예보)
**Module**: `kma_mcp.forecast.forecast_client`

- `get_short_term_forecast()` - 3-day detailed forecast
- `get_medium_term_forecast()` - 3-10 day outlook
- `get_weekly_forecast()` - Weekly forecast summary

**Data**: Temperature, precipitation probability, sky condition, wind

### Weather Warnings (기상특보)
**Module**: `kma_mcp.forecast.warning_client`

- `get_current_warnings()` - Currently active warnings
- `get_warning_history()` - Historical warning data
- `get_special_weather_report()` - Special weather bulletins

**Types**: Typhoon, heavy rain, heavy snow, strong wind, storm surge, etc.

## 9. Global Meteorology (세계기상)

Worldwide meteorological data via GTS.

### GTS (Global Telecommunication System)
**Module**: `kma_mcp.global_met.gts_client`

WMO worldwide meteorological data network.

- `get_synop_observations()` - Global surface observations (SYNOP)
- `get_ship_observations()` - Ship meteorological reports
- `get_buoy_observations()` - Global ocean buoy data
- `get_aircraft_reports()` - Aircraft meteorological reports (AIREP)
- `get_surface_chart()` - Surface weather analysis charts
- `get_synop_chart()` - SYNOP analysis charts

**Coverage**: Worldwide via WMO network

**Format**: BUFR and traditional formats

## 10. Aviation Meteorology (항공기상)

Aviation-specific weather data.

### AMOS (Airport Meteorological Observations)
**Module**: `kma_mcp.aviation.amos_client`

- `get_airport_observations()` - Airport/aerodrome weather (AMOS)
- `get_amdar_data()` - Aircraft meteorological data relay (AMDAR)

**Data**:
- AMOS: Airport surface weather observations
- AMDAR: Aircraft-based observations (temperature, wind, turbulence)

**Coverage**: Korean airports and commercial aircraft routes

## 11. Integrated Meteorology (융합기상)

Specialized integrated observation systems.

### Integrated Observations (통합 기상 관측)
**Module**: `kma_mcp.integrated.integrated_client`

- `get_lightning_data()` - Lightning detection network data
- `get_wind_profiler_data()` - Wind profiler vertical profiles

**Data**:
- Lightning: Location, intensity, polarity, time
- Wind Profiler: Vertical wind profiles by altitude

**Coverage**: Korean Peninsula

**Update frequency**: Real-time (lightning), 1-hour (wind profiler)

## Common Parameters

Most APIs share common parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `tm` | str/datetime | Single time point (format: YYYYMMDDHHmm or YYYYMMDD) |
| `tm1` | str/datetime | Period start time |
| `tm2` | str/datetime | Period end time |
| `stn` | int | Station ID (0 = all stations) |
| `help` | str | Help parameter (usually '0' for JSON response) |

## Response Format

All APIs return JSON data with this structure:

```json
{
  "response": {
    "header": {
      "resultCode": "00",
      "resultMsg": "NORMAL_SERVICE"
    },
    "body": {
      "dataType": "JSON",
      "items": {
        "item": [...]
      },
      "pageNo": 1,
      "numOfRows": 10,
      "totalCount": 100
    }
  }
}
```

## Korean Weather Utilities

`kma_mcp.utils.weather_codes` provides Korean language support:

```python
from kma_mcp.utils.weather_codes import (
    wind_direction_kr,      # 풍향 변환 (270 → "서풍")
    precipitation_type_kr,  # 강수형태 (0-7 → "맑음", "비", "눈" 등)
    sky_condition_kr,       # 하늘상태 (1,3,4 → "맑음", "구름많음", "흐림")
    enhance_weather_data,   # 자동으로 한글 필드 추가
    format_weather_summary  # 요약문 생성
)
```

## Next Steps

- [Getting Started](getting-started.md) - Setup and basic usage
- [API Reference](reference/) - Complete API documentation
- [GitHub](https://github.com/appleparan/kma-mcp) - Source code and examples
- [API_STATUS.md](https://github.com/appleparan/kma-mcp/blob/main/API_STATUS.md) - Detailed implementation status
