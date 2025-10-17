"""Async KMA Typhoon Information API client.

This module provides a client for accessing the Korea Meteorological Administration's
Typhoon Information (태풍) API for tropical cyclone tracking and forecasting.

Typhoon information provides critical data on tropical cyclones including
position, intensity, movement, and forecast tracks for disaster preparedness.
"""

from typing import Any

import httpx


class AsyncTyphoonClient:
    """Async client for KMA Typhoon Information API.

    The Typhoon Information system provides comprehensive data on
    tropical cyclones including current position, intensity, movement
    speed/direction, and forecast tracks for disaster preparedness.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Typhoon Information client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncTyphoonClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Typhoon Information API.

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

    async def get_current_typhoons(self) -> dict[str, Any]:
        """Get information on currently active typhoons.

        Returns:
            Current active typhoon information

        Example:
            >>> async with AsyncTyphoonClient('your_auth_key')
            >>> ...     data = await client.get_current_typhoons()
        """
        params = {'help': '0'}
        return await self._make_request('kma_typ.php', params)

    async def get_typhoon_by_id(
        self,
        typhoon_id: str,
    ) -> dict[str, Any]:
        """Get detailed information for a specific typhoon.

        Args:
            typhoon_id: Typhoon identification number (e.g., '2501')

        Returns:
            Detailed typhoon information

        Example:
            >>> async with AsyncTyphoonClient('your_auth_key')
            >>> ...     data = await client.get_typhoon_by_id('2501')
        """
        params = {'typ_id': typhoon_id, 'help': '0'}
        return await self._make_request('kma_typ_dtl.php', params)

    async def get_typhoon_forecast(
        self,
        typhoon_id: str,
    ) -> dict[str, Any]:
        """Get forecast track for a specific typhoon.

        Args:
            typhoon_id: Typhoon identification number

        Returns:
            Typhoon forecast track data

        Example:
            >>> async with AsyncTyphoonClient('your_auth_key')
            >>> ...     data = await client.get_typhoon_forecast('2501')
        """
        params = {'typ_id': typhoon_id, 'help': '0'}
        return await self._make_request('kma_typ_fcst.php', params)

    async def get_typhoon_history(
        self,
        year: int | str,
    ) -> dict[str, Any]:
        """Get typhoon history for a specific year.

        Args:
            year: Year in 'YYYY' format

        Returns:
            Typhoon history data for the year

        Example:
            >>> async with AsyncTyphoonClient('your_auth_key')
            >>> ...     data = await client.get_typhoon_history(2024)
        """
        params = {'year': str(year), 'help': '0'}
        return await self._make_request('kma_typ_hist.php', params)
