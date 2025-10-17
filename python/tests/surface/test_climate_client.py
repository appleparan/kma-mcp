"""Unit tests for Climate Statistics API client."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.surface.climate_client import ClimateClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing.

    Returns:
        Mock API authentication key
    """
    return 'test_auth_key_12345'


@pytest.fixture
def climate_client(mock_auth_key: str) -> ClimateClient:
    """Create a Climate client instance for testing.

    Args:
        mock_auth_key: Mock authentication key

    Returns:
        ClimateClient instance with mock auth key
    """
    return ClimateClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data.

    Returns:
        Sample API response dictionary
    """
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'stnId': '108', 'avgTa': '15.2', 'sumRn': '45.3'}]},
                'numOfRows': 1,
                'pageNo': 1,
                'totalCount': 1,
            },
        }
    }


class TestClimateClientInit:
    """Test Climate client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = ClimateClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0
        assert isinstance(client._client, httpx.Client)

    def test_init_with_custom_timeout(self, mock_auth_key: str) -> None:
        """Test client initialization with custom timeout."""
        client = ClimateClient(auth_key=mock_auth_key, timeout=60.0)
        assert client.timeout == 60.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with ClimateClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, ClimateClient)


class TestClimateClientRequests:
    """Test Climate client API request methods."""

    @patch('httpx.Client.get')
    def test_get_daily_normals(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting daily climate normals."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_daily_normals(1, 1, 1, 31, 108)

        assert result == mock_response_data
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['stn'] == '108'
        assert call_args.kwargs['params']['mm1'] == '01'
        assert call_args.kwargs['params']['dd1'] == '01'
        assert call_args.kwargs['params']['mm2'] == '01'
        assert call_args.kwargs['params']['dd2'] == '31'
        assert call_args.kwargs['params']['authKey'] == 'test_auth_key_12345'
        assert 'kma_clm_daily.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_ten_day_normals(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting 10-day climate normals."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_ten_day_normals(1, 1, 1, 3, 108)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['mm1'] == '01'
        assert call_args.kwargs['params']['dd1'] == '1'
        assert call_args.kwargs['params']['mm2'] == '01'
        assert call_args.kwargs['params']['dd2'] == '3'
        assert 'kma_clm_tenday.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_monthly_normals(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting monthly climate normals."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_monthly_normals(1, 12, 108)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['mm1'] == '01'
        assert call_args.kwargs['params']['mm2'] == '12'
        assert 'kma_clm_month.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_annual_normals(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting annual climate normals."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_annual_normals(108)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['stn'] == '108'
        assert 'kma_clm_year.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_normals_by_period_daily(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test flexible period specification with daily type."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_normals_by_period('daily', 1, 1, 1, 31, 108)

        assert result == mock_response_data
        assert 'kma_clm_daily.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_normals_by_period_monthly(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test flexible period specification with monthly type."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_normals_by_period('monthly', 1, None, 12, None, 108)

        assert result == mock_response_data
        assert 'kma_clm_month.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_normals_by_period_annual(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test flexible period specification with annual type."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_normals_by_period('annual', stn=108)

        assert result == mock_response_data
        assert 'kma_clm_year.php' in mock_get.call_args.args[0]

    def test_get_normals_by_period_invalid_type(
        self,
        climate_client: ClimateClient,
    ) -> None:
        """Test error handling for invalid period type."""
        with pytest.raises(ValueError, match='Invalid period_type'):
            climate_client.get_normals_by_period('invalid', 1, 1, 1, 31)

    def test_get_normals_by_period_missing_params_daily(
        self,
        climate_client: ClimateClient,
    ) -> None:
        """Test error handling for missing parameters in daily normals."""
        with pytest.raises(ValueError, match='Daily normals require'):
            climate_client.get_normals_by_period('daily', 1, None, 1, 31)

    def test_get_normals_by_period_missing_params_monthly(
        self,
        climate_client: ClimateClient,
    ) -> None:
        """Test error handling for missing parameters in monthly normals."""
        with pytest.raises(ValueError, match='Monthly normals require'):
            climate_client.get_normals_by_period('monthly', 1, None, None, None)

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            climate_client.get_annual_normals(108)

    @patch('httpx.Client.get')
    def test_all_stations_query(
        self,
        mock_get: Mock,
        climate_client: ClimateClient,
        mock_response_data: dict,
    ) -> None:
        """Test querying data for all stations (stn=0)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = climate_client.get_monthly_normals(1, 12, 0)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['stn'] == '0'
