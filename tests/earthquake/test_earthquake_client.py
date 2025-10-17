"""Tests for Earthquake API client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.earthquake.earthquake_client import EarthquakeClient


class TestEarthquakeClientInit:
    """Tests for EarthquakeClient initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = EarthquakeClient('test_key')
        assert client.auth_key == 'test_key'
        assert client._client.timeout.read == 30.0
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with EarthquakeClient('test_key') as client:
            assert client.auth_key == 'test_key'


class TestEarthquakeClientRequests:
    """Tests for Earthquake API requests."""

    @patch('httpx.Client.get')
    def test_get_recent_earthquake(self, mock_get):
        """Test getting recent earthquake data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'earthquake'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with EarthquakeClient('test_key') as client:
            result = client.get_recent_earthquake()

        assert result == {'data': 'earthquake'}
        call_args = mock_get.call_args
        assert 'eqk_now.php' in call_args[0][0]

    @patch('httpx.Client.get')
    def test_get_earthquake_list(self, mock_get):
        """Test getting earthquake list for a period."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'list'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with EarthquakeClient('test_key') as client:
            result = client.get_earthquake_list('202501010000', '202501310000')

        assert result == {'data': 'list'}
        call_args = mock_get.call_args
        assert 'eqk_list.php' in call_args[0][0]
        assert call_args[1]['params']['tm1'] == '202501010000'
        assert call_args[1]['params']['tm2'] == '202501310000'

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with EarthquakeClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_recent_earthquake()
