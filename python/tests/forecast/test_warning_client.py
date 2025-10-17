"""Unit tests for Warning API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.forecast.warning_client import WarningClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def warning_client(mock_auth_key: str) -> WarningClient:
    """Create a Warning client instance for testing."""
    return WarningClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'type': 'heavy_rain', 'level': 'warning'}]},
            },
        }
    }


class TestWarningClientInit:
    """Test Warning client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = WarningClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with WarningClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, WarningClient)


class TestWarningClientRequests:
    """Test Warning client API request methods."""

    @patch('httpx.Client.get')
    def test_get_current_warnings(
        self,
        mock_get: Mock,
        warning_client: WarningClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting current warnings."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = warning_client.get_current_warnings(stn=108)

        assert result == mock_response_data
        assert 'kma_wn.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_warning_history(
        self,
        mock_get: Mock,
        warning_client: WarningClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting warning history."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = warning_client.get_warning_history('20250101', '20250131', stn=108)

        assert result == mock_response_data
        assert 'kma_wn_2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_special_weather_report(
        self,
        mock_get: Mock,
        warning_client: WarningClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting special weather report."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = warning_client.get_special_weather_report(tm='202501011200', stn=108)

        assert result == mock_response_data
        assert 'kma_swr.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        warning_client: WarningClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            warning_client.get_current_warnings(stn=108)
