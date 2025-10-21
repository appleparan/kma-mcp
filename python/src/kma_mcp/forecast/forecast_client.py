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
    CGI_BASE_URL = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/url'
    OPENAPI_BASE_URL = 'https://apihub.kma.go.kr/api/typ02/openApi'

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

    def _make_request(
        self,
        endpoint: str,
        params: dict[str, Any],
        *,
        use_cgi: bool = False,
        use_openapi: bool = False,
    ) -> dict[str, Any]:
        """Make HTTP request to Weather Forecast API.

        Args:
            endpoint: API endpoint path (for OpenAPI, use format: 'ServiceName/methodName')
            params: Query parameters
            use_cgi: Whether to use CGI base URL (default: False)
            use_openapi: Whether to use OpenAPI base URL (default: False)

        Returns:
            API response as dictionary

        Raises:
            httpx.HTTPError: If request fails
        """
        params['authKey'] = self.auth_key
        if use_openapi:
            base_url = self.OPENAPI_BASE_URL
        elif use_cgi:
            base_url = self.CGI_BASE_URL
        else:
            base_url = self.BASE_URL
        url = f'{base_url}/{endpoint}'
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

    # ============================================================================
    # Category 2: Village Forecast Grid Data (동네예보 격자자료)
    # ============================================================================

    def get_village_short_term_grid(
        self,
        tmfc: str | datetime | None = None,
        tmef: str | datetime | None = None,
        vars: str | None = None,  # noqa: A002
    ) -> dict[str, Any]:
        """Get short-term village forecast grid data (documented endpoint).

        Documented endpoint: nph-dfs_shrt_grd (CGI)

        Provides short-term forecast grid data for village-level forecasts.
        Issued 8 times daily (02, 05, 08, 11, 14, 17, 20, 23 KST).
        Provides hourly forecasts up to 3 days.

        Args:
            tmfc: Forecast issue time in 'YYYYMMDDHHmm' format or datetime object.
                  If None, returns all data. If '0', returns most recent.
                  Issued at 3-hour intervals (02, 05, 08, 11, 14, 17, 20, 23 KST).
            tmef: Forecast valid time in 'YYYYMMDDHHmm' format or datetime object.
                  Hourly data provided up to 3 days ahead.
            vars: Forecast variables (comma-separated).
                  TMP(temperature), TMX(max temp), TMN(min temp),
                  UUU(u-wind), VVV(v-wind), VEC(wind direction), WSD(wind speed),
                  SKY(sky condition), PTY(precipitation type), POP(precipitation probability),
                  PCP(1h precipitation), SNO(1h snowfall), REH(humidity), WAV(wave height)

        Returns:
            Village short-term forecast grid data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_village_short_term_grid(
            ...     tmfc='202402250500',
            ...     tmef='202402250600',
            ...     vars='TMP,SKY,PTY'
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params: dict[str, Any] = {'help': '1'}

        if tmfc is not None:
            params['tmfc'] = tmfc if isinstance(tmfc, str) else self._format_datetime(tmfc)
        if tmef is not None:
            params['tmef'] = tmef if isinstance(tmef, str) else self._format_datetime(tmef)
        if vars is not None:
            params['vars'] = vars

        return self._make_request('nph-dfs_shrt_grd', params, use_cgi=True)

    def get_village_very_short_term_grid(
        self,
        tmfc: str | datetime | None = None,
        tmef: str | datetime | None = None,
        vars: str | None = None,  # noqa: A002
    ) -> dict[str, Any]:
        """Get very short-term village forecast grid data (documented endpoint).

        Documented endpoint: nph-dfs_vsrt_grd (CGI)

        Provides ultra short-term forecast grid data for village-level forecasts.
        Issued every 10 minutes. Provides hourly forecasts up to 6 hours ahead.

        Args:
            tmfc: Forecast issue time in 'YYYYMMDDHHmm' format or datetime object.
                  Issued every 10 minutes.
            tmef: Forecast valid time in 'YYYYMMDDHHmm' format or datetime object.
                  Hourly data up to 6 hours from issue time.
            vars: Forecast variables (comma-separated).
                  T1H(temperature), UUU(u-wind), VVV(v-wind), VEC(wind direction),
                  WSD(wind speed), SKY(sky condition), LGT(lightning),
                  PTY(precipitation type), RN1(1h precipitation), REH(humidity)

        Returns:
            Village very short-term forecast grid data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_village_very_short_term_grid(
            ...     tmfc='202403011010',
            ...     tmef='202403011100',
            ...     vars='T1H,SKY,PTY'
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params: dict[str, Any] = {'help': '1'}

        if tmfc is not None:
            params['tmfc'] = tmfc if isinstance(tmfc, str) else self._format_datetime(tmfc)
        if tmef is not None:
            params['tmef'] = tmef if isinstance(tmef, str) else self._format_datetime(tmef)
        if vars is not None:
            params['vars'] = vars

        return self._make_request('nph-dfs_vsrt_grd', params, use_cgi=True)

    def get_village_observation_grid(
        self,
        tmfc: str | datetime | None = None,
        vars: str | None = None,  # noqa: A002
    ) -> dict[str, Any]:
        """Get village observation grid data (documented endpoint).

        Documented endpoint: nph-dfs_odam_grd (CGI)

        Provides current observation grid data for village-level analysis.
        Since 2024-03-04 10:00, issued every 10 minutes.
        Before that, issued every hour on the hour.

        Args:
            tmfc: Observation time in 'YYYYMMDDHHmm' format or datetime object.
                  Since 2024-03-04 10:00: issued every 10 minutes.
                  Before: issued hourly.
            vars: Observation variables (comma-separated).
                  T1H(temperature), UUU(u-wind), VVV(v-wind), VEC(wind direction),
                  WSD(wind speed), PTY(precipitation type),
                  RN1(1h precipitation), REH(humidity)

        Returns:
            Village observation grid data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_village_observation_grid(
            ...     tmfc='202403051010',
            ...     vars='T1H,RN1,REH'
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params: dict[str, Any] = {'help': '1'}

        if tmfc is not None:
            params['tmfc'] = tmfc if isinstance(tmfc, str) else self._format_datetime(tmfc)
        if vars is not None:
            params['vars'] = vars

        return self._make_request('nph-dfs_odam_grd', params, use_cgi=True)

    def convert_grid_to_coords(
        self,
        x: int,
        y: int,
        *,
        help: int = 1,  # noqa: A002
    ) -> dict[str, Any]:
        """Convert village forecast grid numbers to latitude/longitude coordinates.

        Documented endpoint: nph-dfs_xy_lonlat (CGI)

        Converts village forecast grid coordinates (x, y) to geographic coordinates
        (latitude, longitude).

        Args:
            x: Grid number (east-west direction). Range: 1 ~ 149
            y: Grid number (north-south direction). Range: 1 ~ 253
            help: Show help information. 0=no help, 1=show help (default: 1)

        Returns:
            Latitude and longitude coordinates for the grid point

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> coords = client.convert_grid_to_coords(x=60, y=127)

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params = {'x': str(x), 'y': str(y), 'help': str(help)}
        return self._make_request('nph-dfs_xy_lonlat', params, use_cgi=True)

    def convert_coords_to_grid(
        self,
        lon: float,
        lat: float,
        *,
        help: int = 1,  # noqa: A002
    ) -> dict[str, Any]:
        """Convert latitude/longitude coordinates to village forecast grid numbers.

        Documented endpoint: nph-dfs_xy_lonlat (CGI)

        Converts geographic coordinates (latitude, longitude) to the nearest
        village forecast grid coordinates (x, y).

        Args:
            lon: Longitude. Range: 123.310165 ~ 132.774963
            lat: Latitude. Range: 31.651814 ~ 43.393490
            help: Show help information. 0=no help, 1=show help (default: 1)

        Returns:
            Nearest village forecast grid numbers (x, y)

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> grid = client.convert_coords_to_grid(lon=127.5, lat=36.5)

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params = {'lon': str(lon), 'lat': str(lat), 'help': str(help)}
        return self._make_request('nph-dfs_xy_lonlat', params, use_cgi=True)

    # ============================================================================
    # Category 3: Village Forecast Messages (동네예보 통보문)
    # ============================================================================

    def get_weather_situation(
        self,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
        stn_id: str | None = None,
    ) -> dict[str, Any]:
        """Get weather situation overview messages (documented endpoint).

        Documented endpoint: VilageFcstMsgService/getWthrSituation (OpenAPI)

        Retrieves weather situation overview messages issued by regional offices.
        These messages provide general weather conditions and forecasts.

        Args:
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')
            stn_id: Issuing office code. None for all offices.
                    108=KMA HQ, 109=Seoul, etc. See reference documentation.

        Returns:
            Weather situation overview message data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_weather_situation(stn_id='108', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if stn_id is not None:
            params['stnId'] = stn_id

        return self._make_request('VilageFcstMsgService/getWthrSituation', params, use_openapi=True)

    def get_land_forecast_message(
        self,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
        reg_id: str | None = None,
    ) -> dict[str, Any]:
        """Get land forecast messages (documented endpoint).

        Documented endpoint: VilageFcstMsgService/getLandFcst (OpenAPI)

        Retrieves land forecast messages for specific regions.
        Messages contain detailed weather forecasts for land areas.

        Args:
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')
            reg_id: Forecast region code. None for all regions.
                    11A00101=Baengnyeong, 11B10101=Seoul, 11B20201=Incheon, etc.
                    See reference documentation for full list.

        Returns:
            Land forecast message data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_land_forecast_message(reg_id='11B10101', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if reg_id is not None:
            params['regId'] = reg_id

        return self._make_request('VilageFcstMsgService/getLandFcst', params, use_openapi=True)

    def get_sea_forecast_message(
        self,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
        reg_id: str | None = None,
    ) -> dict[str, Any]:
        """Get sea forecast messages (documented endpoint).

        Documented endpoint: VilageFcstMsgService/getSeaFcst (OpenAPI)

        Retrieves sea/marine forecast messages for specific regions.
        Messages contain detailed weather forecasts for sea areas.

        Args:
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')
            reg_id: Forecast region code. None for all regions.
                    12A20100=West Sea Central, 12B20100=South Sea East, etc.
                    See reference documentation for full list.

        Returns:
            Sea forecast message data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_sea_forecast_message(reg_id='12A20100', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if reg_id is not None:
            params['regId'] = reg_id

        return self._make_request('VilageFcstMsgService/getSeaFcst', params, use_openapi=True)

    # ============================================================================
    # Category 4: Village Forecast API (동네예보 API)
    # ============================================================================

    def get_ultra_short_term_observation(
        self,
        base_date: str,
        base_time: str,
        nx: int,
        ny: int,
        page_no: int = 1,
        num_of_rows: int = 1000,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get ultra short-term observation data (documented endpoint).

        Documented endpoint: VilageFcstInfoService_2.0/getUltraSrtNcst (OpenAPI)

        Retrieves current weather observation data for village forecast grid points.
        Issued every hour on the hour.

        Args:
            base_date: Issue date in YYYYMMDD format (e.g., '20210628')
            base_time: Issue time in HHmm format (e.g., '0600')
            nx: Forecast grid X coordinate (1~149)
            ny: Forecast grid Y coordinate (1~253)
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 1000)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Ultra short-term observation data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_ultra_short_term_observation(
            ...     base_date='20210628',
            ...     base_time='0600',
            ...     nx=55,
            ...     ny=127
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'base_date': base_date,
            'base_time': base_time,
            'nx': str(nx),
            'ny': str(ny),
        }
        return self._make_request(
            'VilageFcstInfoService_2.0/getUltraSrtNcst', params, use_openapi=True
        )

    def get_ultra_short_term_forecast(
        self,
        base_date: str,
        base_time: str,
        nx: int,
        ny: int,
        page_no: int = 1,
        num_of_rows: int = 1000,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get ultra short-term forecast data (documented endpoint).

        Documented endpoint: VilageFcstInfoService_2.0/getUltraSrtFcst (OpenAPI)

        Retrieves ultra short-term forecast data for village forecast grid points.
        Issued every 30 minutes. Provides hourly forecasts up to 6 hours ahead.

        Args:
            base_date: Issue date in YYYYMMDD format (e.g., '20210628')
            base_time: Issue time in HHmm format (e.g., '0630')
            nx: Forecast grid X coordinate (1~149)
            ny: Forecast grid Y coordinate (1~253)
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 1000)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Ultra short-term forecast data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_ultra_short_term_forecast(
            ...     base_date='20210628',
            ...     base_time='0630',
            ...     nx=55,
            ...     ny=127
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'base_date': base_date,
            'base_time': base_time,
            'nx': str(nx),
            'ny': str(ny),
        }
        return self._make_request(
            'VilageFcstInfoService_2.0/getUltraSrtFcst', params, use_openapi=True
        )

    def get_village_forecast(
        self,
        base_date: str,
        base_time: str,
        nx: int,
        ny: int,
        page_no: int = 1,
        num_of_rows: int = 1000,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get village short-term forecast data (documented endpoint).

        Documented endpoint: VilageFcstInfoService_2.0/getVilageFcst (OpenAPI)

        Retrieves short-term forecast data for village forecast grid points.
        Issued 8 times daily (02, 05, 08, 11, 14, 17, 20, 23 KST).
        Provides forecasts up to 3 days ahead.

        Args:
            base_date: Issue date in YYYYMMDD format (e.g., '20210628')
            base_time: Issue time in HHmm format (e.g., '0500')
            nx: Forecast grid X coordinate (1~149)
            ny: Forecast grid Y coordinate (1~253)
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 1000)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Village short-term forecast data

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_village_forecast(
            ...     base_date='20210628',
            ...     base_time='0500',
            ...     nx=55,
            ...     ny=127
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'base_date': base_date,
            'base_time': base_time,
            'nx': str(nx),
            'ny': str(ny),
        }
        return self._make_request(
            'VilageFcstInfoService_2.0/getVilageFcst', params, use_openapi=True
        )

    def get_forecast_version(
        self,
        ftype: str,
        basedatetime: str,
        page_no: int = 1,
        num_of_rows: int = 1000,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get forecast version information (documented endpoint).

        Documented endpoint: VilageFcstInfoService_2.0/getFcstVersion (OpenAPI)

        Retrieves version information for village forecast data files.
        Useful for tracking data updates and changes.

        Args:
            ftype: File type - 'ODAM' (observation), 'VSRT' (ultra short-term),
                   'SHRT' (short-term)
            basedatetime: Issue date/time in YYYYMMDDHHmm format (e.g., '202106280800')
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 1000)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Forecast version information

        Example:
            >>> client = ForecastClient(auth_key='your_key')
            >>> data = client.get_forecast_version(
            ...     ftype='SHRT',
            ...     basedatetime='202106280800'
            ... )

        Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'ftype': ftype,
            'basedatetime': basedatetime,
        }
        return self._make_request(
            'VilageFcstInfoService_2.0/getFcstVersion', params, use_openapi=True
        )

    # ============================================================================
    # Helper methods
    # ============================================================================

    def _format_datetime(self, dt: datetime) -> str:
        """Format datetime object to YYYYMMDDHHmm string.

        Args:
            dt: Datetime object to format

        Returns:
            Formatted datetime string in YYYYMMDDHHmm format
        """
        return dt.strftime('%Y%m%d%H%M')
