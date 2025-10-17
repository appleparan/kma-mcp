"""Tests for async API clients."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from kma_mcp.earthquake.async_earthquake_client import AsyncEarthquakeClient
from kma_mcp.marine.async_buoy_client import AsyncBuoyClient
from kma_mcp.surface.async_asos_client import AsyncASOSClient
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
