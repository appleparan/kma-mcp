"""Unit tests for Seasonal Observation API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.season_client import SeasonClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def season_client(mock_auth_key: str) -> SeasonClient:
    """Create a Seasonal client instance for testing."""
    return SeasonClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'year': '2025', 'event': 'cherry_blossom'}]},
            },
        }
    }


class TestSeasonClientInit:
    """Test Seasonal client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = SeasonClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with SeasonClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, SeasonClient)


class TestSeasonClientRequests:
    """Test Seasonal client API request methods."""

    @patch('httpx.Client.get')
    def test_get_observation_data(
        self,
        mock_get: Mock,
        season_client: SeasonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting seasonal observation data for a year."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = season_client.get_observation_data(year=2025, stn=108)

        assert result == mock_response_data
        assert 'kma_season.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_observation_period(
        self,
        mock_get: Mock,
        season_client: SeasonClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting seasonal observation data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = season_client.get_observation_period(2020, 2025, 108)

        assert result == mock_response_data
        assert 'kma_season_2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        season_client: SeasonClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            season_client.get_observation_data(year=2025, stn=108)
