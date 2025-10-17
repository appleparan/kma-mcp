"""Tests for Upper-Air Radiosonde API client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.upper_air.radiosonde_client import RadiosondeClient


class TestRadiosondeClientInit:
    """Tests for RadiosondeClient initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = RadiosondeClient('test_key')
        assert client.auth_key == 'test_key'
        assert client._client.timeout.read == 30.0
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with RadiosondeClient('test_key') as client:
            assert client.auth_key == 'test_key'


class TestRadiosondeClientRequests:
    """Tests for Radiosonde API requests."""

    @patch('httpx.Client.get')
    def test_get_upper_air_data(self, mock_get):
        """Test getting upper-air data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with RadiosondeClient('test_key') as client:
            result = client.get_upper_air_data(tm='202501010000', stn=47122, pa=850)

        assert result == {'data': 'test'}
        call_args = mock_get.call_args
        assert 'upp_temp.php' in call_args[0][0]
        assert call_args[1]['params']['tm'] == '202501010000'
        assert call_args[1]['params']['pa'] == '850'

    @patch('httpx.Client.get')
    def test_get_stability_indices(self, mock_get):
        """Test getting atmospheric stability indices."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'stability'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with RadiosondeClient('test_key') as client:
            result = client.get_stability_indices('202501010000', '202501020000')

        assert result == {'data': 'stability'}
        call_args = mock_get.call_args
        assert 'upp_idx.php' in call_args[0][0]

    @patch('httpx.Client.get')
    def test_get_maximum_altitude_data(self, mock_get):
        """Test getting maximum altitude data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'altitude'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with RadiosondeClient('test_key') as client:
            result = client.get_maximum_altitude_data('20250101', '20250131')

        assert result == {'data': 'altitude'}
        call_args = mock_get.call_args
        assert 'upp_raw_max.php' in call_args[0][0]

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with RadiosondeClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_upper_air_data(tm='202501010000')
