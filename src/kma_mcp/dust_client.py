"""KMA Yellow Dust (PM10) Observation API client.

This module provides a client for accessing the Korea Meteorological Administration's
Yellow Dust (황사관측) API for PM10 particle observations.

Yellow dust observations monitor Asian dust storms and particulate matter
concentrations for air quality assessment and public health alerts.
"""

from datetime import datetime
from typing import Any

import httpx


class DustClient:
    """Client for KMA Yellow Dust (PM10) Observation API.

    The Yellow Dust observation system monitors PM10 particulate matter
    concentrations from Asian dust storms and other sources, providing
    critical air quality data for public health protection.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Yellow Dust client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'DustClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Yellow Dust API.

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
        """Get hourly PM10 observation data for a single time.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly PM10 observation data

        Example:
            >>> client = DustClient('your_auth_key')
            >>> data = client.get_hourly_data('202501011200')
            >>> # Or using datetime
            >>> from datetime import datetime
            >>> data = client.get_hourly_data(datetime(2025, 1, 1, 12, 0))
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_pm10.php', params)

    def get_hourly_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get hourly PM10 observation data for a time period.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Hourly PM10 observation data for the period

        Example:
            >>> client = DustClient('your_auth_key')
            >>> data = client.get_hourly_period('202501010000', '202501020000')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_pm10_2.php', params)

    def get_daily_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily PM10 observation data for a single day.

        Args:
            tm: Date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily PM10 observation data

        Example:
            >>> client = DustClient('your_auth_key')
            >>> data = client.get_daily_data('20250101')
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d')

        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_pm10_day.php', params)

    def get_daily_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily PM10 observation data for a time period.

        Args:
            tm1: Start date in 'YYYYMMDD' format or datetime object
            tm2: End date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            Daily PM10 observation data for the period

        Example:
            >>> client = DustClient('your_auth_key')
            >>> data = client.get_daily_period('20250101', '20250131')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_pm10_day2.php', params)
