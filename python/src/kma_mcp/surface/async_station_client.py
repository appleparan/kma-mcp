"""Async KMA Surface Observation Station Information API client.

This module provides a client for accessing the Korea Meteorological Administration's
Surface Observation Station Information (지상관측 지점정보) API.

Station information provides metadata about weather observation stations
including location, altitude, and operational status.
"""

from typing import Any

import httpx


class AsyncStationClient:
    """Async client for KMA Surface Observation Station Information API.

    The Station Information system provides metadata about weather
    observation stations including location coordinates, altitude,
    station type, and operational status.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Station Information client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncStationClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Station Information API.

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

    async def get_asos_stations(self, stn: int | str = 0) -> dict[str, Any]:
        """Get ASOS station information.

        Args:
            stn: Station number (0 for all stations)

        Returns:
            ASOS station information

        Example:
            >>> async with AsyncStationClient('your_auth_key')
            >>> ...     data = await client.get_asos_stations()  # All stations
            >>> ...     data = await client.get_asos_stations(108)  # Specific station
        """
        params = {'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_stnlist.php', params)

    async def get_aws_stations(self, stn: int | str = 0) -> dict[str, Any]:
        """Get AWS station information.

        Args:
            stn: Station number (0 for all stations)

        Returns:
            AWS station information

        Example:
            >>> async with AsyncStationClient('your_auth_key')
            >>> ...     data = await client.get_aws_stations()  # All stations
        """
        params = {'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws_stnlist.php', params)
