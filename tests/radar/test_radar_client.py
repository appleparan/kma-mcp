"""Unit tests for Radar API client."""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.radar.radar_client import RadarClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def radar_client(mock_auth_key: str) -> RadarClient:
    """Create a Radar client instance for testing."""
    return RadarClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {
                    'item': [{'tm': '202501011200', 'radar': 'ALL', 'image_url': 'http://...'}]
                },
            },
        }
    }


class TestRadarClientInit:
    """Test Radar client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = RadarClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with RadarClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, RadarClient)


class TestRadarClientRequests:
    """Test Radar client API request methods."""

    @patch('httpx.Client.get')
    def test_get_radar_image_with_string(
        self,
        mock_get: Mock,
        radar_client: RadarClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting radar image with string time."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = radar_client.get_radar_image(tm='202501011200')

        assert result == mock_response_data
        assert 'kma_radar.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_radar_image_with_datetime(
        self,
        mock_get: Mock,
        radar_client: RadarClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting radar image with datetime."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 1, 1, 12, 0, tzinfo=UTC)
        result = radar_client.get_radar_image(tm=dt)

        assert result == mock_response_data
        assert mock_get.call_args.kwargs['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_get_radar_image_sequence(
        self,
        mock_get: Mock,
        radar_client: RadarClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting radar image sequence."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = radar_client.get_radar_image_sequence('202501011200', '202501011300')

        assert result == mock_response_data
        assert 'kma_radar_2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_radar_reflectivity(
        self,
        mock_get: Mock,
        radar_client: RadarClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting radar reflectivity."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = radar_client.get_radar_reflectivity('202501011200', 127.0, 37.5)

        assert result == mock_response_data
        assert 'kma_radar_ref.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        radar_client: RadarClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            radar_client.get_radar_image(tm='202501011200')
