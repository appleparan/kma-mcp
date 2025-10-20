"""KMA ASOS (Automated Synoptic Observing System) API client.

This module provides a client for accessing the Korea Meteorological Administration's
ASOS (종관기상관측) API for surface weather observations.
"""

from datetime import datetime
from typing import Any, Literal

import httpx


class ASOSClient:
    """Client for KMA ASOS API.

    The ASOS system collects atmospheric data at standardized times across all
    observation stations, measuring temperature, precipitation, pressure, humidity,
    wind direction/speed, solar radiation, sunshine duration, and snow depth.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize ASOS client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'ASOSClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to ASOS API.

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
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_hourly_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly observation data for a single time.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, or specific station number)

        Returns:
            Hourly observation data

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> data = client.get_hourly_data('202501011200')
            >>> # Or using datetime
            >>> from datetime import datetime
            >>> data = client.get_hourly_data(datetime(2025, 1, 1, 12, 0))
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_sfctm2.php', params)

    def get_hourly_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly observation data for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
                 (maximum 31 days from tm1)
            stn: Station number (0 for all stations)

        Returns:
            Hourly observation data for the period

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> data = client.get_hourly_period('202501010000', '202501020000')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_sfctm3.php', params)

    def get_daily_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get daily observation data for a single day.

        Args:
            tm: Date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)
            disp: Display option (default: 0)

        Returns:
            Daily observation data

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> data = client.get_daily_data('20250101')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d')

        params = {'tm': tm, 'stn': str(stn), 'disp': str(disp), 'help': '0'}
        return self._make_request('kma_sfcdd.php', params)

    def get_daily_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
        obs: str = '',
        mode: int = 0,
    ) -> dict[str, Any]:
        """Get daily observation data for a time period.

        Args:
            tm1: Start date in 'YYYYMMDD' format or datetime object
            tm2: End date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)
            obs: Observation element code (empty for all)
            mode: Mode option (default: 0)

        Returns:
            Daily observation data for the period

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> data = client.get_daily_period('20250101', '20250131')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d')

        params = {
            'tm1': tm1,
            'tm2': tm2,
            'stn': str(stn),
            'obs': obs,
            'mode': str(mode),
            'help': '0',
        }
        return self._make_request('kma_sfcdd3.php', params)

    def get_element_data(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        obs: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get specific element observation data for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            obs: Observation element code
            stn: Station number (0 for all stations)

        Returns:
            Element-specific observation data

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> # Get temperature data
            >>> data = client.get_element_data('202501010000', '202501020000', 'TA')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'obs': obs, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_sfctm5.php', params)

    def get_normals(
        self,
        norm: Literal['D', 'S', 'M', 'Y'],
        tmst: Literal[1991, 2001, 2011, 2021],
        mm1: int,
        dd1: int,
        mm2: int | None = None,
        dd2: int | None = None,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get climate normal values for a period.

        Documented endpoint: sfc_norm1.php
        Reference: API_ENDPOINT_Surface.md line 91-106

        Args:
            norm: Normal period type:
                - 'D': Daily (일)
                - 'S': 10-day period (순)
                - 'M': Monthly (월)
                - 'Y': Yearly (연)
            tmst: Climate normal period:
                - 1991: 1961-1990
                - 2001: 1971-2000
                - 2011: 1981-2010
                - 2021: 1991-2020
            mm1: Start month
            dd1: Start day (for 'S' type: 100=early, 200=middle, 300=late)
            mm2: End month (optional, defaults to mm1)
            dd2: End day (optional, defaults to dd1)
            stn: Station number (0 for all stations)

        Returns:
            Climate normal values for the period

        Example:
            >>> client = ASOSClient('your_auth_key')
            >>> # Get daily normals for May 1-2
            >>> data = client.get_normals('D', 2021, mm1=5, dd1=1, mm2=5, dd2=2)
            >>> # Get monthly normals for May
            >>> data = client.get_normals('M', 2021, mm1=5, dd1=1)
            >>> # Get 10-day period normals (early May)
            >>> data = client.get_normals('S', 2021, mm1=5, dd1=100)
        """
        if mm2 is None:
            mm2 = mm1
        if dd2 is None:
            dd2 = dd1

        params = {
            'norm': norm,
            'tmst': str(tmst),
            'stn': str(stn),
            'MM1': str(mm1),
            'DD1': str(dd1),
            'MM2': str(mm2),
            'DD2': str(dd2),
            'help': '1',
        }
        return self._make_request('sfc_norm1.php', params)
