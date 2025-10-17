"""Tests for GTS client."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from kma_mcp.global_met.gts_client import GTSClient


class TestGTSClientInit:
    """Test GTS client initialization."""

    def test_init_with_defaults(self):
        """Test client initialization with default parameters."""
        client = GTSClient('test_key')
        assert client.auth_key == 'test_key'
        assert isinstance(client._client, httpx.Client)
        client.close()

    def test_context_manager(self):
        """Test client works as a context manager."""
        with GTSClient('test_key') as client:
            assert isinstance(client, GTSClient)


class TestGTSClientRequests:
    """Test GTS client requests."""

    @patch('httpx.Client.get')
    def test_get_synop_observations(self, mock_get):
        """Test getting SYNOP observations."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'synop_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_synop_observations(tm='202501011200', dtm=3, stn=0)

        assert result == {'data': 'synop_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_ship_observations(self, mock_get):
        """Test getting ship observations."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'ship_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_ship_observations(tm='202501011200', dtm=6)

        assert result == {'data': 'ship_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_buoy_observations(self, mock_get):
        """Test getting buoy observations."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'buoy_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_buoy_observations(tm='202501011200', dtm=3)

        assert result == {'data': 'buoy_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_aircraft_reports(self, mock_get):
        """Test getting aircraft reports."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'airep_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_aircraft_reports(tm='202501011200', dtm=120)

        assert result == {'data': 'airep_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_surface_chart(self, mock_get):
        """Test getting surface chart."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'chart_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_surface_chart(tm='202501011200')

        assert result == {'data': 'chart_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_get_synop_chart(self, mock_get):
        """Test getting SYNOP chart."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'synop_chart_test'}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with GTSClient('test_key') as client:
            result = client.get_synop_chart(tm='202501011200')

        assert result == {'data': 'synop_chart_test'}
        mock_get.assert_called_once()

    @patch('httpx.Client.get')
    def test_request_error_handling(self, mock_get):
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('API Error')

        with GTSClient('test_key') as client, pytest.raises(httpx.HTTPError):
            client.get_synop_observations(tm='202501011200')
