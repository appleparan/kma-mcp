"""KMA Weather Forecast API client.

This module provides a client for accessing the Korea Meteorological Administration's
Weather Forecast (예보) API for weather predictions.

Weather forecasts provide predicted meteorological conditions for
planning and decision-making.
"""

from typing import Any

import httpx


class ForecastClient:
    """Client for KMA Weather Forecast API.

    The Weather Forecast system provides predicted meteorological
    conditions including temperature, precipitation probability,
    sky conditions, and wind for various time ranges.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Weather Forecast client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'ForecastClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Weather Forecast API.

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

    def get_short_term_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get short-term weather forecast (up to 3 days).

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Short-term weather forecast data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_short_term_forecast('202501011200')
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_sfcfct.php', params)

    def get_medium_term_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get medium-term weather forecast (3-10 days).

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Medium-term weather forecast data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_medium_term_forecast('202501011200')
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_mtfcst.php', params)

    def get_weekly_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get weekly weather forecast.

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Weekly weather forecast data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_weekly_forecast('202501011200')
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_wkfcst.php', params)
