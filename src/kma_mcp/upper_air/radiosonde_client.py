"""Client for KMA Upper-Air Observations (Radiosonde) API.

This module provides access to upper-air meteorological observations from radiosondes,
including temperature, humidity, wind data at various altitude levels.
"""

from datetime import datetime
from typing import Any

import httpx


class RadiosondeClient:
    """Client for accessing KMA Upper-Air (Radiosonde) observation data.

    Provides access to atmospheric profiles including:
    - Temperature and dew point at altitude
    - Wind direction and speed at various levels
    - Pressure levels and heights
    - Atmospheric stability indices
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize the Radiosonde client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'RadiosondeClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make an API request.

        Args:
            endpoint: API endpoint name
            params: Query parameters

        Returns:
            JSON response as dictionary
        """
        params['authKey'] = self.auth_key
        url = f'{self.BASE_URL}/{endpoint}'
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_upper_air_data(
        self, tm: str | datetime, stn: int | str = 0, pa: float | None = None
    ) -> dict[str, Any]:
        """Get upper-air (TEMP) radiosonde data.

        Args:
            tm: UTC observation time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, default: 0)
            pa: Pressure level in hPa (optional, e.g., 850, 500, 250)

        Returns:
            Upper-air observation data including temperature, humidity, wind

        Example:
            >>> client = RadiosondeClient('your_api_key')
            >>> data = client.get_upper_air_data('202501010000', stn=47122, pa=850)
        """
        if isinstance(tm, datetime):
            tm = tm.strftime('%Y%m%d%H%M')

        params: dict[str, Any] = {'tm': tm, 'stn': str(stn), 'help': '0'}
        if pa is not None:
            params['pa'] = str(pa)

        return self._make_request('upp_temp.php', params)

    def get_stability_indices(
        self, tm1: str | datetime, tm2: str | datetime, stn: int | str = 0
    ) -> dict[str, Any]:
        """Get atmospheric stability analysis data.

        Provides derived indices for convective forecasting including
        CAPE, K-index, lifted index, and cloud layer information.

        Args:
            tm1: Start UTC time in 'YYYYMMDDHHmm' format or datetime object
            tm2: End UTC time in 'YYYYMMDDHHmm' format or datetime object
            stn: Station number (0 for all stations, default: 0)

        Returns:
            Atmospheric stability indices

        Example:
            >>> client = RadiosondeClient('your_api_key')
            >>> data = client.get_stability_indices('202501010000', '202501020000')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d%H%M')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d%H%M')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return self._make_request('upp_idx.php', params)

    def get_maximum_altitude_data(
        self, tm1: str | datetime, tm2: str | datetime, stn: int | str = 0
    ) -> dict[str, Any]:
        """Get maximum altitude reached during radiosonde ascent.

        Args:
            tm1: Start date in 'YYYYMMDD' format or datetime object
            tm2: End date in 'YYYYMMDD' format or datetime object
            stn: Station number (0 for all stations, default: 0)

        Returns:
            Maximum altitude data including flight time, height, horizontal distance

        Example:
            >>> client = RadiosondeClient('your_api_key')
            >>> data = client.get_maximum_altitude_data('20250101', '20250131')
        """
        if isinstance(tm1, datetime):
            tm1 = tm1.strftime('%Y%m%d')
        if isinstance(tm2, datetime):
            tm2 = tm2.strftime('%Y%m%d')

        params = {'tm1': tm1, 'tm2': tm2, 'stn': str(stn), 'help': '0'}
        return self._make_request('upp_raw_max.php', params)
