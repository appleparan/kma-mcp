"""KMA Weather Warning API client.

This module provides a client for accessing the Korea Meteorological Administration's
Weather Warning (특보) API for weather alerts and warnings.

Weather warnings provide critical alerts for severe weather conditions
including heavy rain, strong winds, heavy snow, and other hazards.
"""

from typing import Any

import httpx


class WarningClient:
    """Client for KMA Weather Warning API.

    The Weather Warning system provides alerts for severe weather
    conditions to protect life and property from meteorological hazards.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Weather Warning client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'WarningClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Weather Warning API.

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

    def get_current_warnings(
        self,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get current active weather warnings.

        Args:
            stn: Station/region code (0 for all regions)

        Returns:
            Current active weather warnings

        Example:
            >>> client = WarningClient('your_auth_key')
            >>> data = client.get_current_warnings()
        """
        params = {'stn': str(stn), 'help': '0'}
        return self._make_request('kma_wn.php', params)

    def get_warning_history(
        self,
        start_date: str,
        end_date: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get weather warning history for a date range.

        Args:
            start_date: Start date in 'YYYYMMDD' format
            end_date: End date in 'YYYYMMDD' format
            stn: Station/region code (0 for all regions)

        Returns:
            Weather warning history

        Example:
            >>> client = WarningClient('your_auth_key')
            >>> data = client.get_warning_history('20250101', '20250131')
        """
        params = {'tm1': start_date, 'tm2': end_date, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_wn_2.php', params)

    def get_special_weather_report(
        self,
        tm: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get special weather report.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Special weather report data

        Example:
            >>> client = WarningClient('your_auth_key')
            >>> data = client.get_special_weather_report('202501011200')
        """
        params = {'tm': tm, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_swr.php', params)
