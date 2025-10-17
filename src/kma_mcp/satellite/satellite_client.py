"""Client for KMA Satellite Data API.

This module provides access to GK2A satellite imagery and data products.
"""

from typing import Any

import httpx


class SatelliteClient:
    """Client for accessing KMA GK2A Satellite data.

    Provides access to:
    - Satellite file listings
    - Level 1B and Level 2 products
    - Various satellite imagery channels
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 60.0):
        """Initialize Satellite client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 60.0, longer for large files)
        """
        self.auth_key = auth_key
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'SatelliteClient':
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

    def get_satellite_file_list(
        self,
        sat: str = 'GK2A',
        vars: str = 'L1B',  # noqa: A002
        area: str = 'FD',
        fmt: str = 'NetCDF',
        tm: str | None = None,
    ) -> dict[str, Any]:
        """Get list of available satellite files.

        Args:
            sat: Satellite identifier (default: 'GK2A')
            vars: Variable/product type (default: 'L1B')
                  Options: L1B, L2, etc.
            area: Region code (default: 'FD' for Full Disk)
                  Options: FD, KO (Korea), EA (East Asia), etc.
            fmt: File format (default: 'NetCDF')
            tm: Time filter in 'YYYYMMDDHHmm' format (optional)

        Returns:
            List of available satellite files

        Example:
            >>> client = SatelliteClient('your_api_key')
            >>> files = client.get_satellite_file_list(area='KO')
        """
        params: dict[str, Any] = {
            'sat': sat,
            'vars': vars,
            'area': area,
            'fmt': fmt,
            'help': '0',
        }
        if tm:
            params['tm'] = tm

        return self._make_request('sat_file_list.php', params)

    def get_satellite_imagery(
        self,
        level: str,
        product: str,
        area: str,
        tm: str,
    ) -> dict[str, Any]:
        """Get satellite imagery data.

        Args:
            level: Data level ('l1b' or 'l2')
            product: Product type/channel
                     For L1B: NR016, SW038, etc. (16 channels)
                     For L2: CI (Cloud Imagery), SST, etc.
            area: Area code (FD, KO, EA, ELA, TP)
            tm: Time in 'YYYYMMDDHHmm' format

        Returns:
            Satellite imagery data

        Example:
            >>> client = SatelliteClient('your_api_key')
            >>> data = client.get_satellite_imagery('l1b', 'NR016', 'KO', '202501011200')
        """
        params = {
            'lvl': level,
            'dat': product,
            'are': area,
            'tm': tm,
            'typ': 'img',
            'help': '0',
        }
        return self._make_request('sat_file_down2.php', params)
