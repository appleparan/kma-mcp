"""KMA AWS (Automated Weather Station) API client.

This module provides a client for accessing the Korea Meteorological Administration's
AWS (방재기상관측) API for automated weather station observations.

AWS provides real-time weather data from automated weather stations focused on
disaster prevention and monitoring, with more stations than ASOS.
"""

from datetime import datetime
from typing import Any

import httpx


class AWSClient:
    """Client for KMA AWS API.

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
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'AWSClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(
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
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_minutely_data(
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
            >>> client = AWSClient('your_auth_key')
            >>> # Get data for a specific time
            >>> data = client.get_minutely_data(tm2='202302010900')
            >>> # Get data for a period
            >>> data = client.get_minutely_data(tm1='202302010800', tm2='202302010900')
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

        return self._make_request('nph-aws2_min', params, use_cgi=True)

    def get_land_surface_temperature(
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
            >>> client = AWSClient('your_auth_key')
            >>> data = client.get_land_surface_temperature(tm2='202302010900')
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

        return self._make_request('nph-aws2_min_lst', params, use_cgi=True)

    def get_cloud_data(
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
            >>> client = AWSClient('your_auth_key')
            >>> data = client.get_cloud_data(tm2='202302010900', itv=10)
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

        return self._make_request('nph-aws2_min_cloud', params, use_cgi=True)

    def get_cloud_average(
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
            >>> client = AWSClient('your_auth_key')
            >>> data = client.get_cloud_average(tm2='201503221200', itv=10, range_minutes=10)
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

        return self._make_request('nph-aws2_min_ca2', params, use_cgi=True)

    def get_cloud_min_max(
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
            >>> client = AWSClient('your_auth_key')
            >>> data = client.get_cloud_min_max(tm2='201503221200', itv=10, range_minutes=10)
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

        return self._make_request('nph-aws2_min_ca3', params, use_cgi=True)
