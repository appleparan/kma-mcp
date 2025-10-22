"""Unit tests for Forecast API client."""

from unittest.mock import Mock, patch

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

    # Category 4: Village Forecast API Tests
    @patch('httpx.Client.get')
    def test_get_ultra_short_term_observation(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting ultra short-term observation data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_ultra_short_term_observation(
            base_date='20210628', base_time='0600', nx=55, ny=127
        )

        assert result == mock_response_data
        assert 'VilageFcstInfoService_2.0/getUltraSrtNcst' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_ultra_short_term_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting ultra short-term forecast data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_ultra_short_term_forecast(
            base_date='20210628', base_time='0630', nx=55, ny=127
        )

        assert result == mock_response_data
        assert 'VilageFcstInfoService_2.0/getUltraSrtFcst' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_village_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting village short-term forecast data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_village_forecast(
            base_date='20210628', base_time='0500', nx=55, ny=127
        )

        assert result == mock_response_data
        assert 'VilageFcstInfoService_2.0/getVilageFcst' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_forecast_version(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting forecast version information."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_forecast_version(ftype='SHRT', basedatetime='202106280800')

        assert result == mock_response_data
        assert 'VilageFcstInfoService_2.0/getFcstVersion' in mock_get.call_args.args[0]

    # Category 5: Forecast Distribution Maps Tests
    @patch('httpx.Client.get')
    def test_get_short_term_distribution_map(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting short-term forecast distribution map."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_short_term_distribution_map(
            data0='GEMD', data1='PTY', tm_fc='202212221400', tm_ef='202212260000'
        )

        assert result == mock_response_data
        assert 'nph-dfs_shrt_ana_5d_test' in mock_get.call_args.args[0]
        assert 'typ03/cgi/dfs' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_very_short_term_distribution_map(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting very short-term forecast distribution map."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_very_short_term_distribution_map(
            data0='GEMD', data1='TMP', tm_fc='202212221400', tm_ef='202212260000'
        )

        assert result == mock_response_data
        assert 'nph-dfs_shrt_ana_5d_test' in mock_get.call_args.args[0]

    # Category 6: Grid Coordinate Data Tests
    @patch('httpx.Client.get')
    def test_get_grid_latlon_data(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting grid latitude/longitude data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_grid_latlon_data(fct='SHRT', latlon='lon')

        assert result == mock_response_data
        assert 'nph-dfs_latlon_api' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['fct'] == 'SHRT'
        assert mock_get.call_args.kwargs['params']['latlon'] == 'lon'

    @patch('httpx.Client.get')
    def test_download_grid_latlon_netcdf(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test downloading grid lat/lon NetCDF file."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.download_grid_latlon_netcdf(fct='SHRT')

        assert result == mock_response_data
        assert 'nph-dfs_latlon_api' in mock_get.call_args.args[0]

    # Category 7: Medium-term Forecast Tests
    @patch('httpx.Client.get')
    def test_get_medium_term_region(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term forecast region data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_region(tmfc='0')

        assert result == mock_response_data
        assert 'fct_medm_reg.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_medium_term_overview(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term forecast overview."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_overview(tmfc1='2013121106', tmfc2='2013121118')

        assert result == mock_response_data
        assert 'fct_afs_ws.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_land(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term land forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_land(
            reg='', tmfc1='2013121106', tmfc2='2013121118'
        )

        assert result == mock_response_data
        assert 'fct_afs_wl.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_temperature(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term temperature forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_temperature(tmfc1='2013121106', tmfc2='2013121118')

        assert result == mock_response_data
        assert 'fct_afs_wc.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_sea(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term sea forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_sea(tmfc1='2013121106', tmfc2='2013121118')

        assert result == mock_response_data
        assert 'fct_afs_wo.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_sea_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term sea forecast via OpenAPI."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_sea_forecast(
            reg_id='12A20000', tm_fc='201404080600'
        )

        assert result == mock_response_data
        assert 'MidFcstInfoService/getMidSeaFcst' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['regId'] == '12A20000'

    @patch('httpx.Client.get')
    def test_get_medium_term_temperature_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term temperature forecast via OpenAPI."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_temperature_forecast(
            reg_id='11B10101', tm_fc='201309030600'
        )

        assert result == mock_response_data
        assert 'MidFcstInfoService/getMidTa' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_land_forecast(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term land forecast via OpenAPI."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_land_forecast(
            reg_id='11B00000', tm_fc='202107300600'
        )

        assert result == mock_response_data
        assert 'MidFcstInfoService/getMidLandFcst' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_medium_term_outlook(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting medium-term outlook forecast."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_medium_term_outlook(stn_id='108', tm_fc='201310170600')

        assert result == mock_response_data
        assert 'MidFcstInfoService/getMidFcst' in mock_get.call_args.args[0]

    # Category 8: Weather Warnings Tests
    @patch('httpx.Client.get')
    def test_get_warning_region(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather warning region data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_warning_region(tmfc1='201501010000', tmfc2='201502010000')

        assert result == mock_response_data
        assert 'wrn_reg.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['help'] == '1'

    @patch('httpx.Client.get')
    def test_get_warning_data(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather warning data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_warning_data(
            wrn='R', tmfc1='201501010000', tmfc2='201502010000'
        )

        assert result == mock_response_data
        assert 'wrn_met_data.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_weather_information(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather information reports."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_weather_information(tmfc1='201505010000', tmfc2='201506010000')

        assert result == mock_response_data
        assert 'wrn_inf_rpt.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_weather_commentary(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather commentary reports."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_weather_commentary(tmfc1='202004130000', tmfc2='202004140000')

        assert result == mock_response_data
        assert 'wthr_cmt_rpt.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_current_warning_status(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting current warning status."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_current_warning_status(fe='f')

        assert result == mock_response_data
        assert 'wrn_now_data.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_current_warning_status_new(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting current warning status (new version)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_current_warning_status_new(fe='f')

        assert result == mock_response_data
        assert 'wrn_now_data_new.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_warning_image(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting weather warning image."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_warning_image(
            tm='201611082300',
            lon=127.7,
            lat=36.1,
            range=300,
            size=685,
            wrn='W,R,C,D,O,V,T,S,Y,H',
        )

        assert result == mock_response_data
        assert 'nph-wrn7' in mock_get.call_args.args[0]
        assert 'typ03/cgi/wrn' in mock_get.call_args.args[0]

    # Category 9: Impact Forecast Tests
    @patch('httpx.Client.get')
    def test_get_impact_forecast_status(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting impact forecast status."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_impact_forecast_status(
            tmef1='20210701', tmef2='20210730', ifpar='hw'
        )

        assert result == mock_response_data
        assert 'ifs_fct_pstt.php' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['ifpar'] == 'hw'

    @patch('httpx.Client.get')
    def test_get_impact_risk_level_zone_count(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting impact risk level zone count."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_impact_risk_level_zone_count(
            tmef1='20210701', tmef2='20210730'
        )

        assert result == mock_response_data
        assert 'ifs_ilvl_zone_cnt.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_impact_risk_level_distribution_map(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting impact risk level distribution map."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_impact_risk_level_distribution_map(tmfc='20220601')

        assert result == mock_response_data
        assert 'ifs_ilvl_dmap.php' in mock_get.call_args.args[0]

    # Category 10: Region Information Tests
    @patch('httpx.Client.get')
    def test_get_forecast_zone_code(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting forecast zone code information."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_forecast_zone_code(reg_id='11A00101')

        assert result == mock_response_data
        assert 'FcstZoneInfoService/getFcstZoneCd' in mock_get.call_args.args[0]
        assert mock_get.call_args.kwargs['params']['regId'] == '11A00101'

    @patch('httpx.Client.get')
    def test_get_warning_zone_code(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting warning zone code information."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_warning_zone_code()

        assert result == mock_response_data
        assert 'WethrBasicInfoService/getWrnZoneCd' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_aws_warning_zone_code(
        self,
        mock_get: Mock,
        forecast_client: ForecastClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting AWS station warning zone codes."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = forecast_client.get_aws_warning_zone_code()

        assert result == mock_response_data
        assert 'wrn_reg_aws2.php' in mock_get.call_args.args[0]
