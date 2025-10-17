"""Async client for KMA Marine Meteorological Buoy API.

This module provides access to marine observation data from buoys and wave buoys,
including wave height, water temperature, wind, and atmospheric data.
"""

from datetime import datetime
from typing import Any

import httpx


class AsyncBuoyClient:
    """Async client for accessing KMA Marine Meteorological Buoy data.

    Provides access to marine observation data including:
    - Wave height, period, and direction
    - Water temperature
    - Wind direction and speed
    - Atmospheric pressure and humidity
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize the Buoy client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncBuoyClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make an API request.

        Args:
            endpoint: API endpoint name
            params: Query parameters

        Returns:
            JSON response as dictionary
        """
        params['authKey'] = self.auth_key
        url = f'{self.BASE_URL}/{endpoint}'
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_buoy_data(self, tm: str | datetime, stn: int | str = 0) -> dict[str, Any]:
        """Get marine buoy observation data for a specific time.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, default: 0)

        Returns:
            Marine buoy observation data

        Example:
            >>> async with AsyncBuoyClient('your_api_key')
            >>> ...     data = await client.get_buoy_data('202501011200', stn=0)
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_buoy.php', params)

    async def get_buoy_period(
        self, tm1: str | datetime, tm2: str | datetime, stn: int | str = 0
    ) -> dict[str, Any]:
        """Get marine buoy observation data for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, default: 0)

        Returns:
            Marine buoy observation data for the period

        Example:
            >>> async with AsyncBuoyClient('your_api_key')
            >>> ...     data = await client.get_buoy_period('202501010000', '202501020000', stn=0)
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_buoy2.php', params)

    async def get_comprehensive_marine_data(
        self, tm: str | datetime, stn: int | str = 0
    ) -> dict[str, Any]:
        """Get comprehensive marine observation data.

        Includes wave height, period, direction, water temperature,
        wind data from dual sensors, and atmospheric data.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, default: 0)

        Returns:
            Comprehensive marine observation data

        Example:
            >>> async with AsyncBuoyClient('your_api_key')
            >>> ...     data = await client.get_comprehensive_marine_data('202501011200')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('sea_obs.php', params)
