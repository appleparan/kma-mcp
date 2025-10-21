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

    # Category 1: Short-term Forecast Tests
    @patch('httpx.Client.get')
    def test_get_short_term_region(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term forecast by region (documented endpoint)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_region(tmfc='202501011200')

        assert result == mock_response_data
        assert 'fct_shrt_reg.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_short_term_overview(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term forecast overview (documented endpoint)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_overview(tmfc='202501011200')

        assert result == mock_response_data
        assert 'fct_afs_ds.php' in mock_get.call_args.args[0]
        # Note: This endpoint does not use help parameter

    @patch('httpx.Client.get')
    def test_get_short_term_land(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term land forecast (documented endpoint)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_land(tmfc='202501011200', reg='11B00000')

        assert result == mock_response_data
        assert 'fct_afs_dl.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_short_term_land_v2(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term land forecast v2 (documented endpoint)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_land_v2(tmfc1='202501010000', tmfc2='202501020000')

        assert result == mock_response_data
        assert 'fct_afs_dl2.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_short_term_sea(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term sea forecast (documented endpoint)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_sea(tmef1='202501011200', tmef2='202501021200')

        assert result == mock_response_data
        assert 'fct_afs_do.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    # Category 2: Village Forecast Grid Data Tests
    @patch('httpx.Client.get')
    def test_get_village_short_term_grid(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting village short-term forecast grid data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_village_short_term_grid(
            tmfc='202402250500', tmef='202402250600', vars='TMP,SKY'
        )

        assert result == mock_response_data
        assert 'nph-dfs_shrt_grd' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_village_very_short_term_grid(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting village very short-term forecast grid data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_village_very_short_term_grid(
            tmfc='202403011010', tmef='202403011100', vars='T1H,SKY'
        )

        assert result == mock_response_data
        assert 'nph-dfs_vsrt_grd' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_village_observation_grid(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting village observation grid data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_village_observation_grid(tmfc='202403051010', vars='T1H,RN1')

        assert result == mock_response_data
        assert 'nph-dfs_odam_grd' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_convert_grid_to_coords(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test converting grid numbers to coordinates."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.convert_grid_to_coords(x=60, y=127)

        assert result == mock_response_data
        assert 'nph-dfs_xy_lonlat' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['x'] == '60'
        assert mock_get.call_args.kwargs['params']['y'] == '127'

    @patch('httpx.Client.get')
    def test_convert_coords_to_grid(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test converting coordinates to grid numbers."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.convert_coords_to_grid(lon=127.5, lat=36.5)

        assert result == mock_response_data
        assert 'nph-dfs_xy_lonlat' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['lon'] == '127.5'
        assert mock_get.call_args.kwargs['params']['lat'] == '36.5'

    # Category 3: Village Forecast Messages Tests
    @patch('httpx.Client.get')
    def test_get_weather_situation(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather situation messages."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_weather_situation(stn_id='108', num_of_rows=5)

        assert result == mock_response_data
        assert 'VilageFcstMsgService/getWthrSituation' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['stnId'] == '108'

    @patch('httpx.Client.get')
    def test_get_land_forecast_message(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting land forecast messages."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_land_forecast_message(reg_id='11B10101', num_of_rows=5)

        assert result == mock_response_data
        assert 'VilageFcstMsgService/getLandFcst' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['regId'] == '11B10101'

    @patch('httpx.Client.get')
    def test_get_sea_forecast_message(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting sea forecast messages."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_sea_forecast_message(reg_id='12A20100', num_of_rows=5)

        assert result == mock_response_data
        assert 'VilageFcstMsgService/getSeaFcst' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['regId'] == '12A20100'
