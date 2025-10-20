"""Async KMA AWS (Automated Weather Station) API client.

This module provides a client for accessing the Korea Meteorological Administration's
AWS (방재기상관측) API for automated weather station observations.

AWS provides real-time weather data from automated weather stations focused on
disaster prevention and monitoring, with more stations than ASOS.
"""

from datetime import datetime
from typing import Any

import httpx


class AsyncAWSClient:
    """Async client for KMA AWS API.

    The AWS system provides real-time weather observations from automated weather
    stations for disaster prevention purposes. It typically has more observation
    points than ASOS and focuses on real-time monitoring.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'
    CGI_BASE_URL = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize AWS client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncAWSClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(
        self, endpoint: str, params: dict[str, Any], *, use_cgi: bool = False
    ) -> dict[str, Any]:
        """Make HTTP request to AWS API.

        Args:
            endpoint: API endpoint path
            params: Query parameters
            use_cgi: Use CGI base URL instead of regular URL (default: False)

        Returns:
            API response as dictionary

        Raises:
            httpx.HTTPError: If request fails
        """
        params['authKey'] = self.auth_key
        base_url = self.CGI_BASE_URL if use_cgi else self.BASE_URL
        url = f'{base_url}/{endpoint}'
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_minutely_data(
        self,
        tm1: str | datetime | None = None,
        tm2: str | datetime | None = None,
        stn: int | str = 0,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get AWS minutely observation data (documented endpoint).

        Documented endpoint: nph-aws2_min
        Reference: API_ENDPOINT_Surface.md line 241-252

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
                 (optional, defaults to tm2 if not provided)
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
                 (optional, defaults to current time if not provided)
            stn: Station number (0 for all stations)
            disp: Display format:
                  0 = Fixed width format suitable for Fortran (default)
                  1 = Comma-separated format suitable for Excel

        Returns:
            Minutely AWS observation data

        Example:
            >>> async with AsyncAWSClient('your_auth_key') as client:
            ...     # Get data for a specific time
            ...     data = await client.get_minutely_data(tm2='202302010900')
            ...     # Get data for a period
            ...     data = await client.get_minutely_data(tm1='202302010800', tm2='202302010900')
        """
        params: dict[str, Any] = {'stn': str(stn), 'disp': str(disp), 'help': '1'}

        if tm1 is not None:
            if isinstance(tm1, datetime):
                tm1 = tm1.strftime('%Y%m%d%H%M')
            params['tm1'] = tm1

        if tm2 is not None:
            if isinstance(tm2, datetime):
                tm2 = tm2.strftime('%Y%m%d%H%M')
            params['tm2'] = tm2

        return await self._make_request('nph-aws2_min', params, use_cgi=True)

    async def get_land_surface_temperature(
        self,
        tm: str | datetime | None = None,
        tm1: str | datetime | None = None,
        tm2: str | datetime | None = None,
        stn: int | str = 0,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get AWS land surface temperature data (documented endpoint).

        Documented endpoint: nph-aws2_min_lst
        Reference: API_ENDPOINT_Surface.md line 254-266

        Args:
            tm: Time in 'YYYYMMDDHHmm' format (optional, defaults to current time)
            tm1: Start time (optional, defaults to tm2)
            tm2: End time (optional, defaults to current time)
            stn: Station number (0 for all stations)
            disp: Display format (0=Fortran, 1=Excel)

        Returns:
            Land surface temperature data

        Example:
            >>> async with AsyncAWSClient('your_auth_key') as client:
            ...     data = await client.get_land_surface_temperature(tm2='202302010900')
        """
        params: dict[str, Any] = {'stn': str(stn), 'disp': str(disp), 'help': '1'}

        if tm is not None:
            if isinstance(tm, datetime):
                tm = tm.strftime('%Y%m%d%H%M')
            params['tm'] = tm

        if tm1 is not None:
            if isinstance(tm1, datetime):
                tm1 = tm1.strftime('%Y%m%d%H%M')
            params['tm1'] = tm1

        if tm2 is not None:
            if isinstance(tm2, datetime):
                tm2 = tm2.strftime('%Y%m%d%H%M')
            params['tm2'] = tm2

        return await self._make_request('nph-aws2_min_lst', params, use_cgi=True)

    async def get_cloud_data(
        self,
        tm1: str | datetime | None = None,
        tm2: str | datetime | None = None,
        stn: int | str = 0,
        itv: int | None = None,
        sms: int | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get AWS cloud height and amount data (documented endpoint).

        Documented endpoint: nph-aws2_min_cloud
        Reference: API_ENDPOINT_Surface.md line 268-281

        Args:
            tm1: Start time (optional, defaults to tm2)
            tm2: End time (optional, defaults to current time)
            stn: Station number (0 for all stations)
            itv: Time interval in minutes (optional)
            sms: Smoothing flag, 0 or 1 (optional)
            disp: Display format (0=Fortran, 1=Excel)

        Returns:
            Cloud height and amount data

        Example:
            >>> async with AsyncAWSClient('your_auth_key') as client:
            ...     data = await client.get_cloud_data(tm2='202302010900', itv=10)
        """
        params: dict[str, Any] = {'stn': str(stn), 'disp': str(disp), 'help': '1'}

        if tm1 is not None:
            if isinstance(tm1, datetime):
                tm1 = tm1.strftime('%Y%m%d%H%M')
            params['tm1'] = tm1

        if tm2 is not None:
            if isinstance(tm2, datetime):
                tm2 = tm2.strftime('%Y%m%d%H%M')
            params['tm2'] = tm2

        if itv is not None:
            params['itv'] = str(itv)

        if sms is not None:
            params['sms'] = str(sms)

        return await self._make_request('nph-aws2_min_cloud', params, use_cgi=True)

    async def get_cloud_average(
        self,
        tm1: str | datetime | None = None,
        tm2: str | datetime | None = None,
        stn: int | str = 0,
        itv: int = 10,
        range_minutes: int = 10,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get AWS cloud data with period average (documented endpoint).

        Documented endpoint: nph-aws2_min_ca2
        Reference: API_ENDPOINT_Surface.md line 283-297

        Args:
            tm1: Start time (optional, defaults to tm2)
            tm2: End time (optional, defaults to current time)
            stn: Station number (0 for all stations)
            itv: Time interval in minutes (default: 10)
            range_minutes: Accumulation period for average in minutes (default: 10)
            disp: Display format (0=Fortran, 1=Excel)

        Returns:
            Cloud average data for the period

        Example:
            >>> async with AsyncAWSClient('your_auth_key') as client:
            ...     data = await client.get_cloud_average(
            ...         tm2='201503221200', itv=10, range_minutes=10
            ...     )
        """
        params: dict[str, Any] = {
            'stn': str(stn),
            'itv': str(itv),
            'range': str(range_minutes),
            'disp': str(disp),
            'help': '1',
        }

        if tm1 is not None:
            if isinstance(tm1, datetime):
                tm1 = tm1.strftime('%Y%m%d%H%M')
            params['tm1'] = tm1

        if tm2 is not None:
            if isinstance(tm2, datetime):
                tm2 = tm2.strftime('%Y%m%d%H%M')
            params['tm2'] = tm2

        return await self._make_request('nph-aws2_min_ca2', params, use_cgi=True)

    async def get_cloud_min_max(
        self,
        tm1: str | datetime | None = None,
        tm2: str | datetime | None = None,
        stn: int | str = 0,
        itv: int = 10,
        range_minutes: int = 10,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get AWS cloud data with period min/max (documented endpoint).

        Documented endpoint: nph-aws2_min_ca3
        Reference: API_ENDPOINT_Surface.md line 299-312

        Args:
            tm1: Start time (optional, defaults to tm2)
            tm2: End time (optional, defaults to current time)
            stn: Station number (0 for all stations)
            itv: Time interval in minutes (default: 10)
            range_minutes: Accumulation period for min/max in minutes (default: 10)
            disp: Display format (0=Fortran, 1=Excel)

        Returns:
            Cloud min/max data for the period

        Example:
            >>> async with AsyncAWSClient('your_auth_key') as client:
            ...     data = await client.get_cloud_min_max(
            ...         tm2='201503221200', itv=10, range_minutes=10
            ...     )
        """
        params: dict[str, Any] = {
            'stn': str(stn),
            'itv': str(itv),
            'range': str(range_minutes),
            'disp': str(disp),
            'help': '1',
        }

        if tm1 is not None:
            if isinstance(tm1, datetime):
                tm1 = tm1.strftime('%Y%m%d%H%M')
            params['tm1'] = tm1

        if tm2 is not None:
            if isinstance(tm2, datetime):
                tm2 = tm2.strftime('%Y%m%d%H%M')
            params['tm2'] = tm2

        return await self._make_request('nph-aws2_min_ca3', params, use_cgi=True)

    # Legacy methods - marked as undocumented but may still work
    async def get_minutely_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get minutely AWS data for a period (undocumented endpoint).

        WARNING: This endpoint (kma_aws2.php) is not documented in the official API.
        Consider using get_minutely_data() with tm1 and tm2 parameters instead.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Minutely observation data for the period
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws2.php', params)

    async def get_hourly_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly AWS data for a single time (undocumented endpoint).

        WARNING: This endpoint (kma_aws3.php) is not documented in the official API.
        Consider using get_minutely_data() with the documented nph-aws2_min endpoint.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly observation data
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws3.php', params)

    async def get_hourly_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly AWS data for a period (undocumented endpoint).

        WARNING: This endpoint (kma_aws4.php) is not documented in the official API.
        Consider using get_minutely_data() with tm1 and tm2 parameters instead.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly observation data for the period
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws4.php', params)

    async def get_daily_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily AWS data for a single day (undocumented endpoint).

        WARNING: This endpoint (kma_aws5.php) is not documented in the official API.
        Consider using get_minutely_data() for more recent data.

        Args:
            tm: Date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily observation data
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws5.php', params)

    async def get_daily_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily AWS data for a period (undocumented endpoint).

        WARNING: This endpoint (kma_aws6.php) is not documented in the official API.
        Consider using get_minutely_data() with tm1 and tm2 parameters instead.

        Args:
            tm1: Start date in 'YYYYMMDD' format or datetime object
            tm2: End date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily observation data for the period
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_aws6.php', params)
