"""Unit tests for UV Radiation API client."""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.surface.uv_client import UVClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def uv_client(mock_auth_key: str) -> UVClient:
    """Create a UV client instance for testing."""
    return UVClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'tm': '202501011200', 'uv': '3'}]},
            },
        }
    }


class TestUVClientInit:
    """Test UV client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = UVClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with UVClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, UVClient)


class TestUVClientRequests:
    """Test UV client API request methods."""

    @patch('httpx.Client.get')
    def test_get_observation_data_with_string(
        self,
        mock_get: Mock,
        uv_client: UVClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting UV observation data with string time format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = uv_client.get_observation_data(tm='202203211500', stn=108)

        assert result == mock_response_data
        assert 'kma_sfctm_uv.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_observation_data_with_datetime(
        self,
        mock_get: Mock,
        uv_client: UVClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting UV observation data with datetime object."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2022, 3, 21, 15, 0, tzinfo=UTC)
        result = uv_client.get_observation_data(tm=dt, stn=108)

        assert result == mock_response_data
        assert mock_get.call_args.kwargs['params']['tm'] == '202203211500'

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        uv_client: UVClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            uv_client.get_observation_data(tm='202203211500', stn=108)
