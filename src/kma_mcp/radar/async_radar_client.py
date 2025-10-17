"""Async KMA Weather Radar API client.

This module provides a client for accessing the Korea Meteorological Administration's
Weather Radar (레이더) API for precipitation detection and monitoring.

Weather radar provides real-time precipitation patterns, intensity,
and movement for nowcasting and severe weather monitoring.
"""

from datetime import datetime
from typing import Any

import httpx


class AsyncRadarClient:
    """Async client for KMA Weather Radar API.

    The Weather Radar system provides real-time precipitation detection
    and monitoring using radar reflectivity data for nowcasting,
    severe weather tracking, and precipitation analysis.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Weather Radar client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncRadarClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Weather Radar API.

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

    async def get_radar_image(
        self,
        tm: str | datetime,
        radar_id: str = 'ALL',
    ) -> dict[str, Any]:
        """Get weather radar image data.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            radar_id: Radar station ID (default: 'ALL' for composite)

        Returns:
            Weather radar image data

        Example:
            >>> async with AsyncRadarClient('your_auth_key')
            >>> ...     data = await client.get_radar_image('202501011200')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'radar': radar_id, 'help': '0'}
        return await self._make_request('kma_radar.php', params)

    async def get_radar_image_sequence(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        radar_id: str = 'ALL',
    ) -> dict[str, Any]:
        """Get weather radar image sequence for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            radar_id: Radar station ID (default: 'ALL' for composite)

        Returns:
            Weather radar image sequence data

        Example:
            >>> async with AsyncRadarClient('your_auth_key')
            >>> ...     data = await client.get_radar_image_sequence('202501011200', '202501011300')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'radar': radar_id, 'help': '0'}
        return await self._make_request('kma_radar_2.php', params)

    async def get_radar_reflectivity(
        self,
        tm: str | datetime,
        x: float,
        y: float,
    ) -> dict[str, Any]:
        """Get radar reflectivity data for a specific location.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            x: Longitude coordinate
            y: Latitude coordinate

        Returns:
            Radar reflectivity data

        Example:
            >>> async with AsyncRadarClient('your_auth_key')
            >>> ...     data = await client.get_radar_reflectivity('202501011200', 127.0, 37.5)
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'x': str(x), 'y': str(y), 'help': '0'}
        return await self._make_request('kma_radar_ref.php', params)
