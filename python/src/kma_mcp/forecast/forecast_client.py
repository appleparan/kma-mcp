"""KMA Weather Forecast API client.

This module provides a client for accessing the Korea Meteorological Administration's
Weather Forecast (예보) API for weather predictions.

Weather forecasts provide predicted meteorological conditions for
planning and decision-making.
"""

from datetime import datetime
from typing import Any

import httpx


class ForecastClient:
    """Client for KMA Weather Forecast API.

    The Weather Forecast system provides predicted meteorological
    conditions including temperature, precipitation probability,
    sky conditions, and wind for various time ranges.

    This client implements short-term forecast endpoints from the
    official KMA API Hub documentation.
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

    # ==================== Short-term Forecast (단기예보) ====================

    def get_short_term_region(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get short-term forecast region data.

        Documented endpoint: fct_shrt_reg.php
        Reference: API_ENDPOINT_Forecast.md line 28-43

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time in 'YYYYMMDDHHmm' format or datetime object.
                  None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Short-term forecast region data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> # Get most recent forecast
            >>> data = client.get_short_term_region(tmfc='0')
            >>> # Get forecast for specific period
            >>> data = client.get_short_term_region(
            ...     tmfc1='2013121106', tmfc2='2013121118'
            ... )
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if stn is not None:
            params['stn'] = stn
        if reg is not None:
            params['reg'] = reg

        if tmfc is not None:
            if isinstance(tmfc, datetime):
                tmfc = tmfc.strftime('%Y%m%d%H%M')
            params['tmfc'] = tmfc

        if tmfc1 is not None:
            if isinstance(tmfc1, datetime):
                tmfc1 = tmfc1.strftime('%Y%m%d%H%M')
            params['tmfc1'] = tmfc1

        if tmfc2 is not None:
            if isinstance(tmfc2, datetime):
                tmfc2 = tmfc2.strftime('%Y%m%d%H%M')
            params['tmfc2'] = tmfc2

        if tmef1 is not None:
            if isinstance(tmef1, datetime):
                tmef1 = tmef1.strftime('%Y%m%d%H%M')
            params['tmef1'] = tmef1

        if tmef2 is not None:
            if isinstance(tmef2, datetime):
                tmef2 = tmef2.strftime('%Y%m%d%H%M')
            params['tmef2'] = tmef2

        return self._make_request('fct_shrt_reg.php', params)

    def get_short_term_overview(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get short-term forecast overview (개황).

        Documented endpoint: fct_afs_ds.php
        Reference: API_ENDPOINT_Forecast.md line 46-61

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Short-term forecast overview data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_short_term_overview(
            ...     tmfc1='2013121106', tmfc2='2013121118'
            ... )
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if stn is not None:
            params['stn'] = stn
        if reg is not None:
            params['reg'] = reg

        if tmfc is not None:
            if isinstance(tmfc, datetime):
                tmfc = tmfc.strftime('%Y%m%d%H%M')
            params['tmfc'] = tmfc

        if tmfc1 is not None:
            if isinstance(tmfc1, datetime):
                tmfc1 = tmfc1.strftime('%Y%m%d%H%M')
            params['tmfc1'] = tmfc1

        if tmfc2 is not None:
            if isinstance(tmfc2, datetime):
                tmfc2 = tmfc2.strftime('%Y%m%d%H%M')
            params['tmfc2'] = tmfc2

        if tmef1 is not None:
            if isinstance(tmef1, datetime):
                tmef1 = tmef1.strftime('%Y%m%d%H%M')
            params['tmef1'] = tmef1

        if tmef2 is not None:
            if isinstance(tmef2, datetime):
                tmef2 = tmef2.strftime('%Y%m%d%H%M')
            params['tmef2'] = tmef2

        return self._make_request('fct_afs_ds.php', params)

    def get_short_term_land(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get short-term land forecast (육상예보).

        Documented endpoint: fct_afs_dl.php
        Reference: API_ENDPOINT_Forecast.md line 64-79

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Short-term land forecast data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_short_term_land(
            ...     reg='', tmfc1='2013121106', tmfc2='2013121118'
            ... )
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if stn is not None:
            params['stn'] = stn
        if reg is not None:
            params['reg'] = reg

        if tmfc is not None:
            if isinstance(tmfc, datetime):
                tmfc = tmfc.strftime('%Y%m%d%H%M')
            params['tmfc'] = tmfc

        if tmfc1 is not None:
            if isinstance(tmfc1, datetime):
                tmfc1 = tmfc1.strftime('%Y%m%d%H%M')
            params['tmfc1'] = tmfc1

        if tmfc2 is not None:
            if isinstance(tmfc2, datetime):
                tmfc2 = tmfc2.strftime('%Y%m%d%H%M')
            params['tmfc2'] = tmfc2

        if tmef1 is not None:
            if isinstance(tmef1, datetime):
                tmef1 = tmef1.strftime('%Y%m%d%H%M')
            params['tmef1'] = tmef1

        if tmef2 is not None:
            if isinstance(tmef2, datetime):
                tmef2 = tmef2.strftime('%Y%m%d%H%M')
            params['tmef2'] = tmef2

        return self._make_request('fct_afs_dl.php', params)

    def get_short_term_land_v2(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get short-term land forecast v2 (육상예보 version 2).

        Documented endpoint: fct_afs_dl2.php
        Reference: API_ENDPOINT_Forecast.md line 82-97

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Short-term land forecast data (v2)

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_short_term_land_v2(
            ...     reg='', tmfc1='2020052505', tmfc2='2020052517'
            ... )
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if stn is not None:
            params['stn'] = stn
        if reg is not None:
            params['reg'] = reg

        if tmfc is not None:
            if isinstance(tmfc, datetime):
                tmfc = tmfc.strftime('%Y%m%d%H%M')
            params['tmfc'] = tmfc

        if tmfc1 is not None:
            if isinstance(tmfc1, datetime):
                tmfc1 = tmfc1.strftime('%Y%m%d%H%M')
            params['tmfc1'] = tmfc1

        if tmfc2 is not None:
            if isinstance(tmfc2, datetime):
                tmfc2 = tmfc2.strftime('%Y%m%d%H%M')
            params['tmfc2'] = tmfc2

        if tmef1 is not None:
            if isinstance(tmef1, datetime):
                tmef1 = tmef1.strftime('%Y%m%d%H%M')
            params['tmef1'] = tmef1

        if tmef2 is not None:
            if isinstance(tmef2, datetime):
                tmef2 = tmef2.strftime('%Y%m%d%H%M')
            params['tmef2'] = tmef2

        return self._make_request('fct_afs_dl2.php', params)

    def get_short_term_sea(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get short-term sea forecast (해상예보).

        Documented endpoint: fct_afs_do.php
        Reference: API_ENDPOINT_Forecast.md line 100-115

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Short-term sea forecast data

        Example:
            >>> client = ForecastClient('your_auth_key')
            >>> data = client.get_short_term_sea(
            ...     reg='', tmfc1='2013121106', tmfc2='2013121118'
            ... )
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if stn is not None:
            params['stn'] = stn
        if reg is not None:
            params['reg'] = reg

        if tmfc is not None:
            if isinstance(tmfc, datetime):
                tmfc = tmfc.strftime('%Y%m%d%H%M')
            params['tmfc'] = tmfc

        if tmfc1 is not None:
            if isinstance(tmfc1, datetime):
                tmfc1 = tmfc1.strftime('%Y%m%d%H%M')
            params['tmfc1'] = tmfc1

        if tmfc2 is not None:
            if isinstance(tmfc2, datetime):
                tmfc2 = tmfc2.strftime('%Y%m%d%H%M')
            params['tmfc2'] = tmfc2

        if tmef1 is not None:
            if isinstance(tmef1, datetime):
                tmef1 = tmef1.strftime('%Y%m%d%H%M')
            params['tmef1'] = tmef1

        if tmef2 is not None:
            if isinstance(tmef2, datetime):
                tmef2 = tmef2.strftime('%Y%m%d%H%M')
            params['tmef2'] = tmef2

        return self._make_request('fct_afs_do.php', params)

    # ==================== Legacy Methods (Deprecated) ====================
    # These methods use undocumented endpoints and are kept for backward compatibility

    def get_short_term_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get short-term weather forecast (DEPRECATED - undocumented endpoint).

        **DEPRECATED**: This method uses an undocumented endpoint (kma_sfcfct.php).
        Use get_short_term_region(), get_short_term_land(), or get_short_term_sea()
        instead for documented API endpoints.

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Short-term weather forecast data
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_sfcfct.php', params)

    def get_medium_term_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get medium-term weather forecast (DEPRECATED - undocumented endpoint).

        **DEPRECATED**: This method uses an undocumented endpoint (kma_mtfcst.php).
        Medium-term forecast methods will be implemented in future updates.

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Medium-term weather forecast data
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_mtfcst.php', params)

    def get_weekly_forecast(
        self,
        tm_fc: str,
        stn: int | str = 0,
    ) -> dict[str, Any]:
        """Get weekly weather forecast (DEPRECATED - undocumented endpoint).

        **DEPRECATED**: This method uses an undocumented endpoint (kma_wkfcst.php).
        Use documented medium-term forecast methods instead (to be implemented).

        Args:
            tm_fc: Forecast time in 'YYYYMMDDHHmm' format
            stn: Station/region code (0 for all regions)

        Returns:
            Weekly weather forecast data
        """
        params = {'tm_fc': tm_fc, 'stn': str(stn), 'help': '0'}
        return self._make_request('kma_wkfcst.php', params)
