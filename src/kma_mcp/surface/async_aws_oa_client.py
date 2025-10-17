"""Async KMA AWS Objective Analysis API client.

This module provides a client for accessing the Korea Meteorological Administration's
AWS Objective Analysis (AWS 객관분석) API for objectively analyzed weather data.

AWS Objective Analysis provides gridded meteorological data derived from
AWS observations through objective analysis techniques for improved spatial coverage.
"""

from datetime import datetime
from typing import Any

import httpx


class AsyncAWSOAClient:
    """Async client for KMA AWS Objective Analysis API.

    The AWS Objective Analysis system provides gridded meteorological data
    derived from AWS observations through objective analysis techniques,
    offering improved spatial coverage and consistency for weather analysis.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize AWS Objective Analysis client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncAWSOAClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to AWS Objective Analysis API.

        Args:
            endpoint: API endpoint path
            params: Query parameters

        Returns:
            API response as dictionary

        Raises:
            httpx.HTTPError: If request fails
        """
        params['authKey'] = self.auth_key
        url = f'{self.BASE_URL}/{endpoint}'
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_analysis_data(
        self,
        tm: str | datetime,
        x: float,
        y: float,
    ) -> dict[str, Any]:
        """Get AWS objective analysis data for a specific location and time.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            x: Longitude coordinate
            y: Latitude coordinate

        Returns:
            AWS objective analysis data

        Example:
            >>> async with AsyncAWSOAClient('your_auth_key')
            >>> ...     data = await client.get_analysis_data('202501011200', 127.0, 37.5)
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'x': str(x), 'y': str(y), 'help': '0'}
        return await self._make_request('kma_awsoa.php', params)

    async def get_analysis_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        x: float,
        y: float,
    ) -> dict[str, Any]:
        """Get AWS objective analysis data for a location over a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            x: Longitude coordinate
            y: Latitude coordinate

        Returns:
            AWS objective analysis data for the period

        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'x': str(x), 'y': str(y), 'help': '0'}
        return await self._make_request('kma_awsoa_2.php', params)
