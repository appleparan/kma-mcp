"""Unit tests for ASOS API client."""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.surface.asos_client import ASOSClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing.

    Returns:
        Mock API authentication key
    """
    return 'test_auth_key_12345'


@pytest.fixture
def asos_client(mock_auth_key: str) -> ASOSClient:
    """Create an ASOS client instance for testing.

    Args:
        mock_auth_key: Mock authentication key

    Returns:
        ASOSClient instance with mock auth key
    """
    return ASOSClient(auth_key=mock_auth_key, timeout=10.0)


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
                'items': {'item': [{'stnId': '108', 'tm': '202501011200', 'ta': '5.2'}]},
                'numOfRows': 1,
                'pageNo': 1,
                'totalCount': 1,
            },
        }
    }


class TestASOSClientInit:
    """Test ASOS client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = ASOSClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0
        assert isinstance(client._client, httpx.Client)

    def test_init_with_custom_timeout(self, mock_auth_key: str) -> None:
        """Test client initialization with custom timeout."""
        client = ASOSClient(auth_key=mock_auth_key, timeout=60.0)
        assert client.timeout == 60.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with ASOSClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, ASOSClient)


class TestASOSClientRequests:
    """Test ASOS client API request methods."""

    @patch('httpx.Client.get')
    def test_get_hourly_data_with_string(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly data with string time format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_hourly_data(tm='202501011200', stn=108)

        assert result == mock_response_data
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert 'tm' in call_args.kwargs['params']
        assert call_args.kwargs['params']['tm'] == '202501011200'
        assert call_args.kwargs['params']['stn'] == '108'
        assert call_args.kwargs['params']['authKey'] == 'test_auth_key_12345'

    @patch('httpx.Client.get')
    def test_get_hourly_data_with_datetime(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly data with datetime object."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 1, 1, 12, 0, tzinfo=UTC)
        result = asos_client.get_hourly_data(tm=dt, stn=108)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_get_hourly_period(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting hourly data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_hourly_period(
            tm1='202501010000',
            tm2='202501020000',
            stn=108,
        )

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm1'] == '202501010000'
        assert call_args.kwargs['params']['tm2'] == '202501020000'
        assert 'kma_sfctm3.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_daily_data(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting daily observation data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_daily_data(tm='20250101', stn=108)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm'] == '20250101'
        assert 'kma_sfcdd.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_daily_period(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting daily data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_daily_period(
            tm1='20250101',
            tm2='20250131',
            stn=108,
        )

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm1'] == '20250101'
        assert call_args.kwargs['params']['tm2'] == '20250131'
        assert 'kma_sfcdd3.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_element_data(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting element-specific observation data."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_element_data(
            tm1='202501010000',
            tm2='202501020000',
            obs='TA',
            stn=108,
        )

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['obs'] == 'TA'
        assert 'kma_sfctm5.php' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            asos_client.get_hourly_data(tm='202501011200', stn=108)

    @patch('httpx.Client.get')
    def test_all_stations_query(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test querying data for all stations (stn=0)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = asos_client.get_hourly_data(tm='202501011200', stn=0)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['stn'] == '0'


class TestASOSClientDateTimeConversion:
    """Test datetime conversion in ASOS client."""

    @patch('httpx.Client.get')
    def test_datetime_to_hourly_format(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test conversion of datetime to YYYYMMDDHHmm format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 10, 18, 15, 30, tzinfo=UTC)
        asos_client.get_hourly_data(tm=dt)

        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm'] == '202510181530'

    @patch('httpx.Client.get')
    def test_datetime_to_daily_format(
        self,
        mock_get: Mock,
        asos_client: ASOSClient,
        mock_response_data: dict,
    ) -> None:
        """Test conversion of datetime to YYYYMMDD format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 10, 18, tzinfo=UTC)
        asos_client.get_daily_data(tm=dt)

        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm'] == '20251018'
