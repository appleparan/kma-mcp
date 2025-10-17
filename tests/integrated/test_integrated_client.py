"""Tests for Integrated client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.integrated.integrated_client import IntegratedClient


class TestIntegratedClientInit:
    """Test Integrated client initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = IntegratedClient('test_key')
        assert client.auth_key == 'test_key'
        assert isinstance(client._client, httpx.Client)
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with IntegratedClient('test_key') as client:
            assert isinstance(client, IntegratedClient)


class TestIntegratedClientRequests:
    """Test Integrated client requests."""

    @patch('httpx.Client.get')
    def test_get_lightning_data(self, mock_get):
        """Test getting lightning data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'lightning_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with IntegratedClient('test_key') as client:
            result = client.get_lightning_data(tm1='202501011200', tm2='202501011500')

        assert result == {'data': 'lightning_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_wind_profiler_data(self, mock_get):
        """Test getting wind profiler data."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'profiler_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with IntegratedClient('test_key') as client:
            result = client.get_wind_profiler_data(tm='202501011200', stn=0, mode='L')

        assert result == {'data': 'profiler_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with IntegratedClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_lightning_data(tm1='202501011200', tm2='202501011500')
