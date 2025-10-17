"""Async KMA Seasonal Observation API client.

This module provides a client for accessing the Korea Meteorological Administration's
Seasonal Observation (계절관측) API for phenological observations.

Seasonal observations monitor phenological events such as cherry blossom
flowering, autumn foliage, and other seasonal biological indicators.
"""

from typing import Any

import httpx


class AsyncSeasonClient:
    """Async client for KMA Seasonal Observation API.

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
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncSeasonClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
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
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_observation_data(
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
            >>> async with AsyncSeasonClient('your_auth_key')
            >>> ...     data = await client.get_observation_data(2025)
            >>> # Or with station filter
            >>> ...     data = await client.get_observation_data(2025, stn=108)
        """
        params = {'year': str(year), 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_season.php', params)

    async def get_observation_period(
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
            >>> async with AsyncSeasonClient('your_auth_key')
            >>> ...     data = await client.get_observation_period(2020, 2025)
        """
        params = {'year1': str(start_year), 'year2': str(end_year), 'stn': str(stn), 'help': '0'}
        return await self._make_request('kma_season_2.php', params)
