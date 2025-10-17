"""Tests for Satellite API client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.satellite.satellite_client import SatelliteClient


class TestSatelliteClientInit:
    """Tests for SatelliteClient initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = SatelliteClient('test_key')
        assert client.auth_key == 'test_key'
        assert client._client.timeout.read == 60.0
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with SatelliteClient('test_key') as client:
            assert client.auth_key == 'test_key'


class TestSatelliteClientRequests:
    """Tests for Satellite API requests."""

    @patch('httpx.Client.get')
    def test_get_satellite_file_list(self, mock_get):
        """Test getting satellite file list."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'files': ['file1', 'file2']}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with SatelliteClient('test_key') as client:
            result = client.get_satellite_file_list(area='KO')

        assert result == {'files': ['file1', 'file2']}
        call_args = mock_get.call_args
        assert 'sat_file_list.php' in call_args[0][0]
        assert call_args[1]['params']['area'] == 'KO'

    @patch('httpx.Client.get')
    def test_get_satellite_imagery(self, mock_get):
        """Test getting satellite imagery."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'imagery'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with SatelliteClient('test_key') as client:
            result = client.get_satellite_imagery(
                level='l1b', product='NR016', area='KO', tm='202501011200'
            )

        assert result == {'data': 'imagery'}
        call_args = mock_get.call_args
        assert 'sat_file_down2.php' in call_args[0][0]
        assert call_args[1]['params']['lvl'] == 'l1b'
        assert call_args[1]['params']['dat'] == 'NR016'

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with SatelliteClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_satellite_file_list()
