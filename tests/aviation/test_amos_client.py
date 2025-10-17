"""Tests for AMOS client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.aviation.amos_client import AMOSClient


class TestAMOSClientInit:
    """Test AMOS client initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = AMOSClient('test_key')
        assert client.auth_key == 'test_key'
        assert isinstance(client._client, httpx.Client)
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with AMOSClient('test_key') as client:
            assert isinstance(client, AMOSClient)


class TestAMOSClientRequests:
    """Test AMOS client requests."""

    @patch('httpx.Client.get')
    def test_get_airport_observations(self, mock_get):
        """Test getting airport observations."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'amos_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with AMOSClient('test_key') as client:
            result = client.get_airport_observations(tm='202501011200', dtm=60)

        assert result == {'data': 'amos_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_amdar_data(self, mock_get):
        """Test getting AMDAR data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'amdar_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with AMOSClient('test_key') as client:
            result = client.get_amdar_data(tm1='202501011200', tm2='202501011400')

        assert result == {'data': 'amdar_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with AMOSClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_airport_observations(tm='202501011200')
