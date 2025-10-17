"""Client for KMA Global Meteorology GTS (Global Telecommunication System) API.

Provides access to worldwide meteorological observation data collected through
the WMO Global Telecommunication System.
"""

from typing import Any

import httpx


class GTSClient:
    """Client for accessing KMA Global Meteorology GTS data.

    Provides access to:
    - Global SYNOP observations (surface synoptic reports)
    - Global ship observations (marine weather)
    - Global buoy observations (ocean buoys)
    - Aircraft reports (AIREP)
    """

    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url'

    def __init__(self, auth_key: str, timeout: float = 30.0):
        """Initialize GTS client.

        Args:
            auth_key: KMA API authentication key
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.auth_key = auth_key
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> 'GTSClient':
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

    def get_synop_observations(
        self,
        tm: str,
        dtm: int = 3,
        stn: int = 0,
    ) -> dict[str, Any]:
        """Get global SYNOP surface observations.

        SYNOP reports are surface synoptic observations from land stations
        worldwide, transmitted through the GTS network.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            dtm: Data time range in hours before tm (default: 3)
                 Options: 3, 6, 12, 24
            stn: Station ID (0 for all stations, default: 0)

        Returns:
            Global SYNOP observation data

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_synop_observations('202501011200', dtm=3)
        """
        params = {'tm': tm, 'dtm': dtm, 'stn': stn, 'help': '0'}
        return self._make_request('gts_bufr_syn.php', params)

    def get_ship_observations(
        self,
        tm: str,
        dtm: int = 3,
    ) -> dict[str, Any]:
        """Get global ship observations.

        Ship reports provide marine weather observations from vessels at sea,
        transmitted through the GTS network.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            dtm: Data time range in hours before tm (default: 3)
                 Options: 3, 6, 12, 24

        Returns:
            Global ship observation data

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_ship_observations('202501011200', dtm=6)
        """
        params = {'tm': tm, 'dtm': dtm, 'help': '0'}
        return self._make_request('gts_bufr_ship.php', params)

    def get_buoy_observations(
        self,
        tm: str,
        dtm: int = 3,
        stn: str = '',
    ) -> dict[str, Any]:
        """Get global buoy observations.

        Buoy reports provide marine weather observations from moored and
        drifting buoys worldwide, transmitted through the GTS network.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            dtm: Data time range in hours before tm (default: 3)
                 Options: 3, 6, 12, 24
            stn: Buoy station ID (empty string for all, default: '')

        Returns:
            Global buoy observation data

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_buoy_observations('202501011200', dtm=3)
        """
        params = {'tm': tm, 'dtm': dtm, 'stn': stn, 'help': '0'}
        return self._make_request('gts_bufr_buoy.php', params)

    def get_aircraft_reports(
        self,
        tm: str,
        dtm: int = 60,
        stn: int = 0,
    ) -> dict[str, Any]:
        """Get aircraft meteorological reports (AIREP).

        AIREP provides in-flight weather observations from commercial aircraft,
        transmitted through the GTS network.

        Args:
            tm: Observation time in 'YYYYMMDDHHmm' format
            dtm: Data time range in minutes before tm (default: 60)
                 Note: dtm is in MINUTES for aircraft reports
            stn: Station/aircraft ID (0 for all, default: 0)

        Returns:
            Aircraft meteorological report data

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_aircraft_reports('202501011200', dtm=120)
        """
        params = {'tm': tm, 'dtm': dtm, 'stn': stn, 'help': '0'}
        return self._make_request('gts_airep1.php', params)

    def get_surface_chart(
        self,
        tm: str,
    ) -> dict[str, Any]:
        """Get GTS surface weather chart.

        Surface charts provide synoptic analysis and forecast maps
        distributed through the GTS network.

        Args:
            tm: Chart time in 'YYYYMMDDHHmm' format

        Returns:
            Surface weather chart data/image

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_surface_chart('202501011200')
        """
        params = {'tm': tm, 'help': '0'}
        return self._make_request('gts_cht_sfc.php', params)

    def get_synop_chart(
        self,
        tm: str,
    ) -> dict[str, Any]:
        """Get GTS SYNOP analysis chart.

        SYNOP charts provide surface synoptic analysis maps
        distributed through the GTS network.

        Args:
            tm: Chart time in 'YYYYMMDDHHmm' format

        Returns:
            SYNOP analysis chart data/image

        Example:
            >>> with GTSClient('api_key') as client:
            >>>     data = client.get_synop_chart('202501011200')
        """
        params = {'tm': tm, 'help': '0'}
        return self._make_request('gts_cht_syn.php', params)
