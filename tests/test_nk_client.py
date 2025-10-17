"""Unit tests for North Korea Meteorological API client."""

from datetime import datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.nk_client import NKClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def nk_client(mock_auth_key: str) -> NKClient:
    """Create a North Korea client instance for testing."""
    return NKClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'tm': '202501011200', 'ta': '5.2'}]},
            },
        }
    }


class TestNKClientInit:
    """Test North Korea client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = NKClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with NKClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, NKClient)


class TestNKClientRequests:
    """Test North Korea client API request methods."""

    @patch('httpx.Client.get')
    def test_get_hourly_data_with_string(
        self,
        mock_get: Mock,
        nk_client: NKClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly North Korea data with string time format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = nk_client.get_hourly_data(tm='202501011200', stn=108)

        assert result == mock_response_data
        assert 'kma_nkobs.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_hourly_data_with_datetime(
        self,
        mock_get: Mock,
        nk_client: NKClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly North Korea data with datetime object."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 1, 1, 12, 0)
        result = nk_client.get_hourly_data(tm=dt, stn=108)

        assert result == mock_response_data
        assert mock_get.call_args.kwargs['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_get_hourly_period(
        self,
        mock_get: Mock,
        nk_client: NKClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly North Korea data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = nk_client.get_hourly_period('202501010000', '202501020000', 108)

        assert result == mock_response_data
        assert 'kma_nkobs_2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_daily_data(
        self,
        mock_get: Mock,
        nk_client: NKClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting daily North Korea data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = nk_client.get_daily_data(tm='20250101', stn=108)

        assert result == mock_response_data
        assert 'kma_nkobs_day.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_daily_period(
        self,
        mock_get: Mock,
        nk_client: NKClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting daily North Korea data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = nk_client.get_daily_period('20250101', '20250131', 108)

        assert result == mock_response_data
        assert 'kma_nkobs_day2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        nk_client: NKClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            nk_client.get_hourly_data(tm='202501011200', stn=108)
