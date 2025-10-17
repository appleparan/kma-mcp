# kma-mcp

MCP server for Korea Meteorological Administration API access

## Features

### ASOS (Automated Synoptic Observing System) MCP Server

This project provides a FastMCP server for accessing KMA's ASOS (종관기상관측) surface weather observation data. The ASOS system collects atmospheric data at standardized times across all observation stations, measuring:

- Temperature (기온)
- Precipitation (강수량)
- Pressure (기압)
- Humidity (습도)
- Wind direction and speed (풍향, 풍속)
- Solar radiation (일사)
- Sunshine duration (일조)
- Snow depth (적설)

## Quick Start

### Prerequisites

1. Get an API key from [KMA API Hub](https://apihub.kma.go.kr/)
   - Register an account on the KMA API Hub
   - Request an API key from your account page
   - The API key will be used as the `authKey` parameter in API requests

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

1. **get_current_weather**: Get current hourly weather observation data
2. **get_hourly_weather**: Get hourly weather data for a time period (max 31 days)
3. **get_daily_weather**: Get daily weather data for a date range
4. **get_temperature_data**: Get temperature observations for a specific period
5. **get_precipitation_data**: Get precipitation observations for a specific period
6. **list_station_info**: Get a list of weather station IDs and names

### Example Usage

```python
from kma_mcp.asos_client import ASOSClient

# Initialize client
client = ASOSClient('your_api_key')

# Get current weather for Seoul (station 108)
data = client.get_hourly_data(tm='202501011200', stn=108)

# Get daily weather for a period
data = client.get_daily_period(tm1='20250101', tm2='20250131', stn=108)

# Get temperature data
data = client.get_element_data(tm1='202501011200', tm2='202501011800', obs='TA', stn=108)
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
├── tests              <- Unit test files.
└── src/kma_mcp   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes kma_mcp a Python module
    │
    └── cli.py                  <- Default CLI program
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
* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
* [Python Packaging User Guide](https://packaging.python.org/)


** This project template is generated by [copier-modern-ml](https://github.com/appleparan/copier-modern-ml)**
