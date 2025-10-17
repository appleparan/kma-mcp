"""Unit tests for Forecast API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.forecast.forecast_client import ForecastClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def forecast_client(mock_auth_key: str) -> ForecastClient:
    """Create a Forecast client instance for testing."""
    return ForecastClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'tm_fc': '202501011200', 'ta': '5'}]},
            },
        }
    }


class TestForecastClientInit:
    """Test Forecast client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = ForecastClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with ForecastClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, ForecastClient)


class TestForecastClientRequests:
    """Test Forecast client API request methods."""

    @patch('httpx.Client.get')
    def test_get_short_term_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_forecast(tm_fc='202501011200', stn=108)

        assert result == mock_response_data
        assert 'kma_sfcfct.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_forecast(tm_fc='202501011200', stn=108)

        assert result == mock_response_data
        assert 'kma_mtfcst.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_weekly_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weekly forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_weekly_forecast(tm_fc='202501011200', stn=108)

        assert result == mock_response_data
        assert 'kma_wkfcst.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            forecast_client.get_short_term_forecast(tm_fc='202501011200', stn=108)
