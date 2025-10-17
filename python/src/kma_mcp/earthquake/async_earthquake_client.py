"""Async client for KMA Earthquake Monitoring API.

This module provides access to earthquake information including magnitude,
epicenter location, depth, and seismic intensity data.
"""

from datetime import UTC, datetime
from typing import Any

import httpx


class AsyncEarthquakeClient:
    """Async client for accessing KMA Earthquake monitoring data.

    Provides access to:
    - Recent earthquake information
    - Earthquake lists for time periods
    - Earthquake bulletin messages
    - Domestic and foreign earthquake data
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize the Earthquake client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncEarthquakeClient':
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

    async def get_recent_earthquake(
        self, tm: str | datetime | None = None, disp: int = 0
    ) -> dict[str, Any]:
        """Get the most recent earthquake information.

        Args:
            tm: Reference time in 'YYYYMMDDHHmm' format or datetime object
                (default: None for current time)
            disp: Output format - 0/1/2 (default: 0)

        Returns:
            Most recent earthquake data or earthquakes within past 10 days

        Example:
            >>> async with AsyncEarthquakeClient('your_api_key')
            >>> ...     data = await client.get_recent_earthquake()
        """
        if tm is None:
            tm = datetime.now(UTC).strftime('%Y%m%d%H%M')
        elif isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'disp': str(disp), 'help': '0'}
        return await self._make_request('eqk_now.php', params)

    async def get_earthquake_list(
        self, tm1: str | datetime, tm2: str | datetime, disp: int = 0
    ) -> dict[str, Any]:
        """Get earthquake list for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            disp: Output format - 0/1/2 (default: 0)

        Returns:
            List of earthquakes during the period

        Example:
            >>> async with AsyncEarthquakeClient('your_api_key')
            >>> ...     data = await client.get_earthquake_list('202501010000', '202501310000')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'disp': str(disp), 'help': '0'}
        return await self._make_request('eqk_list.php', params)
