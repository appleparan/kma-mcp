"""Tests for async API clients."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from kma_mcp.earthquake.async_earthquake_client import AsyncEarthquakeClient
from kma_mcp.forecast.async_forecast_client import AsyncForecastClient
from kma_mcp.forecast.async_warning_client import AsyncWarningClient
from kma_mcp.marine.async_buoy_client import AsyncBuoyClient
from kma_mcp.radar.async_radar_client import AsyncRadarClient
from kma_mcp.satellite.async_satellite_client import AsyncSatelliteClient
from kma_mcp.surface.async_asos_client import AsyncASOSClient
from kma_mcp.surface.async_aws_client import AsyncAWSClient
from kma_mcp.surface.async_aws_oa_client import AsyncAWSOAClient
from kma_mcp.surface.async_climate_client import AsyncClimateClient
from kma_mcp.surface.async_dust_client import AsyncDustClient
from kma_mcp.surface.async_nk_client import AsyncNKClient
from kma_mcp.surface.async_season_client import AsyncSeasonClient
from kma_mcp.surface.async_snow_client import AsyncSnowClient
from kma_mcp.surface.async_station_client import AsyncStationClient
from kma_mcp.surface.async_uv_client import AsyncUVClient
from kma_mcp.typhoon.async_typhoon_client import AsyncTyphoonClient
from kma_mcp.upper_air.async_radiosonde_client import AsyncRadiosondeClient


class TestAsyncASOSClient:
    """Tests for async ASOS client."""

    @pytest.mark.asyncio
    async def test_init_and_close(self):
        """Test client initialization and cleanup."""
        client = AsyncASOSClient('test_key')
        assert client.auth_key == 'test_key'
        await client.close()

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncASOSClient('test_key') as client:
            assert client.auth_key == 'test_key'
        # Client should be closed after context

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_hourly_data(self, mock_get):
        """Test getting hourly data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'test'}
        mock_response.raise_for_status = MagicMock()

        # Create AsyncMock for get
        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncASOSClient('test_key') as client:
            result = await client.get_hourly_data(tm='202501011200', stn=108)

        assert result == {'data': 'test'}


class TestAsyncBuoyClient:
    """Tests for async Buoy client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncBuoyClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_buoy_data(self, mock_get):
        """Test getting buoy data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'buoy_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncBuoyClient('test_key') as client:
            result = await client.get_buoy_data(tm='202501011200', stn=0)

        assert result == {'data': 'buoy_test'}


class TestAsyncRadiosondeClient:
    """Tests for async Radiosonde client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncRadiosondeClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_upper_air_data(self, mock_get):
        """Test getting upper-air data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'radiosonde_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncRadiosondeClient('test_key') as client:
            result = await client.get_upper_air_data(tm='202501010000', stn=47122)

        assert result == {'data': 'radiosonde_test'}


class TestAsyncEarthquakeClient:
    """Tests for async Earthquake client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncEarthquakeClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_recent_earthquake(self, mock_get):
        """Test getting recent earthquake data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'earthquake_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncEarthquakeClient('test_key') as client:
            result = await client.get_recent_earthquake()

        assert result == {'data': 'earthquake_test'}


# ============================================================================
# Surface Observation Clients
# ============================================================================


class TestAsyncAWSClient:
    """Tests for async AWS client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncAWSClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_minutely_data(self, mock_get):
        """Test getting minutely data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'aws_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncAWSClient('test_key') as client:
            result = await client.get_minutely_data(tm2='202501011200', stn=108)

        assert result == {'data': 'aws_test'}


class TestAsyncClimateClient:
    """Tests for async Climate client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncClimateClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_daily_normals(self, mock_get):
        """Test getting daily normals."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'climate_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncClimateClient('test_key') as client:
            result = await client.get_daily_normals(1, 1, 1, 31, 108)

        assert result == {'data': 'climate_test'}


class TestAsyncDustClient:
    """Tests for async Dust client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncDustClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_hourly_data(self, mock_get):
        """Test getting hourly dust data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'dust_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncDustClient('test_key') as client:
            result = await client.get_hourly_data(tm='202501011200', stn=108)

        assert result == {'data': 'dust_test'}


class TestAsyncUVClient:
    """Tests for async UV client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncUVClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_hourly_data(self, mock_get):
        """Test getting hourly UV data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'uv_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncUVClient('test_key') as client:
            result = await client.get_observation_data(tm='202501011200', stn=108)

        assert result == {'data': 'uv_test'}


class TestAsyncSnowClient:
    """Tests for async Snow client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncSnowClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_snow_depth(self, mock_get):
        """Test getting snow depth data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'snow_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncSnowClient('test_key') as client:
            result = await client.get_snow_depth(tm='202501011200', sd_type='tot')

        assert result == {'data': 'snow_test'}


class TestAsyncNKClient:
    """Tests for async NK client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncNKClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_hourly_data(self, mock_get):
        """Test getting hourly NK data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'nk_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncNKClient('test_key') as client:
            result = await client.get_hourly_data(tm='202501011200', stn=0)

        assert result == {'data': 'nk_test'}


class TestAsyncAWSOAClient:
    """Tests for async AWS OA client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncAWSOAClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_analysis_data(self, mock_get):
        """Test getting AWS OA analysis data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'awsoa_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncAWSOAClient('test_key') as client:
            result = await client.get_analysis_data(tm='202501011200', x=127.0, y=37.5)

        assert result == {'data': 'awsoa_test'}


class TestAsyncSeasonClient:
    """Tests for async Season client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncSeasonClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_observation_data(self, mock_get):
        """Test getting seasonal observation data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'season_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncSeasonClient('test_key') as client:
            result = await client.get_observation_data(year=2025, stn=108)

        assert result == {'data': 'season_test'}


class TestAsyncStationClient:
    """Tests for async Station client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncStationClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_asos_stations(self, mock_get):
        """Test getting ASOS station information."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'station_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncStationClient('test_key') as client:
            result = await client.get_asos_stations(stn=108)

        assert result == {'data': 'station_test'}


# ============================================================================
# Forecast and Warning Clients
# ============================================================================


class TestAsyncForecastClient:
    """Tests for async Forecast client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncForecastClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_short_term_region(self, mock_get):
        """Test getting short-term forecast by region."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'forecast_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncForecastClient('test_key') as client:
            result = await client.get_short_term_region(tmfc='0')

        assert result == {'data': 'forecast_test'}

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_village_forecast(self, mock_get):
        """Test getting village forecast (OpenAPI)."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'village_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncForecastClient('test_key') as client:
            result = await client.get_village_forecast(
                page_no=1, num_of_rows=10, data_type='JSON',
                base_date='20210628', base_time='0500', nx=60, ny=127
            )

        assert result == {'data': 'village_test'}

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_medium_term_region(self, mock_get):
        """Test getting medium-term forecast region."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'medium_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncForecastClient('test_key') as client:
            result = await client.get_medium_term_region(tmfc='0')

        assert result == {'data': 'medium_test'}

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_warning_region(self, mock_get):
        """Test getting weather warning region."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'warning_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncForecastClient('test_key') as client:
            result = await client.get_warning_region(wrn='W')

        assert result == {'data': 'warning_test'}


class TestAsyncWarningClient:
    """Tests for async Warning client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncWarningClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_current_warnings(self, mock_get):
        """Test getting current weather warnings."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'warning_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncWarningClient('test_key') as client:
            result = await client.get_current_warnings(stn=0)

        assert result == {'data': 'warning_test'}


# ============================================================================
# Radar, Satellite, and Typhoon Clients
# ============================================================================


class TestAsyncRadarClient:
    """Tests for async Radar client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncRadarClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_radar_image(self, mock_get):
        """Test getting radar image."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'radar_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncRadarClient('test_key') as client:
            result = await client.get_radar_image(tm='202501011200', radar_id='ALL')

        assert result == {'data': 'radar_test'}


class TestAsyncSatelliteClient:
    """Tests for async Satellite client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncSatelliteClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_satellite_file_list(self, mock_get):
        """Test getting satellite file list."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'satellite_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncSatelliteClient('test_key') as client:
            result = await client.get_satellite_file_list(sat='GK2A', vars='L1B', area='FD')

        assert result == {'data': 'satellite_test'}


class TestAsyncTyphoonClient:
    """Tests for async Typhoon client."""

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager."""
        async with AsyncTyphoonClient('test_key') as client:
            assert client.auth_key == 'test_key'

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_get_current_typhoons(self, mock_get):
        """Test getting current typhoons."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'typhoon_test'}
        mock_response.raise_for_status = MagicMock()

        async_mock = AsyncMock(return_value=mock_response)
        mock_get.side_effect = async_mock

        async with AsyncTyphoonClient('test_key') as client:
            result = await client.get_current_typhoons()

        assert result == {'data': 'typhoon_test'}
