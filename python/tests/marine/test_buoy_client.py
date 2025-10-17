"""Tests for Marine Buoy API client."""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.marine.buoy_client import BuoyClient


class TestBuoyClientInit:
    """Tests for BuoyClient initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = BuoyClient('test_key')
        assert client.auth_key == 'test_key'
        assert client._client.timeout.read == 30.0
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with BuoyClient('test_key') as client:
            assert client.auth_key == 'test_key'
        # Client should be closed after context


class TestBuoyClientRequests:
    """Tests for Buoy API requests."""

    @patch('httpx.Client.get')
    def test_get_buoy_data_with_string(self, mock_get):
        """Test getting buoy data with string time parameter."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with BuoyClient('test_key') as client:
            result = client.get_buoy_data(tm='202501011200', stn=0)

        assert result == {'data': 'test'}
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert 'kma_buoy.php' in call_args[0][0]
        assert call_args[1]['params']['tm'] == '202501011200'
        assert call_args[1]['params']['stn'] == '0'

    @patch('httpx.Client.get')
    def test_get_buoy_data_with_datetime(self, mock_get):
        """Test getting buoy data with datetime parameter."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        test_dt = datetime(2025, 1, 1, 12, 0, tzinfo=UTC)

        with BuoyClient('test_key') as client:
            result = client.get_buoy_data(tm=test_dt, stn=0)

        assert result == {'data': 'test'}
        call_args = mock_get.call_args
        assert call_args[1]['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_get_buoy_period(self, mock_get):
        """Test getting buoy data for a time period."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'period_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with BuoyClient('test_key') as client:
            result = client.get_buoy_period(tm1='202501010000', tm2='202501020000', stn=0)

        assert result == {'data': 'period_test'}
        call_args = mock_get.call_args
        assert 'kma_buoy2.php' in call_args[0][0]
        assert call_args[1]['params']['tm1'] == '202501010000'
        assert call_args[1]['params']['tm2'] == '202501020000'

    @patch('httpx.Client.get')
    def test_get_comprehensive_marine_data(self, mock_get):
        """Test getting comprehensive marine observation data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'comprehensive'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with BuoyClient('test_key') as client:
            result = client.get_comprehensive_marine_data(tm='202501011200', stn=0)

        assert result == {'data': 'comprehensive'}
        call_args = mock_get.call_args
        assert 'sea_obs.php' in call_args[0][0]
        assert call_args[1]['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with BuoyClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_buoy_data(tm='202501011200')
