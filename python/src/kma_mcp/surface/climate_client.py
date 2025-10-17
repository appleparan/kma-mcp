"""KMA Climate Statistics API client.

This module provides a client for accessing the Korea Meteorological Administration's
Climate Statistics (기후통계) API for climate normal values and long-term statistics.

Climate normals are calculated over standard 30-year periods and provide reference
values for temperature, precipitation, and other meteorological elements.
"""

from typing import Any

import httpx


class ClimateClient:
    """Client for KMA Climate Statistics API.

    The Climate Statistics API provides long-term climate normal values
    calculated over 30-year reference periods (e.g., 1991-2020).
    Available data includes temperature, precipitation, humidity, wind, and more.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Climate Statistics client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'ClimateClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Climate Statistics API.

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

    def get_daily_normals(
        self,
        start_month: int,
        start_day: int,
        end_month: int,
        end_day: int,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get daily climate normal values for a date range.

        Args:
            start_month: Start month (1-12)
            start_day: Start day (1-31)
            end_month: End month (1-12)
            end_day: End day (1-31)
            stn: Station number (0 for all stations)

        Returns:
            Daily climate normal values

        Example:
            >>> client = ClimateClient('your_auth_key')
            >>> # Get normals for January 1-31
            >>> data = client.get_daily_normals(1, 1, 1, 31)
        """
        params = {
            'stn': str(stn),
            'mm1': str(start_month).zfill(2),
            'dd1': str(start_day).zfill(2),
            'mm2': str(end_month).zfill(2),
            'dd2': str(end_day).zfill(2),
            'help': '0',
        }
        return self._make_request('kma_clm_daily.php', params)

    def get_ten_day_normals(
        self,
        start_month: int,
        start_period: int,
        end_month: int,
        end_period: int,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get 10-day (dekad) climate normal values.

        Each month is divided into three 10-day periods:
        - Period 1: Days 1-10
        - Period 2: Days 11-20
        - Period 3: Days 21-end of month

        Args:
            start_month: Start month (1-12)
            start_period: Start period (1-3)
            end_month: End month (1-12)
            end_period: End period (1-3)
            stn: Station number (0 for all stations)

        Returns:
            10-day climate normal values

        Example:
            >>> client = ClimateClient('your_auth_key')
            >>> # Get normals for first 10-day period of January
            >>> data = client.get_ten_day_normals(1, 1, 1, 1)
        """
        params = {
            'stn': str(stn),
            'mm1': str(start_month).zfill(2),
            'dd1': str(start_period),
            'mm2': str(end_month).zfill(2),
            'dd2': str(end_period),
            'help': '0',
        }
        return self._make_request('kma_clm_tenday.php', params)

    def get_monthly_normals(
        self,
        start_month: int,
        end_month: int,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get monthly climate normal values.

        Args:
            start_month: Start month (1-12)
            end_month: End month (1-12)
            stn: Station number (0 for all stations)

        Returns:
            Monthly climate normal values

        Example:
            >>> client = ClimateClient('your_auth_key')
            >>> # Get normals for entire year
            >>> data = client.get_monthly_normals(1, 12)
        """
        params = {
            'stn': str(stn),
            'mm1': str(start_month).zfill(2),
            'mm2': str(end_month).zfill(2),
            'help': '0',
        }
        return self._make_request('kma_clm_month.php', params)

    def get_annual_normals(
        self,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get annual climate normal values.

        Args:
            stn: Station number (0 for all stations)

        Returns:
            Annual climate normal values

        Example:
            >>> client = ClimateClient('your_auth_key')
            >>> data = client.get_annual_normals()
        """
        params = {
            'stn': str(stn),
            'help': '0',
        }
        return self._make_request('kma_clm_year.php', params)

    def get_normals_by_period(
        self,
        period_type: str,
        start_month: int | None = None,
        start_day: int | None = None,
        end_month: int | None = None,
        end_day: int | None = None,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get climate normals with flexible period specification.

        Args:
            period_type: Type of period ('daily', 'tenday', 'monthly', 'annual')
            start_month: Start month (required for daily, tenday, monthly)
            start_day: Start day (required for daily) or period (1-3 for tenday)
            end_month: End month (required for daily, tenday, monthly)
            end_day: End day (required for daily) or period (1-3 for tenday)
            stn: Station number (0 for all stations)

        Returns:
            Climate normal values for the specified period

        Raises:
            ValueError: If required parameters are missing for the period type

        Example:
            >>> client = ClimateClient('your_auth_key')
            >>> data = client.get_normals_by_period('monthly', 1, None, 12, None)
        """
        if period_type == 'daily':
            if None in (start_month, start_day, end_month, end_day):
                msg = 'Daily normals require start_month, start_day, end_month, end_day'
                raise ValueError(msg)
            return self.get_daily_normals(start_month, start_day, end_month, end_day, stn)
        elif period_type == 'tenday':
            if None in (start_month, start_day, end_month, end_day):
                msg = 'Ten-day normals require start_month, start_period, end_month, end_period'
                raise ValueError(msg)
            return self.get_ten_day_normals(start_month, start_day, end_month, end_day, stn)
        elif period_type == 'monthly':
            if None in (start_month, end_month):
                msg = 'Monthly normals require start_month and end_month'
                raise ValueError(msg)
            return self.get_monthly_normals(start_month, end_month, stn)
        elif period_type == 'annual':
            return self.get_annual_normals(stn)
        else:
            msg = (
                f'Invalid period_type: {period_type}. '
                f"Must be 'daily', 'tenday', 'monthly', or 'annual'"
            )
            raise ValueError(msg)
