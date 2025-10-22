"""Async KMA Weather Forecast API client.

This module provides an async client for accessing the Korea Meteorological Administration's
Weather Forecast (예보) API for weather predictions.

Weather forecasts provide predicted meteorological conditions for
planning and decision-making.
"""

from datetime import datetime
from typing import Any

import httpx


class AsyncForecastClient:
    """Async client for KMA Weather Forecast API.

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
        self._client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> 'AsyncForecastClient':
        """Context manager entry."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def _make_request(
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
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # ==================== Short-term Forecast (단기예보) ====================

    async def get_short_term_region(
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
            >>> async with AsyncForecastClient('your_auth_key')
            >>> # Get most recent forecast
            >>> data = await client.get_short_term_region(tmfc='0')
            >>> # Get forecast for specific period
            >>> data = await client.get_short_term_region(
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

        return await self._make_request('fct_shrt_reg.php', params)

    async def get_short_term_overview(
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
            >>> async with AsyncForecastClient('your_auth_key')
            >>> data = await client.get_short_term_overview(
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

        return await self._make_request('fct_afs_ds.php', params)

    async def get_short_term_land(
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
            >>> async with AsyncForecastClient('your_auth_key')
            >>> data = await client.get_short_term_land(
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

        return await self._make_request('fct_afs_dl.php', params)

    async def get_short_term_land_v2(
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
            >>> async with AsyncForecastClient('your_auth_key')
            >>> data = await client.get_short_term_land_v2(
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

        return await self._make_request('fct_afs_dl2.php', params)

    async def get_short_term_sea(
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
            >>> async with AsyncForecastClient('your_auth_key')
            >>> data = await client.get_short_term_sea(
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

        return await self._make_request('fct_afs_do.php', params)

    # ============================================================================
    # Category 2: Village Forecast Grid Data (동네예보 격자자료)
    # ============================================================================

    async def get_village_short_term_grid(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_village_short_term_grid(
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

        return await self._make_request('nph-dfs_shrt_grd', params, use_cgi=True)

    async def get_village_very_short_term_grid(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_village_very_short_term_grid(
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

        return await self._make_request('nph-dfs_vsrt_grd', params, use_cgi=True)

    async def get_village_observation_grid(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_village_observation_grid(
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

        return await self._make_request('nph-dfs_odam_grd', params, use_cgi=True)

    async def convert_grid_to_coords(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> coords = client.convert_grid_to_coords(x=60, y=127)

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params = {'x': str(x), 'y': str(y), 'help': str(help)}
        return await self._make_request('nph-dfs_xy_lonlat', params, use_cgi=True)

    async def convert_coords_to_grid(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> grid = client.convert_coords_to_grid(lon=127.5, lat=36.5)

        Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
        """
        params = {'lon': str(lon), 'lat': str(lat), 'help': str(help)}
        return await self._make_request('nph-dfs_xy_lonlat', params, use_cgi=True)

    # ============================================================================
    # Category 3: Village Forecast Messages (동네예보 통보문)
    # ============================================================================

    async def get_weather_situation(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_weather_situation(stn_id='108', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if stn_id is not None:
            params['stnId'] = stn_id

        return await self._make_request(
            'VilageFcstMsgService/getWthrSituation', params, use_openapi=True
        )

    async def get_land_forecast_message(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_land_forecast_message(reg_id='11B10101', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if reg_id is not None:
            params['regId'] = reg_id

        return await self._make_request(
            'VilageFcstMsgService/getLandFcst', params, use_openapi=True
        )

    async def get_sea_forecast_message(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_sea_forecast_message(reg_id='12A20100', num_of_rows=5)

        Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }
        if reg_id is not None:
            params['regId'] = reg_id

        return await self._make_request('VilageFcstMsgService/getSeaFcst', params, use_openapi=True)

    # ============================================================================
    # Category 4: Village Forecast API (동네예보 API)
    # ============================================================================

    async def get_ultra_short_term_observation(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_ultra_short_term_observation(
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
        return await self._make_request(
            'VilageFcstInfoService_2.0/getUltraSrtNcst', params, use_openapi=True
        )

    async def get_ultra_short_term_forecast(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_ultra_short_term_forecast(
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
        return await self._make_request(
            'VilageFcstInfoService_2.0/getUltraSrtFcst', params, use_openapi=True
        )

    async def get_village_forecast(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_village_forecast(
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
        return await self._make_request(
            'VilageFcstInfoService_2.0/getVilageFcst', params, use_openapi=True
        )

    async def get_forecast_version(
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
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_forecast_version(
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
        return await self._make_request(
            'VilageFcstInfoService_2.0/getFcstVersion', params, use_openapi=True
        )

    # ============================================================================
    # Category 5: Forecast Distribution Maps (그래픽 예보 분포도)
    # ============================================================================

    async def get_short_term_distribution_map(
        self,
        data0: str,
        data1: str,
        tm_fc: str | datetime,
        tm_ef: str | datetime,
        dtm: str = 'H0',
        map: str = 'G1',  # noqa: A002
        mask: str = 'M',
        color: str = 'E',
        size: int = 600,
        effect: str = 'NTL',
        overlay: str = 'S',
        zoom_rate: int = 2,
        zoom_level: int = 0,
        zoom_x: str = '0000000',
        zoom_y: str = '0000000',
        auto_man: str = 'm',
        mode: str = 'I',
        interval: int = 1,
        rand: int = 1412,
    ) -> dict[str, Any]:
        """Get graphical short-term forecast distribution map (documented endpoint).

        Documented endpoint: nph-dfs_shrt_ana_5d_test (typ03 CGI)

        Provides graphical distribution maps for short-term village forecasts.
        Returns images showing spatial distribution of forecast variables.

        Args:
            data0: Data type (e.g., 'GEMD' for village forecast)
            data1: Variable type (e.g., 'PTY' for precipitation type,
                                  'TMP' for temperature, 'SKY' for sky condition)
            tm_fc: Forecast issue time in 'YYYYMMDDHHmm' format or datetime object
            tm_ef: Forecast valid time in 'YYYYMMDDHHmm' format or datetime object
            dtm: Time step unit and value (default: 'H0')
            map: Map type (default: 'G1')
            mask: Image land/sea mask (default: 'M')
            color: Image color palette (default: 'E')
            size: Image size in pixels (default: 600)
            effect: Image effects (default: 'NTL')
            overlay: Image overlay (default: 'S')
            zoom_rate: Zoom magnification (default: 2)
            zoom_level: Zoom level (default: 0)
            zoom_x: Zoom X coordinate (default: '0000000')
            zoom_y: Zoom Y coordinate (default: '0000000')
            auto_man: Auto/manual mode - 'a' (auto) or 'm' (manual) (default: 'm')
            mode: Display format - 'H' (HTML), 'I' (image), 'A' (auto), 'F' (file) (default: 'I')
            interval: Time interval in hours (default: 1)
            rand: Random number for image regeneration interval in minutes (default: 1412)

        Returns:
            Graphical forecast distribution map data/image

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_short_term_distribution_map(
            ...     data0='GEMD',
            ...     data1='PTY',
            ...     tm_fc='202212221400',
            ...     tm_ef='202212260000'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 288-311
        """
        params = {
            'data0': data0,
            'data1': data1,
            'tm_fc': tm_fc if isinstance(tm_fc, str) else self._format_datetime(tm_fc),
            'tm_ef': tm_ef if isinstance(tm_ef, str) else self._format_datetime(tm_ef),
            'dtm': dtm,
            'map': map,
            'mask': mask,
            'color': color,
            'size': str(size),
            'effect': effect,
            'overlay': overlay,
            'zoom_rate': str(zoom_rate),
            'zoom_level': str(zoom_level),
            'zoom_x': zoom_x,
            'zoom_y': zoom_y,
            'auto_man': auto_man,
            'mode': mode,
            'interval': str(interval),
            'rand': str(rand),
        }
        # This uses typ03 API base URL
        base_url = 'https://apihub.kma.go.kr/api/typ03/cgi/dfs'
        url = f'{base_url}/nph-dfs_shrt_ana_5d_test'
        params['authKey'] = self.auth_key
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def get_very_short_term_distribution_map(
        self,
        data0: str,
        data1: str,
        tm_fc: str | datetime,
        tm_ef: str | datetime,
        dtm: str = 'H0',
        map: str = 'G1',  # noqa: A002
        mask: str = 'M',
        color: str = 'E',
        size: int = 600,
        effect: str = 'NTL',
        overlay: str = 'S',
        zoom_rate: int = 2,
        zoom_level: int = 0,
        zoom_x: str = '0000000',
        zoom_y: str = '0000000',
        auto_man: str = 'm',
        mode: str = 'I',
        interval: int = 1,
        rand: int = 1412,
    ) -> dict[str, Any]:
        """Get graphical ultra short-term forecast distribution map (documented endpoint).

        Documented endpoint: nph-dfs_shrt_ana_5d_test (typ03 CGI)

        Provides graphical distribution maps for ultra short-term village forecasts.
        Returns images showing spatial distribution of forecast variables.

        Args:
            data0: Data type (e.g., 'GEMD' for village forecast)
            data1: Variable type (e.g., 'PTY', 'TMP', 'SKY')
            tm_fc: Forecast issue time in 'YYYYMMDDHHmm' format or datetime object
            tm_ef: Forecast valid time in 'YYYYMMDDHHmm' format or datetime object
            dtm: Time step unit and value (default: 'H0')
            map: Map type (default: 'G1')
            mask: Image land/sea mask (default: 'M')
            color: Image color palette (default: 'E')
            size: Image size in pixels (default: 600)
            effect: Image effects (default: 'NTL')
            overlay: Image overlay (default: 'S')
            zoom_rate: Zoom magnification (default: 2)
            zoom_level: Zoom level (default: 0)
            zoom_x: Zoom X coordinate (default: '0000000')
            zoom_y: Zoom Y coordinate (default: '0000000')
            auto_man: Auto/manual mode - 'a' or 'm' (default: 'm')
            mode: Display format - 'H', 'I', 'A', 'F' (default: 'I')
            interval: Time interval in hours (default: 1)
            rand: Random number for image regeneration interval (default: 1412)

        Returns:
            Graphical forecast distribution map data/image

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_very_short_term_distribution_map(
            ...     data0='GEMD',
            ...     data1='PTY',
            ...     tm_fc='202212221400',
            ...     tm_ef='202212260000'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 313-336
        """
        params = {
            'data0': data0,
            'data1': data1,
            'tm_fc': tm_fc if isinstance(tm_fc, str) else self._format_datetime(tm_fc),
            'tm_ef': tm_ef if isinstance(tm_ef, str) else self._format_datetime(tm_ef),
            'dtm': dtm,
            'map': map,
            'mask': mask,
            'color': color,
            'size': str(size),
            'effect': effect,
            'overlay': overlay,
            'zoom_rate': str(zoom_rate),
            'zoom_level': str(zoom_level),
            'zoom_x': zoom_x,
            'zoom_y': zoom_y,
            'auto_man': auto_man,
            'mode': mode,
            'interval': str(interval),
            'rand': str(rand),
        }
        # This uses typ03 API base URL
        base_url = 'https://apihub.kma.go.kr/api/typ03/cgi/dfs'
        url = f'{base_url}/nph-dfs_shrt_ana_5d_test'
        params['authKey'] = self.auth_key
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # ============================================================================
    # Category 6: Grid Coordinate Data (동네예보 격자데이터 위경도)
    # ============================================================================

    async def get_grid_latlon_data(
        self,
        fct: str,
        latlon: str,
        disp: str = 'A',
    ) -> dict[str, Any]:
        """Get village forecast grid latitude/longitude data (documented endpoint).

        Documented endpoint: nph-dfs_latlon_api (CGI)

        Retrieves latitude or longitude values for all grid points in the
        village forecast system.

        Args:
            fct: Forecast type - 'SHRT' (short-term), 'VSRT' (very short-term/observation)
            latlon: Coordinate type - 'lon' (longitude) or 'lat' (latitude)
                   'lon': outputs longitude values from bottom-left to top-right
                   'lat': outputs latitude values from bottom-left to top-right
            disp: Display format (default: 'A')
                  'A' (ASCII): grid count + data values
                  'B' (BINARY): grid count (4 bytes) + data as floats

        Returns:
            Grid latitude or longitude data for all grid points

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> # Get longitude values for short-term forecast grid
            >>> data = await client.get_grid_latlon_data(fct='SHRT', latlon='lon')

        Reference: API_ENDPOINT_Forecast.md line 339-351
        """
        params = {'fct': fct, 'latlon': latlon, 'disp': disp}
        return await self._make_request('nph-dfs_latlon_api', params, use_cgi=True)

    async def download_grid_latlon_netcdf(
        self,
        fct: str,
    ) -> dict[str, Any]:
        """Download village forecast grid lat/lon NetCDF file (documented endpoint).

        Documented endpoint: nph-dfs_latlon_api (CGI)

        Downloads a NetCDF file containing latitude and longitude coordinates
        for all grid points in the village forecast system.

        Args:
            fct: Forecast type - 'SHRT' (short-term), 'VSRT' (very short-term/observation)

        Returns:
            NetCDF file data with grid coordinates

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.download_grid_latlon_netcdf(fct='SHRT')

        Reference: API_ENDPOINT_Forecast.md line 353-362
        """
        params = {'fct': fct}
        return await self._make_request('nph-dfs_latlon_api', params, use_cgi=True)

    # ============================================================================
    # Category 7: Medium-term Forecast (중기예보)
    # ============================================================================

    async def get_medium_term_region(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        mode: int = 0,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get medium-term forecast region data (documented endpoint).

        Documented endpoint: fct_medm_reg.php

        Retrieves medium-term forecast region information. Medium-term forecasts
        cover 3-10 days ahead with AM/PM details for days 3-7 and daily for days 8-10.

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            mode: Display mode. 0=values only (fast), 1=include forecaster ID/name/region name
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Medium-term forecast region data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_region(tmfc='0')

        Reference: API_ENDPOINT_Forecast.md line 370-387
        """
        params: dict[str, Any] = {'mode': str(mode), 'disp': str(disp), 'help': '1'}

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

        return await self._make_request('fct_medm_reg.php', params)

    async def get_medium_term_overview(
        self,
        stn: str | None = None,
        reg: str | None = None,
        tmfc: str | datetime | None = None,
        tmfc1: str | datetime | None = None,
        tmfc2: str | datetime | None = None,
        tmef1: str | datetime | None = None,
        tmef2: str | datetime | None = None,
        mode: int = 0,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get medium-term forecast overview (중기 개황) (documented endpoint).

        Documented endpoint: fct_afs_ws.php

        Retrieves medium-term forecast overview/summary information.

        Args:
            stn: Station/office number. None for all.
            reg: Forecast region code. None for all.
            tmfc: Forecast time. None for all, '0' for most recent.
            tmfc1: Forecast period start time. None for most recent.
            tmfc2: Forecast period end time. None for most recent.
            tmef1: Effective period start time. None for all forecast period.
            tmef2: Effective period end time. None for all forecast period.
            mode: Display mode. 0=values only, 1=include forecaster info
            disp: Display format. 0=Fortran (default), 1=Excel (CSV)

        Returns:
            Medium-term forecast overview data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_overview(
            ...     tmfc1='2013121106', tmfc2='2013121118'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 388-405
        """
        params: dict[str, Any] = {'mode': str(mode), 'disp': str(disp), 'help': '1'}

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

        return await self._make_request('fct_afs_ws.php', params)

    async def get_medium_term_land(
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
        """Get medium-term land forecast (중기 육상예보) (documented endpoint).

        Documented endpoint: fct_afs_wl.php

        Retrieves medium-term land forecast data for 3-10 days ahead.

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
            Medium-term land forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_land(
            ...     reg='',
            ...     tmfc1='2013121106',
            ...     tmfc2='2013121118',
            ...     tmef1='20131214',
            ...     tmef2='20131219'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 406-422
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

        return await self._make_request('fct_afs_wl.php', params)

    async def get_medium_term_temperature(
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
        """Get medium-term temperature forecast (중기 기온예보) (documented endpoint).

        Documented endpoint: fct_afs_wc.php

        Retrieves medium-term temperature forecast data including max/min temperatures
        and temperature ranges for 3-10 days ahead.

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
            Medium-term temperature forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_temperature(
            ...     reg='',
            ...     tmfc1='2013121106',
            ...     tmfc2='2013121118',
            ...     tmef1='20131214',
            ...     tmef2='20131219'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 423-439
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

        return await self._make_request('fct_afs_wc.php', params)

    async def get_medium_term_sea(
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
        """Get medium-term sea forecast (중기 해상예보) (documented endpoint).

        Documented endpoint: fct_afs_wo.php

        Retrieves medium-term marine/sea forecast data including wave height
        for 3-10 days ahead.

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
            Medium-term sea forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_sea(
            ...     reg='',
            ...     tmfc1='2013121106',
            ...     tmfc2='2013121118',
            ...     tmef1='20131214',
            ...     tmef2='20131219'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 440-456
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

        return await self._make_request('fct_afs_wo.php', params)

    async def get_medium_term_sea_forecast(
        self,
        reg_id: str,
        tm_fc: str,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get medium-term sea forecast via OpenAPI (documented endpoint).

        Documented endpoint: MidFcstInfoService/getMidSeaFcst (OpenAPI)

        Retrieves medium-term marine forecast for specific sea regions.
        Issued twice daily at 06:00 and 18:00 KST. Only last 24 hours available.

        Args:
            reg_id: Forecast region code (e.g., '12A20000' West Sea Central,
                                                '12B10000' South Sea West)
            tm_fc: Forecast issue time in YYYYMMDDHHmm format (e.g., '201404080600')
                   Must be either 0600 or 1800.
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Medium-term sea forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_sea_forecast(
            ...     reg_id='12A20000',
            ...     tm_fc='201404080600'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 459-473
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'regId': reg_id,
            'tmFc': tm_fc,
        }
        return await self._make_request(
            'MidFcstInfoService/getMidSeaFcst', params, use_openapi=True
        )

    async def get_medium_term_temperature_forecast(
        self,
        reg_id: str,
        tm_fc: str,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get medium-term temperature forecast via OpenAPI (documented endpoint).

        Documented endpoint: MidFcstInfoService/getMidTa (OpenAPI)

        Retrieves medium-term temperature forecast for specific regions.
        Issued twice daily at 06:00 and 18:00 KST. Only last 24 hours available.

        Args:
            reg_id: Forecast region code (e.g., '11B10101' Seoul, '11B20201' Incheon)
            tm_fc: Forecast issue time in YYYYMMDDHHmm format (e.g., '201309030600')
                   Must be either 0600 or 1800.
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Medium-term temperature forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_temperature_forecast(
            ...     reg_id='11B10101',
            ...     tm_fc='201309030600'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 474-488
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'regId': reg_id,
            'tmFc': tm_fc,
        }
        return await self._make_request('MidFcstInfoService/getMidTa', params, use_openapi=True)

    async def get_medium_term_land_forecast(
        self,
        reg_id: str,
        tm_fc: str,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get medium-term land forecast via OpenAPI (documented endpoint).

        Documented endpoint: MidFcstInfoService/getMidLandFcst (OpenAPI)

        Retrieves medium-term land forecast for specific regions.
        Issued twice daily at 06:00 and 18:00 KST. Only last 24 hours available.

        Args:
            reg_id: Forecast region code (e.g., '11B00000' Seoul/Incheon/Gyeonggi,
                                                '11D10000' Gangwon Yeongdong)
            tm_fc: Forecast issue time in YYYYMMDDHHmm format (e.g., '202107300600')
                   Must be either 0600 or 1800.
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Medium-term land forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_land_forecast(
            ...     reg_id='11B00000',
            ...     tm_fc='202107300600'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 489-503
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'regId': reg_id,
            'tmFc': tm_fc,
        }
        return await self._make_request(
            'MidFcstInfoService/getMidLandFcst', params, use_openapi=True
        )

    async def get_medium_term_outlook(
        self,
        stn_id: str,
        tm_fc: str,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
    ) -> dict[str, Any]:
        """Get medium-term outlook/perspective forecast (중기전망) (documented endpoint).

        Documented endpoint: MidFcstInfoService/getMidFcst (OpenAPI)

        Retrieves medium-term forecast outlook for specific stations.
        Issued twice daily at 06:00 and 18:00 KST. Only last 24 hours available.

        Args:
            stn_id: Station code (e.g., '108' National, '109' Seoul/Incheon/Gyeonggi)
            tm_fc: Forecast issue time in YYYYMMDDHHmm format (e.g., '201310170600')
                   Must be either 0600 or 1800.
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')

        Returns:
            Medium-term outlook forecast data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_medium_term_outlook(
            ...     stn_id='108',
            ...     tm_fc='201310170600'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 504-518
        """
        params = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
            'stnId': stn_id,
            'tmFc': tm_fc,
        }
        return await self._make_request('MidFcstInfoService/getMidFcst', params, use_openapi=True)

    # ============================================================================
    # Category 8: Weather Warnings (기상특보)
    # ============================================================================

    async def get_warning_region(
        self,
        wrn: str | None = None,
        reg: str | None = None,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        subcd: str | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get weather warning region data (documented endpoint).

        Documented endpoint: wrn_reg.php

        Retrieves weather warning region information for various warning types.

        Args:
            wrn: Warning type. W=strong wind, R=heavy rain, C=cold wave, D=dry,
                 O=storm surge, N=tsunami, V=high waves, T=typhoon, S=heavy snow,
                 Y=yellow dust, H=heat wave, F=fog. None for all types.
            reg: Forecast region code. None for all.
            tmfc1: Issue time period start (YYYYMMDDHHmm). None for most recent.
            tmfc2: Issue time period end (YYYYMMDDHHmm). None for most recent.
            subcd: Weather comment subtitle code. 11=ultra-short, 12=short, 13=medium,
                   99=direct input. None for all.
            disp: Display level. 0=basic, 1=+warning content, 2=+editor info

        Returns:
            Weather warning region data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_warning_region(tmfc1='201501010000', tmfc2='201502010000')

        Reference: API_ENDPOINT_Forecast.md line 526-540
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if wrn is not None:
            params['wrn'] = wrn
        if reg is not None:
            params['reg'] = reg
        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2
        if subcd is not None:
            params['subcd'] = subcd

        return await self._make_request('wrn_reg.php', params)

    async def get_warning_data(
        self,
        wrn: str | None = None,
        reg: str | None = None,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        subcd: str | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get weather warning data (documented endpoint).

        Documented endpoint: wrn_met_data.php

        Retrieves detailed weather warning data for analysis.

        Args:
            wrn: Warning type (see get_warning_region for codes). None for all.
            reg: Forecast region code. None for all.
            tmfc1: Issue time period start. None for most recent.
            tmfc2: Issue time period end. None for most recent.
            subcd: Weather comment subtitle code. None for all.
            disp: Display level. 0=basic, 1=+warning content, 2=+editor info

        Returns:
            Weather warning data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_warning_data(
            ...     wrn='R', tmfc1='201501010000', tmfc2='201502010000'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 541-555
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if wrn is not None:
            params['wrn'] = wrn
        if reg is not None:
            params['reg'] = reg
        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2
        if subcd is not None:
            params['subcd'] = subcd

        return await self._make_request('wrn_met_data.php', params)

    async def get_weather_information(
        self,
        wrn: str | None = None,
        reg: str | None = None,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        stn: str = '0',
        subcd: str | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get weather information reports (documented endpoint).

        Documented endpoint: wrn_inf_rpt.php

        Retrieves weather information and alert reports.

        Args:
            wrn: Warning type. None for all.
            reg: Forecast region code. None for all.
            tmfc1: Issue time period start. None for most recent.
            tmfc2: Issue time period end. None for most recent.
            stn: Station number (default: '0' for all)
            subcd: Weather comment subtitle code. None for all.
            disp: Display level. 0=basic, 1=+warning content, 2=+editor info

        Returns:
            Weather information report data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_weather_information(
            ...     tmfc1='201505010000', tmfc2='201506010000'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 556-570
        """
        params: dict[str, Any] = {'stn': stn, 'disp': str(disp), 'help': '1'}

        if wrn is not None:
            params['wrn'] = wrn
        if reg is not None:
            params['reg'] = reg
        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2
        if subcd is not None:
            params['subcd'] = subcd

        return await self._make_request('wrn_inf_rpt.php', params)

    async def get_weather_commentary(
        self,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        stn: str = '0',
        subcd: str = '0',
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get weather commentary/explanation reports (documented endpoint).

        Documented endpoint: wthr_cmt_rpt.php

        Retrieves weather commentary and explanation reports from forecasters.

        Args:
            tmfc1: Issue time period start. None for most recent.
            tmfc2: Issue time period end. None for most recent.
            stn: Station number (default: '0' for all)
            subcd: Weather comment subtitle code (default: '0' for all)
            disp: Display level. 0=basic, 1=+warning content, 2=+editor info

        Returns:
            Weather commentary report data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_weather_commentary(
            ...     tmfc1='202004130000', tmfc2='202004140000'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 571-585
        """
        params: dict[str, Any] = {'stn': stn, 'subcd': subcd, 'disp': str(disp), 'help': '1'}

        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2

        return await self._make_request('wthr_cmt_rpt.php', params)

    async def get_current_warning_status(
        self,
        fe: str = 'f',
        tm: str | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get current warning status (documented endpoint).

        Documented endpoint: wrn_now_data.php

        Retrieves current active warning status.

        Args:
            fe: Time basis. 'f'=issue time basis (default), 'e'=effective time basis
            tm: Reference time in YYYYMMDDHHmm format. None for current.
            disp: Display format

        Returns:
            Current warning status data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_current_warning_status(fe='f')

        Reference: API_ENDPOINT_Forecast.md line 588-598
        """
        params: dict[str, Any] = {'fe': fe, 'disp': str(disp), 'help': '1'}

        if tm is not None:
            params['tm'] = tm

        return await self._make_request('wrn_now_data.php', params)

    async def get_current_warning_status_new(
        self,
        fe: str = 'f',
        tm: str | None = None,
        disp: int = 0,
    ) -> dict[str, Any]:
        """Get current warning status (new version) (documented endpoint).

        Documented endpoint: wrn_now_data_new.php

        Retrieves current active warning status using new API version.

        Args:
            fe: Time basis. 'f'=issue time basis (default), 'e'=effective time basis
            tm: Reference time in YYYYMMDDHHmm format. None for current.
            disp: Display format

        Returns:
            Current warning status data (new version)

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_current_warning_status_new(fe='f')

        Reference: API_ENDPOINT_Forecast.md line 600-610
        """
        params: dict[str, Any] = {'fe': fe, 'disp': str(disp), 'help': '1'}

        if tm is not None:
            params['tm'] = tm

        return await self._make_request('wrn_now_data_new.php', params)

    async def get_warning_image(
        self,
        tm: str,
        lat: float,
        lon: float,
        range: int,  # noqa: A002
        size: int,
        wrn: str,
        tmef: int = 1,
        city: int = 1,
        name: int = 0,
        stn: str | None = None,
        out: int = 0,
    ) -> dict[str, Any]:
        """Get weather warning image for arbitrary region (documented endpoint).

        Documented endpoint: nph-wrn7 (typ03 CGI)

        Retrieves weather warning images for specified regions and warning types.

        Args:
            tm: Query time (warning issue time) in YYYYMMDDHHmm format
            lat: Latitude - center latitude for arbitrary region warning image
            lon: Longitude - center longitude for arbitrary region warning image
            range: Display radius in km from center (lat/lon)
            size: Warning image size in pixels
            wrn: Warning types (delimiter | for multiple).
                 W=strong wind, R=heavy rain, C=cold wave, D=dry, O=storm surge,
                 V=high waves, T=typhoon, S=heavy snow, Y=yellow dust, H=heat wave
            tmef: Issue/effective distinction. 0=issue time basis,
                  1=effective time basis (default: 1)
            city: City/county boundary. 0=not displayed, 1=displayed (default: 1)
            name: Administrative district name. 0=not displayed (default), 1=displayed
            stn: Regional office query. 108=HQ, 133=Daejeon, 159=Busan, 156=Gwangju,
                 184=Jeju, 105=Gangwon. None for arbitrary region.
            out: Output format (default: 0)

        Returns:
            Weather warning image data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_warning_image(
            ...     tm='201611082300',
            ...     lon=127.7,
            ...     lat=36.1,
            ...     range=300,
            ...     size=685,
            ...     wrn='W,R,C,D,O,V,T,S,Y,H'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 614-634
        """
        params = {
            'tm': tm,
            'lat': str(lat),
            'lon': str(lon),
            'range': str(range),
            'size': str(size),
            'wrn': wrn,
            'tmef': str(tmef),
            'city': str(city),
            'name': str(name),
            'out': str(out),
        }

        if stn is not None:
            params['stn'] = stn

        # This uses typ03 API base URL
        base_url = 'https://apihub.kma.go.kr/api/typ03/cgi/wrn'
        url = f'{base_url}/nph-wrn7'
        params['authKey'] = self.auth_key
        response = await self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # ============================================================================
    # Category 9: Impact Forecast (영향예보)
    # ============================================================================

    async def get_impact_forecast_status(
        self,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        tmef1: str | None = None,
        tmef2: str | None = None,
        ifpar: str | None = None,
        ifarea: str = '0',
        regid: str | None = None,
    ) -> dict[str, Any]:
        """Get impact forecast status (발표구역별 위험수준) (documented endpoint).

        Documented endpoint: ifs_fct_pstt.php

        Retrieves impact forecast status showing risk levels by region.
        Impact forecasts provide detailed impact information and response guidelines
        by risk level for heat waves and cold waves.

        Args:
            tmfc1: Issue time period start (YYYYMMDDHHmm)
            tmfc2: Issue time period end (YYYYMMDDHHmm)
            tmef1: Effective time period start (YYYYMMDD)
            tmef2: Effective time period end (YYYYMMDD)
            ifpar: Impact forecast parameter. 'hw'=heat wave, 'cw'=cold wave
            ifarea: Impact area (default: '0')
            regid: Warning region code

        Returns:
            Impact forecast status data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> # Heat wave impact forecast for period (effective time basis)
            >>> data = await client.get_impact_forecast_status(
            ...     tmef1='20210701', tmef2='20210730', ifpar='hw'
            ... )
            >>> # Cold wave impact forecast for period (issue time basis)
            >>> data = await client.get_impact_forecast_status(
            ...     tmfc1='20210101', tmfc2='20210131', ifpar='cw'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 647-663
        """
        params: dict[str, Any] = {'ifarea': ifarea, 'help': '1'}

        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2
        if tmef1 is not None:
            params['tmef1'] = tmef1
        if tmef2 is not None:
            params['tmef2'] = tmef2
        if ifpar is not None:
            params['ifpar'] = ifpar
        if regid is not None:
            params['regid'] = regid

        return await self._make_request('ifs_fct_pstt.php', params)

    async def get_impact_risk_level_zone_count(
        self,
        tmfc1: str | None = None,
        tmfc2: str | None = None,
        tmef1: str | None = None,
        tmef2: str | None = None,
        ifarea: str = '0',
        stn: str | None = None,
        ilvl: int | None = None,
    ) -> dict[str, Any]:
        """Get impact forecast risk level zone count (documented endpoint).

        Documented endpoint: ifs_ilvl_zone_cnt.php

        Retrieves the count of areas by risk level for impact forecasts.

        Args:
            tmfc1: Issue time period start (YYYYMMDDHHmm)
            tmfc2: Issue time period end (YYYYMMDDHHmm)
            tmef1: Effective time period start (YYYYMMDD)
            tmef2: Effective time period end (YYYYMMDD)
            ifarea: Impact area (default: '0')
            stn: Station/office code (e.g., '108')
            ilvl: Risk level (0-3)

        Returns:
            Zone count by risk level

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_impact_risk_level_zone_count(
            ...     tmef1='20210701', tmef2='20210730'
            ... )

        Reference: API_ENDPOINT_Forecast.md line 666-689
        """
        params: dict[str, Any] = {'ifarea': ifarea, 'help': '1'}

        if tmfc1 is not None:
            params['tmfc1'] = tmfc1
        if tmfc2 is not None:
            params['tmfc2'] = tmfc2
        if tmef1 is not None:
            params['tmef1'] = tmef1
        if tmef2 is not None:
            params['tmef2'] = tmef2
        if stn is not None:
            params['stn'] = stn
        if ilvl is not None:
            params['ilvl'] = str(ilvl)

        return await self._make_request('ifs_ilvl_zone_cnt.php', params)

    async def get_impact_risk_level_distribution_map(
        self,
        tmfc: str,
        stn: str | None = None,
        ifpar: str | None = None,
        ifarea: int | None = None,
    ) -> dict[str, Any]:
        """Get impact forecast risk level distribution map (documented endpoint).

        Documented endpoint: ifs_ilvl_dmap.php

        Retrieves spatial distribution map of risk levels for impact forecasts.

        Args:
            tmfc: Forecast issue date (YYYYMMDD)
            stn: Station/office code (e.g., '108')
            ifpar: Impact forecast parameter. 'hw'=heat wave, 'cw'=cold wave
            ifarea: Impact area code

        Returns:
            Risk level distribution map data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_impact_risk_level_distribution_map(tmfc='20220601')

        Reference: API_ENDPOINT_Forecast.md line 692-716
        """
        params: dict[str, Any] = {'tmfc': tmfc}

        if stn is not None:
            params['stn'] = stn
        if ifpar is not None:
            params['ifpar'] = ifpar
        if ifarea is not None:
            params['ifarea'] = str(ifarea)

        return await self._make_request('ifs_ilvl_dmap.php', params)

    # ============================================================================
    # Category 10: Region Information (예,특보 구역정보)
    # ============================================================================

    async def get_forecast_zone_code(
        self,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
        reg_id: str | None = None,
    ) -> dict[str, Any]:
        """Get forecast zone code information (documented endpoint).

        Documented endpoint: FcstZoneInfoService/getFcstZoneCd (OpenAPI)

        Retrieves forecast zone code information for administrative regions.

        Args:
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')
            reg_id: Region ID (e.g., '11A00101')

        Returns:
            Forecast zone code data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_forecast_zone_code(reg_id='11A00101')

        Reference: API_ENDPOINT_Forecast.md line 722-727
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }

        if reg_id is not None:
            params['regId'] = reg_id

        return await self._make_request(
            'FcstZoneInfoService/getFcstZoneCd', params, use_openapi=True
        )

    async def get_warning_zone_code(
        self,
        page_no: int = 1,
        num_of_rows: int = 10,
        data_type: str = 'JSON',
        kor_name: str | None = None,
    ) -> dict[str, Any]:
        """Get warning zone code information (documented endpoint).

        Documented endpoint: WethrBasicInfoService/getWrnZoneCd (OpenAPI)

        Retrieves warning zone code information for weather warnings.

        Args:
            page_no: Page number (default: 1)
            num_of_rows: Number of results per page (default: 10)
            data_type: Response data format - 'XML' or 'JSON' (default: 'JSON')
            kor_name: Korean name of the region

        Returns:
            Warning zone code data

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_warning_zone_code()

        Reference: API_ENDPOINT_Forecast.md line 730-735
        """
        params: dict[str, Any] = {
            'pageNo': str(page_no),
            'numOfRows': str(num_of_rows),
            'dataType': data_type,
        }

        if kor_name is not None:
            params['korName'] = kor_name

        return await self._make_request(
            'WethrBasicInfoService/getWrnZoneCd', params, use_openapi=True
        )

    async def get_aws_warning_zone_code(
        self,
        tm: str | None = None,
        disp: int = 1,
    ) -> dict[str, Any]:
        """Get AWS station warning zone codes (documented endpoint).

        Documented endpoint: wrn_reg_aws2.php

        Retrieves warning zone codes for AWS (Automated Weather Station) locations,
        including warning zone names.

        Args:
            tm: Reference time. None for current.
            disp: Display format (default: 1)

        Returns:
            AWS warning zone code data with zone names

        Example:
            >>> async with AsyncForecastClient(auth_key='your_key')
            >>> data = await client.get_aws_warning_zone_code()

        Reference: API_ENDPOINT_Forecast.md line 744-749
        """
        params: dict[str, Any] = {'disp': str(disp), 'help': '1'}

        if tm is not None:
            params['tm'] = tm

        return await self._make_request('wrn_reg_aws2.php', params)

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
