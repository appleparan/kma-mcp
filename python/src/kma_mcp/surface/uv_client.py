"""KMA UV Radiation Observation API client.

This module provides a client for accessing the Korea Meteorological Administration's
UV Radiation (자외선관측) API for ultraviolet index observations.

UV radiation observations monitor ultraviolet radiation levels for
public health protection and sun safety guidance.
"""

from datetime import datetime
from typing import Any

import httpx


class UVClient:
    """Client for KMA UV Radiation Observation API.

    The UV observation system monitors ultraviolet radiation levels
    and provides UV index data for public health protection and
    sun safety recommendations.
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0) -> None:
        """Initialize UV Radiation client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'UVClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make HTTP request to UV Radiation API.

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
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get UV radiation observation data for a single time.

        This is the only documented API endpoint for UV observations.
        UV observations monitor ultraviolet A and erythema B radiation levels.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Returns:
            UV radiation observation data

        Example:
            >>> client = UVClient('your_auth_key')
            >>> data = client.get_observation_data('202203211500')
            >>> # Or using datetime
            >>> from datetime import datetime
            >>> data = client.get_observation_data(datetime(2022, 3, 21, 15, 0))

        Note:
            - UV observation stations: Anmyeondo, Gosan, Ulleungdo, Seoul,
              Pohang, Mokpo, Gangneung (7 stations)
            - Measures UVA (320-400nm) and erythema UVB (280-320nm)
            - Data available from January 1994 to present
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params = {'tm': tm, 'stn': str(stn), 'help': '1'}
        return self._make_request('kma_sfctm_uv.php', params)

    # Legacy methods - kept for backward compatibility but raise NotImplementedError
    def get_hourly_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Legacy method - not documented in official API.

        Args:
            tm: Time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations)

        Raises:
            NotImplementedError: This endpoint is not documented in the official KMA API.
                Use get_observation_data() instead.
        """
        msg = (
            'get_hourly_data() is not documented in the official KMA API. '
            'Use get_observation_data(tm, stn) instead for UV observation data.'
        )
        raise NotImplementedError(msg)

    def get_hourly_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Legacy method - not documented in official API.

        Args:
            tm1: Start time
            tm2: End time
            stn: Station number

        Raises:
            NotImplementedError: This endpoint is not documented in the official KMA API.
        """
        msg = (
            'get_hourly_period() is not documented in the official KMA API. '
            'Period queries may need to be implemented using multiple calls to '
            'get_observation_data().'
        )
        raise NotImplementedError(msg)

    def get_daily_data(
        self,
        tm: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Legacy method - not documented in official API.

        Args:
            tm: Date
            stn: Station number

        Raises:
            NotImplementedError: This endpoint is not documented in the official KMA API.
        """
        msg = 'get_daily_data() is not documented in the official KMA API.'
        raise NotImplementedError(msg)

    def get_daily_period(
        self,
        tm1: str | datetime,
        tm2: str | datetime,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Legacy method - not documented in official API.

        Args:
            tm1: Start date
            tm2: End date
            stn: Station number

        Raises:
            NotImplementedError: This endpoint is not documented in the official KMA API.
        """
        msg = 'get_daily_period() is not documented in the official KMA API.'
        raise NotImplementedError(msg)
