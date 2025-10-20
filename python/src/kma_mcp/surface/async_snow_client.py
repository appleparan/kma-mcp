"""Async KMA Snow Depth Observation API client.

This module provides a client for accessing the Korea Meteorological Administration's
Snow Depth (적설관측) API for snow accumulation observations.

Snow depth observations monitor snow accumulation for winter weather
analysis, transportation safety, and disaster prevention.
"""

from datetime import datetime
from typing import Any, Literal

import httpx


class AsyncSnowClient:
    """Async client for KMA Snow Depth Observation API.

    The snow depth observation system monitors snow accumulation
    and provides critical data for winter weather analysis,
    transportation safety, and disaster prevention.

    Snow depth types:
        - tot: Total snow depth (적설)
        - day: Daily new snow (일신적설)
        - 3hr: 3-hour new snow (3시간 신적설)
        - 24h: 24-hour new snow (24시간 신적설)
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Snow Depth client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncSnowClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Snow Depth API.

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

    async def get_snow_depth(
        self,
        tm: str | datetime,
        sd_type: Literal['tot', 'day', '3hr', '24h'] = 'tot',
    ) -> dict[str, Any]:
        """Get snow depth observation data.

        Documented endpoint: kma_snow1.php
        Reference: API_ENDPOINT_Surface.md line 1370-1393

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            sd_type: Snow depth type:
                - 'tot': Total snow depth (적설)
                - 'day': Daily new snow (일신적설)
                - '3hr': 3-hour new snow
                - '24h': 24-hour new snow

        Returns:
            Snow depth observation data

        Example:
            >>> async with AsyncSnowClient('your_auth_key') as client:
            ...     # Get total snow depth
            ...     data = await client.get_snow_depth('201412051800', sd_type='tot')
            ...     # Get daily new snow
            ...     data = await client.get_snow_depth('201412051800', sd_type='day')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'sd': sd_type, 'tm': tm, 'help': '1'}
        return await self._make_request('kma_snow1.php', params)

    async def get_snow_period(
        self,
        tm: str | datetime,
        tm_st: str | datetime,
        snow: int = 0,
    ) -> dict[str, Any]:
        """Get snow depth data for a period.

        Documented endpoint: kma_snow2.php
        Reference: API_ENDPOINT_Surface.md line 1394-1399

        Args:
            tm: End time in 'YYYYMMDDHHmm' format or datetime object
            tm_st: Start time in 'YYYYMMDDHHmm' format or datetime object
            snow: Snow parameter (default: 0)

        Returns:
            Snow depth data for the period

        Example:
            >>> async with AsyncSnowClient('your_auth_key') as client:
            ...     data = await client.get_snow_period('201412051800', '201412040100')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')
        if isinstance(tm_st, datetime):
            tm_st = tm_st.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'tm_st': tm_st, 'snow': str(snow), 'help': '1'}
        return await self._make_request('kma_snow2.php', params)

    async def get_max_snow_depth(
        self,
        tm: str | datetime,
        tm_st: str | datetime,
        sd_type: Literal['tot', 'day'] = 'tot',
        stn: int | str = 0,
        snow: int = 0,
    ) -> dict[str, Any]:
        """Get maximum snow depth for a period.

        Documented endpoint: kma_snow_day.php
        Reference: API_ENDPOINT_Surface.md line 1400-1417

        Args:
            tm: End date in 'YYYYMMDD' format or datetime object
            tm_st: Start date in 'YYYYMMDD' format or datetime object
            sd_type: Snow depth type:
                - 'tot': Maximum total snow depth (최심적설)
                - 'day': Maximum daily new snow (최심신적설)
            stn: Station number (0 for all stations)
            snow: Snow parameter (default: 0)

        Returns:
            Maximum snow depth data for the period

        Example:
            >>> async with AsyncSnowClient('your_auth_key') as client:
            ...     # Get maximum total snow depth
            ...     data = await client.get_max_snow_depth('20150131', '20150125', sd_type='tot')
            ...     # Get maximum daily new snow
            ...     data = await client.get_max_snow_depth('20150131', '20150125', sd_type='day')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d')
        if isinstance(tm_st, datetime):
            tm_st = tm_st.strftime('%Y%m%d')

        params = {
            'sd': sd_type,
            'tm': tm,
            'tm_st': tm_st,
            'stn': str(stn),
            'snow': str(snow),
            'help': '1',
        }
        return await self._make_request('kma_snow_day.php', params)

    # Legacy methods - marked as undocumented but may still work
    async def get_hourly_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly snow depth data (undocumented endpoint).

        WARNING: This endpoint (kma_sd.php) is not documented in the official API.
        Consider using get_snow_depth() with the documented kma_snow1.php endpoint.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly snow depth observation data
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_sd.php', params)

    async def get_hourly_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly snow depth data for period (undocumented endpoint).

        WARNING: This endpoint (kma_sd_2.php) is not documented in the official API.
        Consider using get_snow_period() with the documented kma_snow2.php endpoint.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly snow depth observation data for the period
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_sd_2.php', params)

    async def get_daily_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily snow depth data (undocumented endpoint).

        WARNING: This endpoint (kma_sd_day.php) is not documented in the official API.
        Consider using get_max_snow_depth() with the documented kma_snow_day.php endpoint.

        Args:
            tm: Date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily snow depth observation data
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_sd_day.php', params)

    async def get_daily_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily snow depth data for period (undocumented endpoint).

        WARNING: This endpoint (kma_sd_day2.php) is not documented in the official API.
        Consider using get_snow_period() or get_max_snow_depth() with documented endpoints.

        Args:
            tm1: Start date in 'YYYYMMDD' format or datetime object
            tm2: End date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily snow depth observation data for the period
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_sd_day2.php', params)
