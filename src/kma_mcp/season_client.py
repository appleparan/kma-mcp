"""KMA Seasonal Observation API client.

This module provides a client for accessing the Korea Meteorological Administration's
Seasonal Observation (계절관측) API for phenological observations.

Seasonal observations monitor phenological events such as cherry blossom
flowering, autumn foliage, and other seasonal biological indicators.
"""

from typing import Any

import httpx


class SeasonClient:
    """Client for KMA Seasonal Observation API.

    The Seasonal observation system monitors phenological events such as
    cherry blossom flowering, autumn foliage, and other seasonal biological
    indicators for climate analysis and public information.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize Seasonal Observation client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'SeasonClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to Seasonal Observation API.

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

    def get_observation_data(
        self,
        year: int | str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get seasonal observation data for a specific year.

        Args:
            year: Year in 'YYYY' format
            stn: Station number (0 for all stations)

        Returns:
            Seasonal observation data

        Example:
            >>> client = SeasonClient('your_auth_key')
            >>> data = client.get_observation_data(2025)
            >>> # Or with station filter
            >>> data = client.get_observation_data(2025, stn=108)
        """
        params = {'year': str(year), 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_season.php', params)

    def get_observation_period(
        self,
        start_year: int | str,
        end_year: int | str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get seasonal observation data for a year range.

        Args:
            start_year: Start year in 'YYYY' format
            end_year: End year in 'YYYY' format
            stn: Station number (0 for all stations)

        Returns:
            Seasonal observation data for the period

        Example:
            >>> client = SeasonClient('your_auth_key')
            >>> data = client.get_observation_period(2020, 2025)
        """
        params = {'year1': str(start_year), 'year2': str(end_year), 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_season_2.php', params)
