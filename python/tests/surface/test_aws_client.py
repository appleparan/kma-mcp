"""Unit tests for AWS API client."""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.surface.aws_client import AWSClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing.

    Returns:
        Mock API authentication key
    """
    return 'test_auth_key_12345'


@pytest.fixture
def aws_client(mock_auth_key: str) -> AWSClient:
    """Create an AWS client instance for testing.

    Args:
        mock_auth_key: Mock authentication key

    Returns:
        AWSClient instance with mock auth key
    """
    return AWSClient(auth_key=mock_auth_key, timeout=10.0)


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
                'items': {
                    'item': [{'stnId': '108', 'tm': '202501011200', 'ta': '5.2', 'rn': '0.0'}]
                },
                'numOfRows': 1,
                'pageNo': 1,
                'totalCount': 1,
            },
        }
    }


class TestAWSClientInit:
    """Test AWS client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = AWSClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0
        assert isinstance(client._client, httpx.Client)

    def test_init_with_custom_timeout(self, mock_auth_key: str) -> None:
        """Test client initialization with custom timeout."""
        client = AWSClient(auth_key=mock_auth_key, timeout=60.0)
        assert client.timeout == 60.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with AWSClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, AWSClient)


class TestAWSClientRequests:
    """Test AWS client API request methods."""

    @patch('httpx.Client.get')
    def test_get_minutely_data_with_string(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting minutely data with string time format (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = aws_client.get_minutely_data(tm2='202302010900', stn=0)

        assert result == mock_response_data
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert 'tm2' in call_args.kwargs['params']
        assert call_args.kwargs['params']['tm2'] == '202302010900'
        assert call_args.kwargs['params']['stn'] == '0'
        assert call_args.kwargs['params']['authKey'] == 'test_auth_key_12345'
        assert 'nph-aws2_min' in call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_minutely_data_with_datetime(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting minutely data with datetime object (documented API)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2023, 2, 1, 9, 0, tzinfo=UTC)
        result = aws_client.get_minutely_data(tm2=dt, stn=0)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm2'] == '202302010900'

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            aws_client.get_minutely_data(tm2='202501011200', stn=108)

    @patch('httpx.Client.get')
    def test_all_stations_query(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
        mock_response_data: dict,
    ) -> None:
        """Test querying data for all stations (stn=0)."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = aws_client.get_minutely_data(tm2='202501011200', stn=0)

        assert result == mock_response_data
        call_args = mock_get.call_args
        assert call_args.kwargs['params']['stn'] == '0'


class TestAWSClientDateTimeConversion:
    """Test datetime conversion in AWS client."""

    @patch('httpx.Client.get')
    def test_datetime_to_minutely_format(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
        mock_response_data: dict,
    ) -> None:
        """Test conversion of datetime to YYYYMMDDHHmm format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 10, 18, 15, 30, tzinfo=UTC)
        aws_client.get_minutely_data(tm2=dt)

        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm2'] == '202510181530'

    @patch('httpx.Client.get')
    def test_datetime_to_daily_format(
        self,
        mock_get: Mock,
        aws_client: AWSClient,
        mock_response_data: dict,
    ) -> None:
        """Test conversion of datetime to YYYYMMDD format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 10, 18, 15, 30, tzinfo=UTC)
        aws_client.get_minutely_data(tm1=dt, tm2=dt)

        call_args = mock_get.call_args
        assert call_args.kwargs['params']['tm1'] == '202510181530'
