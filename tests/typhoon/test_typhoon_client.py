"""Unit tests for Typhoon API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.typhoon.typhoon_client import TyphoonClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def typhoon_client(mock_auth_key: str) -> TyphoonClient:
    """Create a Typhoon client instance for testing."""
    return TyphoonClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'typ_id': '2501', 'name': 'TEST', 'lat': 25.0, 'lon': 130.0}]},
            },
        }
    }


class TestTyphoonClientInit:
    """Test Typhoon client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = TyphoonClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with TyphoonClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, TyphoonClient)


class TestTyphoonClientRequests:
    """Test Typhoon client API request methods."""

    @patch('httpx.Client.get')
    def test_get_current_typhoons(
        self,
        mock_get: Mock,
        typhoon_client: TyphoonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting current typhoons."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = typhoon_client.get_current_typhoons()

        assert result == mock_response_data
        assert 'kma_typ.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_typhoon_by_id(
        self,
        mock_get: Mock,
        typhoon_client: TyphoonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting typhoon by ID."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = typhoon_client.get_typhoon_by_id('2501')

        assert result == mock_response_data
        assert 'kma_typ_dtl.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_typhoon_forecast(
        self,
        mock_get: Mock,
        typhoon_client: TyphoonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting typhoon forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = typhoon_client.get_typhoon_forecast('2501')

        assert result == mock_response_data
        assert 'kma_typ_fcst.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_typhoon_history(
        self,
        mock_get: Mock,
        typhoon_client: TyphoonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting typhoon history."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = typhoon_client.get_typhoon_history(2024)

        assert result == mock_response_data
        assert 'kma_typ_hist.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        typhoon_client: TyphoonClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            typhoon_client.get_current_typhoons()
