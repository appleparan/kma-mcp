"""Unit tests for Station Information API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.station_client import StationClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def station_client(mock_auth_key: str) -> StationClient:
    """Create a Station client instance for testing."""
    return StationClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'stnNm': 'Seoul', 'lat': '37.5', 'lon': '127.0'}]},
            },
        }
    }


class TestStationClientInit:
    """Test Station client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = StationClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with StationClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, StationClient)


class TestStationClientRequests:
    """Test Station client API request methods."""

    @patch('httpx.Client.get')
    def test_get_asos_stations(
        self,
        mock_get: Mock,
        station_client: StationClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting ASOS station information."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = station_client.get_asos_stations(stn=108)

        assert result == mock_response_data
        assert 'kma_stnlist.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_aws_stations(
        self,
        mock_get: Mock,
        station_client: StationClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting AWS station information."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = station_client.get_aws_stations(stn=108)

        assert result == mock_response_data
        assert 'kma_aws_stnlist.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        station_client: StationClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            station_client.get_asos_stations(stn=108)
