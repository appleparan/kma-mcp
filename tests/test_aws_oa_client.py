"""Unit tests for AWS Objective Analysis API client."""

from datetime import datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from kma_mcp.aws_oa_client import AWSOAClient


@pytest.fixture
def mock_auth_key() -> str:
    """Provide a mock authentication key for testing."""
    return 'test_auth_key_12345'


@pytest.fixture
def aws_oa_client(mock_auth_key: str) -> AWSOAClient:
    """Create an AWS OA client instance for testing."""
    return AWSOAClient(auth_key=mock_auth_key, timeout=10.0)


@pytest.fixture
def mock_response_data() -> dict:
    """Provide mock API response data."""
    return {
        'response': {
            'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
            'body': {
                'dataType': 'JSON',
                'items': {'item': [{'tm': '202501011200', 'ta': '5.2', 'x': '127.0', 'y': '37.5'}]},
            },
        }
    }


class TestAWSOAClientInit:
    """Test AWS OA client initialization."""

    def test_init_with_defaults(self, mock_auth_key: str) -> None:
        """Test client initialization with default values."""
        client = AWSOAClient(auth_key=mock_auth_key)
        assert client.auth_key == mock_auth_key
        assert client.timeout == 30.0

    def test_context_manager(self, mock_auth_key: str) -> None:
        """Test client as context manager."""
        with AWSOAClient(auth_key=mock_auth_key) as client:
            assert isinstance(client, AWSOAClient)


class TestAWSOAClientRequests:
    """Test AWS OA client API request methods."""

    @patch('httpx.Client.get')
    def test_get_analysis_data_with_string(
        self,
        mock_get: Mock,
        aws_oa_client: AWSOAClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting analysis data with string time format."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = aws_oa_client.get_analysis_data(tm='202501011200', x=127.0, y=37.5)

        assert result == mock_response_data
        assert 'kma_awsoa.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_get_analysis_data_with_datetime(
        self,
        mock_get: Mock,
        aws_oa_client: AWSOAClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting analysis data with datetime object."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        dt = datetime(2025, 1, 1, 12, 0)
        result = aws_oa_client.get_analysis_data(tm=dt, x=127.0, y=37.5)

        assert result == mock_response_data
        assert mock_get.call_args.kwargs['params']['tm'] == '202501011200'

    @patch('httpx.Client.get')
    def test_get_analysis_period(
        self,
        mock_get: Mock,
        aws_oa_client: AWSOAClient,
        mock_response_data: dict,
    ) -> None:
        """Test getting analysis data for a period."""
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = aws_oa_client.get_analysis_period('202501010000', '202501020000', 127.0, 37.5)

        assert result == mock_response_data
        assert 'kma_awsoa_2.php' in mock_get.call_args.args[0]

    @patch('httpx.Client.get')
    def test_request_error_handling(
        self,
        mock_get: Mock,
        aws_oa_client: AWSOAClient,
    ) -> None:
        """Test error handling for failed requests."""
        mock_get.side_effect = httpx.HTTPError('Connection error')

        with pytest.raises(httpx.HTTPError):
            aws_oa_client.get_analysis_data(tm='202501011200', x=127.0, y=37.5)
