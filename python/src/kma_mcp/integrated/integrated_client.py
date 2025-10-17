"""Client for KMA Integrated Meteorology API.

Provides access to integrated meteorological data combining various
observation sources and specialized data products.
"""

from typing import Any

import httpx


class IntegratedClient:
    """Client for accessing KMA Integrated Meteorology data.

    Provides access to:
    - Lightning detection data
    - Wind profiler data
    - Integrated observation products
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize Integrated client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'IntegratedClient':
        """Context manager entry."""
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make an API request."""
        params['authKey'] = self.auth_key
        url = f'{self.BASE_URL}/{endpoint}'
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_lightning_data(
        self,
        tm1: str,
        tm2: str,
    ) -> dict[str, Any]:
        """Get lightning detection data.

        Provides lightning strike location and intensity data from
        the KMA lightning detection network.

        Args:
            tm1: Start time in 'YYYYMMDDHHmm' format
            tm2: End time in 'YYYYMMDDHHmm' format

        Returns:
            Lightning detection data including location and intensity

        Example:
            >>> with IntegratedClient('api_key') as client:
            >>>     data = client.get_lightning_data(
            >>>         '202501011200', '202501011500'
            >>>     )
        """
        params = {'tm1': tm1, 'tm2': tm2, 'help': '0'}
        return self._make_request('lgt_kma_np3.php', params)

    def get_wind_profiler_data(
        self,
        tm: str,
        stn: int = 0,
        mode: str = 'L',
    ) -> dict[str, Any]:
        """Get wind profiler data.

        Wind profilers provide vertical profiles of wind speed and
        direction at various altitudes.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            stn: Station ID (0 for all stations, default: 0)
            mode: Data mode (default: 'L')
                  Options: 'L' (low mode), 'H' (high mode)

        Returns:
            Wind profiler vertical profile data

        Example:
            >>> with IntegratedClient('api_key') as client:
            >>>     data = client.get_wind_profiler_data(
            >>>         '202501011200', stn=0, mode='L'
            >>>     )
        """
        params = {'tm': tm, 'stn': stn, 'mode': mode, 'help': '0'}
        return self._make_request('kma_wpf.php', params)
