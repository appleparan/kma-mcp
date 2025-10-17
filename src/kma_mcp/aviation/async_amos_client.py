"""Async client for KMA Aviation Meteorology AMOS API.

AMOS (Aerodrome Meteorological Observation Station) provides weather
observations from airports and aerodromes for aviation safety.
"""

from typing import Any

import httpx


class AsyncAMOSClient:
    """Async client for accessing KMA Aviation Meteorology AMOS data.

    Provides access to:
    - Airport weather observations
    - Aerodrome meteorological data
    - Aviation-specific weather parameters
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize AMOS client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncAMOSClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make an API request."""
        params['authKey'] = self.auth_key
        url = f'{self.BASE_URL}/{endpoint}'
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_airport_observations(
        self,
        tm: str,
        dtm: int = 60,
    ) -> dict[str, Any]:
        """Get aerodrome meteorological observations.

        AMOS provides weather observations from airports and aerodromes
        for aviation operations and safety.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            dtm: Data time range in minutes before tm (default: 60)
                 Typical values: 30, 60, 120, 180

        Returns:
            Airport weather observation data

        Example:
            >>> with AMOSClient('api_key') as client:
            >>>     data = client.get_airport_observations('202501011200', dtm=60)
        """
        params = {'tm': tm, 'dtm': dtm, 'help': '0'}
        return await self._make_request('amos.php', params)

    async def get_amdar_data(
        self,
        tm1: str,
        tm2: str,
        st: str = 'E',
    ) -> dict[str, Any]:
        """Get AMDAR aircraft meteorological data.

        AMDAR (Aircraft Meteorological Data Relay) provides in-flight
        weather observations from commercial aircraft equipped with
        meteorological sensors.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format
            tm2: End time in 'YYYYMMDDHHmm' format
            st: Station type filter (default: 'E')
                Options: 'E' (all), specific station codes

        Returns:
            AMDAR aircraft meteorological data

        Example:
            >>> with AMOSClient('api_key') as client:
            >>>     data = client.get_amdar_data(
            >>>         '202501011200', '202501011400', st='E'
            >>>     )
        """
        params = {'tm1': tm1, 'tm2': tm2, 'st': st, 'help': '0'}
        return await self._make_request('amdar_kma.php', params)
