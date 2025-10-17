# kma-mcp

Model Context Protocol (MCP) server for Korea Meteorological Administration API access

## About

This package provides Python and TypeScript implementations of MCP servers for accessing the [Korea Meteorological Administration (KMA) API Hub](https://apihub.kma.go.kr/).

**All API implementations are based on the official KMA API Hub specifications and documentation available at [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/).**

The KMA API Hub provides comprehensive meteorological data including:
- Real-time weather observations (ASOS, AWS)
- Climate statistics and normals
- Weather forecasts and warnings
- Radar and satellite imagery
- Typhoon tracking
- Specialized observations (UV, dust, snow, etc.)

## Features

This project provides FastMCP servers for accessing KMA (Korea Meteorological Administration) weather APIs:

### ✅ ASOS (Automated Synoptic Observing System)
Standard meteorological observations at 96 stations nationwide:
- Temperature, Precipitation, Pressure, Humidity
- Wind direction/speed, Solar radiation, Sunshine duration, Snow depth
- Hourly and daily data

### ✅ AWS (Automated Weather Station)
Real-time disaster prevention monitoring with extensive station coverage:
- **Minutely data** for rapid monitoring
- Temperature, Precipitation, Wind, Humidity
- More observation points than ASOS
- Focused on disaster prevention and real-time alerts

### ✅ Climate Statistics (기후통계)
Long-term climate normals based on 30-year averages:
- Daily, 10-day, monthly, and annual normals
- Reference periods (e.g., 1991-2020)
- Temperature, precipitation, wind, humidity averages
- Essential for climate trend analysis

### ✅ North Korea Meteorological Observation (북한기상관측)
Regional weather data from North Korea observation stations:
- **Hourly and daily meteorological observations**
- Cross-border weather monitoring
- Regional weather analysis and forecasting
- Critical for Korean Peninsula weather patterns

### ✅ Yellow Dust Observation (황사관측)
PM10 particulate matter monitoring for air quality assessment:
- **Hourly and daily PM10 concentrations**
- Asian dust storm monitoring
- Air quality data for public health alerts
- Critical for environmental monitoring and health protection


### ✅ UV Radiation Observation (자외선관측)
Ultraviolet radiation monitoring for sun safety and health protection:
- **Hourly and daily UV index measurements**
- Public health protection guidance
- Sun safety recommendations
- Critical for outdoor activity planning and health alerts

### ✅ Snow Depth Observation (적설관측)
Snow accumulation monitoring for winter weather analysis:
- **Hourly and daily snow depth measurements**
- Winter weather analysis and transportation safety
- Disaster prevention and planning
- Critical for snow-related emergency response

### ✅ Weather Forecast and Warnings (예특보)
Comprehensive weather forecasting and severe weather alerts:
- **Short-term (3-day), medium-term (3-10 day), and weekly forecasts**
- Current active weather warnings and alerts
- Special weather reports for significant events
- Critical for disaster preparedness and planning

### ✅ Weather Radar (기상 레이더)
Real-time precipitation monitoring and storm tracking:
- **Radar imagery for precipitation patterns**
- Radar animation sequences for storm movement
- Location-specific reflectivity data
- Critical for nowcasting and severe weather monitoring

### ✅ Typhoon Information (태풍 정보)
Tropical cyclone tracking and forecasting:
- **Current active typhoon positions and intensity**
- Detailed typhoon information and forecast tracks
- Historical typhoon data for climatological analysis
- Critical for disaster preparedness and emergency response

> **Implementation Status**: 14 APIs implemented (Surface: 10, Forecast/Warning: 2, Radar: 1, Typhoon: 1). See [API_STATUS.md](API_STATUS.md) for complete list of 60+ available APIs.

## Quick Start

### Prerequisites

1. Get an API key from [KMA API Hub](https://apihub.kma.go.kr/)
   - Register an account at [https://apihub.kma.go.kr/](https://apihub.kma.go.kr/)
   - Navigate to "마이페이지" (My Page) to generate an API key
   - The API key will be used as the `authKey` parameter in all API requests
   - **Note**: All APIs in this package correspond to the services available on the KMA API Hub

2. Set up your environment:

   **Option 1: Using .env file (Recommended)**
   ```bash
   # Copy the example file
   cp .env.example .env

   # Edit .env and add your API key
   # KMA_API_KEY=your_actual_api_key_here
   ```

   **Option 2: Using environment variable**
   ```bash
   export KMA_API_KEY='your_api_key_here'
   ```

### Run the MCP Server

```bash
# Using uv
uv run python scripts/start_mcp_server.py

# Or directly
python scripts/start_mcp_server.py
```

The server will automatically load your API key from:
1. `.env` file in the project root (if exists)
2. Environment variable `KMA_API_KEY` (if set)

The API key is passed as `authKey` parameter in all API requests.

### Available Tools

The MCP server provides the following tools:

**ASOS (Synoptic Observations)**:
1. **get_current_weather**: Get current hourly weather observation data
2. **get_hourly_weather**: Get hourly weather data for a time period (max 31 days)
3. **get_daily_weather**: Get daily weather data for a date range
4. **get_temperature_data**: Get temperature observations for a specific period
5. **get_precipitation_data**: Get precipitation observations for a specific period
6. **list_station_info**: Get a list of weather station IDs and names

**AWS (Automated Weather Station)**:
7. **get_aws_current_weather**: Get current real-time AWS weather data
8. **get_aws_minutely_weather**: Get minutely AWS data for rapid monitoring
9. **get_aws_hourly_weather**: Get hourly AWS data for a time period
10. **get_aws_daily_weather**: Get daily AWS data for a date range

**Climate Statistics (기후통계)**:
11. **get_climate_daily_normals**: Get daily climate normal values (30-year averages)
12. **get_climate_monthly_normals**: Get monthly climate normal values
13. **get_climate_annual_normals**: Get annual climate normal values

**North Korea Meteorological Observation (북한기상관측)**:
14. **get_nk_current_weather**: Get current North Korea weather observation
15. **get_nk_hourly_weather**: Get hourly North Korea weather data for a time period
16. **get_nk_daily_weather**: Get daily North Korea weather data for a date range

**Yellow Dust Observation (황사관측)**:
17. **get_dust_current_pm10**: Get current PM10 (yellow dust) concentration
18. **get_dust_hourly_pm10**: Get hourly PM10 data for a time period
19. **get_dust_daily_pm10**: Get daily PM10 data for a date range


**UV Radiation Observation (자외선관측)**:
20. **get_uv_current_index**: Get current UV radiation index
21. **get_uv_hourly_index**: Get hourly UV index data for a time period
22. **get_uv_daily_index**: Get daily UV index data for a date range

**Snow Depth Observation (적설관측)**:
23. **get_snow_current_depth**: Get current snow depth measurement
24. **get_snow_hourly_depth**: Get hourly snow depth data for a time period
25. **get_snow_daily_depth**: Get daily snow depth data for a date range

**AWS Objective Analysis (AWS 객관분석)**:
26. **get_aws_oa_current**: Get current AWS gridded analysis data for a location
27. **get_aws_oa_period**: Get AWS gridded analysis data for a time period

**Seasonal Observation (계절관측)**:
28. **get_season_current_year**: Get seasonal observation data for current year
29. **get_season_by_year**: Get seasonal observation data for a specific year
30. **get_season_period**: Get seasonal observation data for a year range

**Station Information (지점정보)**:
31. **get_asos_station_list**: Get ASOS station metadata
32. **get_aws_station_list**: Get AWS station metadata

**Weather Forecast (기상예보)**:
33. **get_short_term_forecast**: Get 3-day weather forecast
34. **get_medium_term_forecast**: Get 3-10 day weather forecast
35. **get_weekly_forecast**: Get weekly weather forecast

**Weather Warnings (기상특보)**:
36. **get_current_weather_warnings**: Get current active weather warnings
37. **get_weather_warning_history**: Get historical weather warnings
38. **get_special_weather_report**: Get special weather reports

**Weather Radar (기상 레이더)**:
39. **get_radar_image**: Get weather radar image data
40. **get_radar_image_sequence**: Get radar animation sequence
41. **get_radar_reflectivity_at_location**: Get radar reflectivity for a location

**Typhoon Information (태풍 정보)**:
42. **get_current_typhoons**: Get currently active typhoons
43. **get_typhoon_details**: Get detailed information for a specific typhoon
44. **get_typhoon_forecast_track**: Get typhoon forecast track
45. **get_typhoon_history_by_year**: Get historical typhoon data for a year

### Example Usage

**ASOS Client**:
```python
from kma_mcp.surface.asos_client import ASOSClient

# Initialize client
client = ASOSClient('your_api_key')

# Get current weather for Seoul (station 108)
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get daily weather for a period

data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)
# Get temperature data
data = client.get_element_data(tm1='202501011200', tm2='202501011800', obs='TA', stn=108)
```

**AWS Client**:
```python
from kma_mcp.surface.aws_client import AWSClient

# Initialize AWS client
client = AWSClient('your_api_key')

# Get minutely data for real-time monitoring
data = client.get_minutely_data(tm='202501011200', stn=108)

# Get minutely data for a period (rapid monitoring)
data = client.get_minutely_period(tm1='202501011200', tm2='202501011300', stn=108)

# Get hourly AWS data
data = client.get_hourly_period(tm1='202501010000', tm2='202501020000', stn=108)
```

**North Korea Client**:
```python
from kma_mcp.surface.nk_client import NKClient

# Initialize North Korea client
client = NKClient('your_api_key')

# Get current hourly weather from North Korea stations
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get hourly weather for a period
data = client.get_hourly_period(tm1='202501010000', tm2='202501020000', stn=108)

# Get daily weather data
data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)
```

**Climate Client**:
```python
from kma_mcp.surface.climate_client import ClimateClient

# Initialize Climate client
client = ClimateClient('your_api_key')

# Get daily normals for January (30-year averages)
data = client.get_daily_normals(start_month=1, start_day=1, end_month=1, end_day=31, stn=108)

# Get monthly normals for the entire year
data = client.get_monthly_normals(start_month=1, end_month=12, stn=108)

# Get annual normals
data = client.get_annual_normals(stn=108)
```

**Yellow Dust Client**:
```python
from kma_mcp.surface.dust_client import DustClient

# Initialize Yellow Dust client
client = DustClient('your_api_key')

# Get current hourly PM10 data
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get hourly PM10 data for a period
data = client.get_hourly_period(tm1='202501010000', tm2='202501020000', stn=108)

# Get daily PM10 averages
data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)
```

**UV Radiation Client**:
```python
from kma_mcp.surface.uv_client import UVClient

# Initialize UV Radiation client
client = UVClient('your_api_key')

# Get current hourly UV index
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get hourly UV index for a period
data = client.get_hourly_period(tm1='202501010000', tm2='202501020000', stn=108)

# Get daily UV index averages
data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)
```

**Snow Depth Client**:
```python
from kma_mcp.surface.snow_client import SnowClient

# Initialize Snow Depth client
client = SnowClient('your_api_key')

# Get current hourly snow depth
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get hourly snow depth for a period
data = client.get_hourly_period(tm1='202501010000', tm2='202501020000', stn=108)

# Get daily snow depth data
data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)
```

**Radar Client**:
```python
from kma_mcp.radar.radar_client import RadarClient

# Initialize Radar client
client = RadarClient('your_api_key')

# Get radar image for a specific time
data = client.get_radar_image(tm='202501011200', radar_id='ALL')

# Get radar image sequence for animation
data = client.get_radar_image_sequence(tm1='202501011200', tm2='202501011300', radar_id='ALL')

# Get radar reflectivity at a specific location
data = client.get_radar_reflectivity(tm='202501011200', x=127.0, y=37.5)
```

**Typhoon Client**:
```python
from kma_mcp.typhoon.typhoon_client import TyphoonClient

# Initialize Typhoon client
client = TyphoonClient('your_api_key')

# Get currently active typhoons
data = client.get_current_typhoons()

# Get detailed information for a specific typhoon
data = client.get_typhoon_by_id(typhoon_id='2501')

# Get forecast track for a typhoon
data = client.get_typhoon_forecast(typhoon_id='2501')

# Get historical typhoon data for a year
data = client.get_typhoon_history(year=2024)
```

### Common Station IDs

- 108: Seoul (서울)
- 112: Incheon (인천)
- 133: Daejeon (대전)
- 143: Daegu (대구)
- 156: Gwangju (광주)
- 159: Busan (부산)
- 184: Jeju (제주)


## Project Organization

```plaintext
kma_mcp/
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── mkdocs.yml         <- mkdocs-material configuration file.
├── pyproject.toml     <- Project configuration file with package metadata for
│                         kma_mcp and configuration for tools like ruff
├── uv.lock            <- The lock file for reproducing the production environment, e.g.
│                         generated with `uv sync`
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
├── models             <- Trained and serialized models, model predictions, or model summaries
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
├── python/            <- Python implementation
│   ├── src/kma_mcp    <- Source code for use in this project
│   │   ├── __init__.py         <- Makes kma_mcp a Python module
│   │   └── cli.py              <- Default CLI program
│   └── tests/         <- Unit test files
└── typescript/        <- TypeScript implementation
    ├── src/           <- TypeScript source code
    │   ├── clients/   <- API client implementations
    │   └── index.ts   <- MCP server entry point
    └── tests/         <- TypeScript test files
```

## For Developers

### Whether to use `package`

This determines if the project should be treated as a Python package or a "virtual" project.

A `package` is a fully installable Python module,
while a virtual project is not installable but manages its dependencies in the virtual environment.

If you don't want to use this packaging feature,
you can set `tool.uv.package = false` in the pyproject.toml file.
This tells `uv` to handle your project as a virtual project instead of a package.

### Install Python (3.13)
```shell
uv python install 3.13
```

### Pin Python version
```shell
uv python pin 3.13
```

### Install packages with PyTorch + CUDA 12.6 (Ubuntu)
```shell
uv sync --extra cu126
```

### Install packages without locking environments
```shell
uv sync --frozen
```

### Install dev packages, too
```shell
uv sync --group dev --group docs --extra cu126
```

### Run tests
```shell
uv run pytest
```

### Linting
```shell
uv ruff check --fix .
```

### Formatting
```shell
uv ruff format
```

### Run pre-commit
* Assume that `pre-commit` installed with `uv tool install pre-commit`

```shell
uvx pre-commit run --all-files
```

### Build package
```shell
uv build
```

### Serve Document
```shell
uv run mkdocs serve
```

### Build Document
```shell
uv run mkdocs build
```

### Build Docker Image (from source)

[ref. uv docs](https://docs.astral.sh/uv/guides/integration/docker/#installing-a-project)

```shell
docker build -t TAGNAME -f Dockerfile.source
```

### Build Docker Image (from package)

[ref. uv docs](https://docs.astral.sh/uv/guides/integration/docker/#non-editable-installs)

```shell
docker build -t TAGNAME -f Dockerfile.package
```

### Run Docker Container
```shell
docker run --gpus all -p 8000:8000 my-production-app
```

### Check next version
```shell
uv run git-cliff --bumped-version
```

### Release
Execute scripts
```shell
sh scripts/release.sh
```

What `release.sh` do:

1. Set next version to `BUMPED_VERSION`: This ensures that the `git-cliff --bumped-version` command produces consistent results.

    ```shell
    BUMPED_VERSION=$(uv run git-cliff --bumped-version)
    ```

2. Generate `CHANGELOG.md` and `RELEASE.md`: The script creates or updates the changelog and release notes using the bumped version:

    ```shell
    uv run git-cliff --strip header --tag $BUMPED_VERSION -o CHANGELOG.md
    uv run git-cliff --latest --strip header --tag $BUMPED_VERSION --unreleased -o RELEASE.md
    ```

3. Commit updated `CHANGELOG.md` and `RELEASE.md` then add tags and push: It commits the updated files, creates a tag for the new version, and pushes the changes to the repository:

    ```shell
    git add CHANGELOG.md RELEASE.md
    git commit -am "docs: Add CHANGELOG.md and RELEASE.md to release $BUMPED_VERSION"
    git tag -a v$BUMPED_VERSION -m "Release $BUMPED_VERSION"
    git push origin tag $BUMPED_VERSION
    ```

4. For dry run:

    ```shell
    uv run git-cliff --latest --strip header --tag $(uv run git-cliff --bumped-version) --unreleased
    ```

## References

### KMA API Documentation
* [KMA API Hub](https://apihub.kma.go.kr/) - Official Korea Meteorological Administration API Hub
* [KMA API Hub Documentation](https://apihub.kma.go.kr/api) - API specifications and usage guides
* **All API implementations in this package are based on the official KMA API Hub specifications**

### Development Resources
* [Model Context Protocol](https://modelcontextprotocol.io/) - MCP specification
* [FastMCP Documentation](https://github.com/jlowin/fastmcp) - Python MCP framework
* [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk) - TypeScript MCP framework
* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
* [Python Packaging User Guide](https://packaging.python.org/)


** This project template is generated by [copier-modern-ml](https://github.com/appleparan/copier-modern-ml)**
