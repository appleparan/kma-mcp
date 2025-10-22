"""Unit tests for Snow Depth API client."""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.surface.snow_client import SnowClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def snow_client(mock_auth_key: str) -> SnowClient:
    """Create a Snow client instance for testing."""
    return SnowClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'tm': '202501011200', 'sd': '10.5'}]},
            },
        }
    }


class TestSnowClientInit:
    """Test Snow client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = SnowClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with SnowClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, SnowClient)


class TestSnowClientRequests:
    """Test Snow client API request methods."""

    @patch('httpx.Client.get')
    def test_get_snow_depth_with_string(
        self,
        mock_get: Mock,
        snow_client: SnowClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting snow depth with string time format (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = snow_client.get_snow_depth(tm='201412051800', sd_type='tot')

        assert result == mock_response_data
        assert 'kma_snow1.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['sd'] == 'tot'

    @patch('httpx.Client.get')
    def test_get_snow_depth_with_datetime(
        self,
        mock_get: Mock,
        snow_client: SnowClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting snow depth with datetime object (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2014, 12, 5, 18, 0, tzinfo=UTC)
        result = snow_client.get_snow_depth(tm=dt, sd_type='day')

        assert result == mock_response_data
        assert mock_get.call_args.kwargs['params']['tm'] == '201412051800'
        assert mock_get.call_args.kwargs['params']['sd'] == 'day'

    @patch('httpx.Client.get')
    def test_get_snow_period(
        self,
        mock_get: Mock,
        snow_client: SnowClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting snow depth for a period (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = snow_client.get_snow_period('201412051800', '201412040100', snow=0)

        assert result == mock_response_data
        assert 'kma_snow2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_max_snow_depth(
        self,
        mock_get: Mock,
        snow_client: SnowClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting maximum snow depth for a period (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = snow_client.get_max_snow_depth('20150131', '20150125', sd_type='tot', stn=0)

        assert result == mock_response_data
        assert 'kma_snow_day.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['sd'] == 'tot'

