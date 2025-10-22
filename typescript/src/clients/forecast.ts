/**
 * Weather Forecast Client
 * 예보 클라이언트
 *
 * Provides access to various KMA forecast services including:
 * - Short-term forecasts (up to 3 days)
 * - Medium-term forecasts (3-10 days)
 * - Village forecast grid data
 * - Weather warnings and impact forecasts
 *
 * Reference: API_ENDPOINT_Forecast.md
 */
import axios from 'axios';
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface ForecastData {
  tmFc: string; // 예보시각
  regId: string; // 지역코드
  taMin: number; // 최저기온(°C)
  taMax: number; // 최고기온(°C)
  wf: string; // 날씨
  rnSt: number; // 강수확률(%)
}

export class ForecastClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  // ============================================================================
  // Category 1: Short-term Forecast (단기예보)
  // ============================================================================

  /**
   * Get short-term forecast by region (documented endpoint)
   *
   * Documented endpoint: fct_shrt_reg.php
   *
   * Provides short-term weather forecast data organized by region.
   * Supports flexible time range queries for forecast issue times and
   * effective times.
   *
   * @param stn - Station/region code (optional)
   * @param reg - Region code (optional)
   * @param tmfc - Single forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc1 - Start forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc2 - End forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef1 - Start forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef2 - End forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Short-term forecast data by region
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * // Get forecast for a specific time
   * const data = await client.getShortTermRegion({ tmfc: '202501011200' });
   * // Get forecast for a time range
   * const data2 = await client.getShortTermRegion({
   *   tmfc1: '202501010000',
   *   tmfc2: '202501020000',
   *   reg: '11B00000'
   * });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 1: Short-term Forecast
   */
  async getShortTermRegion(params?: {
    stn?: string;
    reg?: string;
    tmfc?: string | Date;
    tmfc1?: string | Date;
    tmfc2?: string | Date;
    tmef1?: string | Date;
    tmef2?: string | Date;
    disp?: number;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: '1',
    };

    if (params?.stn) requestParams.stn = params.stn;
    if (params?.reg) requestParams.reg = params.reg;
    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmfc1) {
      requestParams.tmfc1 =
        typeof params.tmfc1 === 'string' ? params.tmfc1 : this.formatDateTime(params.tmfc1);
    }
    if (params?.tmfc2) {
      requestParams.tmfc2 =
        typeof params.tmfc2 === 'string' ? params.tmfc2 : this.formatDateTime(params.tmfc2);
    }
    if (params?.tmef1) {
      requestParams.tmef1 =
        typeof params.tmef1 === 'string' ? params.tmef1 : this.formatDateTime(params.tmef1);
    }
    if (params?.tmef2) {
      requestParams.tmef2 =
        typeof params.tmef2 === 'string' ? params.tmef2 : this.formatDateTime(params.tmef2);
    }

    return this.makeRequest<ForecastData>('fct_shrt_reg.php', requestParams);
  }

  /**
   * Get short-term forecast overview (documented endpoint)
   *
   * Documented endpoint: fct_afs_ds.php
   *
   * Provides overview of short-term weather forecasts.
   * Note: This endpoint does not require a help parameter.
   *
   * @param stn - Station/region code (optional)
   * @param reg - Region code (optional)
   * @param tmfc - Single forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc1 - Start forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc2 - End forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef1 - Start forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef2 - End forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Short-term forecast overview data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getShortTermOverview({ tmfc: '202501011200' });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 1: Short-term Forecast
   */
  async getShortTermOverview(params?: {
    stn?: string;
    reg?: string;
    tmfc?: string | Date;
    tmfc1?: string | Date;
    tmfc2?: string | Date;
    tmef1?: string | Date;
    tmef2?: string | Date;
    disp?: number;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
    };

    if (params?.stn) requestParams.stn = params.stn;
    if (params?.reg) requestParams.reg = params.reg;
    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmfc1) {
      requestParams.tmfc1 =
        typeof params.tmfc1 === 'string' ? params.tmfc1 : this.formatDateTime(params.tmfc1);
    }
    if (params?.tmfc2) {
      requestParams.tmfc2 =
        typeof params.tmfc2 === 'string' ? params.tmfc2 : this.formatDateTime(params.tmfc2);
    }
    if (params?.tmef1) {
      requestParams.tmef1 =
        typeof params.tmef1 === 'string' ? params.tmef1 : this.formatDateTime(params.tmef1);
    }
    if (params?.tmef2) {
      requestParams.tmef2 =
        typeof params.tmef2 === 'string' ? params.tmef2 : this.formatDateTime(params.tmef2);
    }

    return this.makeRequest<ForecastData>('fct_afs_ds.php', requestParams);
  }

  /**
   * Get short-term land forecast (documented endpoint)
   *
   * Documented endpoint: fct_afs_dl.php
   *
   * Provides short-term weather forecasts specifically for land areas.
   *
   * @param stn - Station/region code (optional)
   * @param reg - Region code (optional)
   * @param tmfc - Single forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc1 - Start forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc2 - End forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef1 - Start forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef2 - End forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Short-term land forecast data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getShortTermLand({ tmfc: '202501011200' });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 1: Short-term Forecast
   */
  async getShortTermLand(params?: {
    stn?: string;
    reg?: string;
    tmfc?: string | Date;
    tmfc1?: string | Date;
    tmfc2?: string | Date;
    tmef1?: string | Date;
    tmef2?: string | Date;
    disp?: number;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: '1',
    };

    if (params?.stn) requestParams.stn = params.stn;
    if (params?.reg) requestParams.reg = params.reg;
    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmfc1) {
      requestParams.tmfc1 =
        typeof params.tmfc1 === 'string' ? params.tmfc1 : this.formatDateTime(params.tmfc1);
    }
    if (params?.tmfc2) {
      requestParams.tmfc2 =
        typeof params.tmfc2 === 'string' ? params.tmfc2 : this.formatDateTime(params.tmfc2);
    }
    if (params?.tmef1) {
      requestParams.tmef1 =
        typeof params.tmef1 === 'string' ? params.tmef1 : this.formatDateTime(params.tmef1);
    }
    if (params?.tmef2) {
      requestParams.tmef2 =
        typeof params.tmef2 === 'string' ? params.tmef2 : this.formatDateTime(params.tmef2);
    }

    return this.makeRequest<ForecastData>('fct_afs_dl.php', requestParams);
  }

  /**
   * Get short-term land forecast v2 (documented endpoint)
   *
   * Documented endpoint: fct_afs_dl2.php
   *
   * Provides short-term weather forecasts for land areas using an updated format.
   * This is a newer version of the land forecast endpoint.
   *
   * @param stn - Station/region code (optional)
   * @param reg - Region code (optional)
   * @param tmfc - Single forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc1 - Start forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc2 - End forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef1 - Start forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef2 - End forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Short-term land forecast data (v2 format)
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getShortTermLandV2({ tmfc: '202501011200' });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 1: Short-term Forecast
   */
  async getShortTermLandV2(params?: {
    stn?: string;
    reg?: string;
    tmfc?: string | Date;
    tmfc1?: string | Date;
    tmfc2?: string | Date;
    tmef1?: string | Date;
    tmef2?: string | Date;
    disp?: number;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: '1',
    };

    if (params?.stn) requestParams.stn = params.stn;
    if (params?.reg) requestParams.reg = params.reg;
    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmfc1) {
      requestParams.tmfc1 =
        typeof params.tmfc1 === 'string' ? params.tmfc1 : this.formatDateTime(params.tmfc1);
    }
    if (params?.tmfc2) {
      requestParams.tmfc2 =
        typeof params.tmfc2 === 'string' ? params.tmfc2 : this.formatDateTime(params.tmfc2);
    }
    if (params?.tmef1) {
      requestParams.tmef1 =
        typeof params.tmef1 === 'string' ? params.tmef1 : this.formatDateTime(params.tmef1);
    }
    if (params?.tmef2) {
      requestParams.tmef2 =
        typeof params.tmef2 === 'string' ? params.tmef2 : this.formatDateTime(params.tmef2);
    }

    return this.makeRequest<ForecastData>('fct_afs_dl2.php', requestParams);
  }

  /**
   * Get short-term sea forecast (documented endpoint)
   *
   * Documented endpoint: fct_afs_do.php
   *
   * Provides short-term weather forecasts specifically for sea/ocean areas.
   *
   * @param stn - Station/region code (optional)
   * @param reg - Region code (optional)
   * @param tmfc - Single forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc1 - Start forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmfc2 - End forecast issue time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef1 - Start forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param tmef2 - End forecast effective time in YYYYMMDDHHmm format or Date object (optional)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Short-term sea forecast data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getShortTermSea({ tmfc: '202501011200' });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 1: Short-term Forecast
   */
  async getShortTermSea(params?: {
    stn?: string;
    reg?: string;
    tmfc?: string | Date;
    tmfc1?: string | Date;
    tmfc2?: string | Date;
    tmef1?: string | Date;
    tmef2?: string | Date;
    disp?: number;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: '1',
    };

    if (params?.stn) requestParams.stn = params.stn;
    if (params?.reg) requestParams.reg = params.reg;
    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmfc1) {
      requestParams.tmfc1 =
        typeof params.tmfc1 === 'string' ? params.tmfc1 : this.formatDateTime(params.tmfc1);
    }
    if (params?.tmfc2) {
      requestParams.tmfc2 =
        typeof params.tmfc2 === 'string' ? params.tmfc2 : this.formatDateTime(params.tmfc2);
    }
    if (params?.tmef1) {
      requestParams.tmef1 =
        typeof params.tmef1 === 'string' ? params.tmef1 : this.formatDateTime(params.tmef1);
    }
    if (params?.tmef2) {
      requestParams.tmef2 =
        typeof params.tmef2 === 'string' ? params.tmef2 : this.formatDateTime(params.tmef2);
    }

    return this.makeRequest<ForecastData>('fct_afs_do.php', requestParams);
  }

  // ============================================================================
  // Category 2: Village Forecast Grid Data (동네예보 격자자료)
  // ============================================================================

  /**
   * Get short-term village forecast grid data (documented endpoint)
   *
   * Documented endpoint: nph-dfs_shrt_grd (CGI)
   *
   * Provides short-term forecast grid data for village-level forecasts.
   * Issued 8 times daily (02, 05, 08, 11, 14, 17, 20, 23 KST).
   * Provides hourly forecasts up to 3 days.
   *
   * @param params - Query parameters
   * @param params.tmfc - Forecast issue time in YYYYMMDDHHmm format or Date object.
   *                      If undefined, returns all data. If '0', returns most recent.
   * @param params.tmef - Forecast valid time in YYYYMMDDHHmm format or Date object.
   *                      Hourly data provided up to 3 days ahead.
   * @param params.vars - Forecast variables (comma-separated).
   *                      TMP, TMX, TMN, UUU, VVV, VEC, WSD, SKY, PTY, POP, PCP, SNO, REH, WAV
   * @returns Village short-term forecast grid data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getVillageShortTermGrid({
   *   tmfc: '202402250500',
   *   tmef: '202402250600',
   *   vars: 'TMP,SKY,PTY'
   * });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
   */
  async getVillageShortTermGrid(params?: {
    tmfc?: string | Date;
    tmef?: string | Date;
    vars?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: '1',
    };

    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmef) {
      requestParams.tmef =
        typeof params.tmef === 'string' ? params.tmef : this.formatDateTime(params.tmef);
    }
    if (params?.vars) {
      requestParams.vars = params.vars;
    }

    return this.makeRequest<ForecastData>('nph-dfs_shrt_grd', requestParams, true);
  }

  /**
   * Get very short-term village forecast grid data (documented endpoint)
   *
   * Documented endpoint: nph-dfs_vsrt_grd (CGI)
   *
   * Provides ultra short-term forecast grid data for village-level forecasts.
   * Issued every 10 minutes. Provides hourly forecasts up to 6 hours ahead.
   *
   * @param params - Query parameters
   * @param params.tmfc - Forecast issue time in YYYYMMDDHHmm format or Date object.
   *                      Issued every 10 minutes.
   * @param params.tmef - Forecast valid time in YYYYMMDDHHmm format or Date object.
   *                      Hourly data up to 6 hours from issue time.
   * @param params.vars - Forecast variables (comma-separated).
   *                      T1H, UUU, VVV, VEC, WSD, SKY, LGT, PTY, RN1, REH
   * @returns Village very short-term forecast grid data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getVillageVeryShortTermGrid({
   *   tmfc: '202403011010',
   *   tmef: '202403011100',
   *   vars: 'T1H,SKY,PTY'
   * });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
   */
  async getVillageVeryShortTermGrid(params?: {
    tmfc?: string | Date;
    tmef?: string | Date;
    vars?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: '1',
    };

    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.tmef) {
      requestParams.tmef =
        typeof params.tmef === 'string' ? params.tmef : this.formatDateTime(params.tmef);
    }
    if (params?.vars) {
      requestParams.vars = params.vars;
    }

    return this.makeRequest<ForecastData>('nph-dfs_vsrt_grd', requestParams, true);
  }

  /**
   * Get village observation grid data (documented endpoint)
   *
   * Documented endpoint: nph-dfs_odam_grd (CGI)
   *
   * Provides current observation grid data for village-level analysis.
   * Since 2024-03-04 10:00, issued every 10 minutes.
   * Before that, issued every hour on the hour.
   *
   * @param params - Query parameters
   * @param params.tmfc - Observation time in YYYYMMDDHHmm format or Date object.
   * @param params.vars - Observation variables (comma-separated).
   *                      T1H, UUU, VVV, VEC, WSD, PTY, RN1, REH
   * @returns Village observation grid data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getVillageObservationGrid({
   *   tmfc: '202403051010',
   *   vars: 'T1H,RN1,REH'
   * });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
   */
  async getVillageObservationGrid(params?: {
    tmfc?: string | Date;
    vars?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: '1',
    };

    if (params?.tmfc) {
      requestParams.tmfc =
        typeof params.tmfc === 'string' ? params.tmfc : this.formatDateTime(params.tmfc);
    }
    if (params?.vars) {
      requestParams.vars = params.vars;
    }

    return this.makeRequest<ForecastData>('nph-dfs_odam_grd', requestParams, true);
  }

  /**
   * Convert village forecast grid numbers to latitude/longitude coordinates
   *
   * Documented endpoint: nph-dfs_xy_lonlat (CGI)
   *
   * Converts village forecast grid coordinates (x, y) to geographic coordinates
   * (latitude, longitude).
   *
   * @param x - Grid number (east-west direction). Range: 1 ~ 149
   * @param y - Grid number (north-south direction). Range: 1 ~ 253
   * @param help - Show help information. 0=no help, 1=show help (default: 1)
   * @returns Latitude and longitude coordinates for the grid point
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const coords = await client.convertGridToCoords(60, 127);
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
   */
  async convertGridToCoords(x: number, y: number, help = 1): Promise<ForecastData[]> {
    const requestParams = {
      x: String(x),
      y: String(y),
      help: String(help),
    };

    return this.makeRequest<ForecastData>('nph-dfs_xy_lonlat', requestParams, true);
  }

  /**
   * Convert latitude/longitude coordinates to village forecast grid numbers
   *
   * Documented endpoint: nph-dfs_xy_lonlat (CGI)
   *
   * Converts geographic coordinates (latitude, longitude) to the nearest
   * village forecast grid coordinates (x, y).
   *
   * @param lon - Longitude. Range: 123.310165 ~ 132.774963
   * @param lat - Latitude. Range: 31.651814 ~ 43.393490
   * @param help - Show help information. 0=no help, 1=show help (default: 1)
   * @returns Nearest village forecast grid numbers (x, y)
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const grid = await client.convertCoordsToGrid(127.5, 36.5);
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 2: Village Forecast Grid Data
   */
  async convertCoordsToGrid(lon: number, lat: number, help = 1): Promise<ForecastData[]> {
    const requestParams = {
      lon: String(lon),
      lat: String(lat),
      help: String(help),
    };

    return this.makeRequest<ForecastData>('nph-dfs_xy_lonlat', requestParams, true);
  }

  // ============================================================================
  // Category 3: Village Forecast Messages (동네예보 통보문)
  // ============================================================================

  /**
   * Get weather situation overview messages (documented endpoint)
   *
   * Documented endpoint: VilageFcstMsgService/getWthrSituation (OpenAPI)
   *
   * Retrieves weather situation overview messages issued by regional offices.
   * These messages provide general weather conditions and forecasts.
   *
   * @param params - Query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 10)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @param params.stnId - Issuing office code (108=KMA HQ, 109=Seoul, etc.)
   * @returns Weather situation overview message data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getWeatherSituation({ stnId: '108', numOfRows: 5 });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
   */
  async getWeatherSituation(params?: {
    pageNo?: number;
    numOfRows?: number;
    dataType?: string;
    stnId?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 10),
      dataType: params?.dataType ?? 'JSON',
    };

    if (params?.stnId) {
      requestParams.stnId = params.stnId;
    }

    return this.makeRequest<ForecastData>(
      'VilageFcstMsgService/getWthrSituation',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get land forecast messages (documented endpoint)
   *
   * Documented endpoint: VilageFcstMsgService/getLandFcst (OpenAPI)
   *
   * Retrieves land forecast messages for specific regions.
   * Messages contain detailed weather forecasts for land areas.
   *
   * @param params - Query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 10)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @param params.regId - Forecast region code (11A00101=Baengnyeong, 11B10101=Seoul, etc.)
   * @returns Land forecast message data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getLandForecastMessage({ regId: '11B10101', numOfRows: 5 });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
   */
  async getLandForecastMessage(params?: {
    pageNo?: number;
    numOfRows?: number;
    dataType?: string;
    regId?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 10),
      dataType: params?.dataType ?? 'JSON',
    };

    if (params?.regId) {
      requestParams.regId = params.regId;
    }

    return this.makeRequest<ForecastData>(
      'VilageFcstMsgService/getLandFcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get sea forecast messages (documented endpoint)
   *
   * Documented endpoint: VilageFcstMsgService/getSeaFcst (OpenAPI)
   *
   * Retrieves sea/marine forecast messages for specific regions.
   * Messages contain detailed weather forecasts for sea areas.
   *
   * @param params - Query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 10)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @param params.regId - Forecast region code (12A20100=West Sea Central, 12B20100=South Sea East, etc.)
   * @returns Sea forecast message data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getSeaForecastMessage({ regId: '12A20100', numOfRows: 5 });
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 3: Village Forecast Messages
   */
  async getSeaForecastMessage(params?: {
    pageNo?: number;
    numOfRows?: number;
    dataType?: string;
    regId?: string;
  }): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 10),
      dataType: params?.dataType ?? 'JSON',
    };

    if (params?.regId) {
      requestParams.regId = params.regId;
    }

    return this.makeRequest<ForecastData>(
      'VilageFcstMsgService/getSeaFcst',
      requestParams,
      false,
      true
    );
  }

  // ============================================================================
  // Category 4: Village Forecast API (동네예보 API)
  // ============================================================================

  /**
   * Get ultra short-term observation data (documented endpoint)
   *
   * Documented endpoint: VilageFcstInfoService_2.0/getUltraSrtNcst (OpenAPI)
   *
   * Retrieves current weather observation data for village forecast grid points.
   * Issued every hour on the hour.
   *
   * @param baseDate - Issue date in YYYYMMDD format (e.g., '20210628')
   * @param baseTime - Issue time in HHmm format (e.g., '0600')
   * @param nx - Forecast grid X coordinate (1~149)
   * @param ny - Forecast grid Y coordinate (1~253)
   * @param params - Optional query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 1000)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @returns Ultra short-term observation data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getUltraShortTermObservation('20210628', '0600', 55, 127);
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
   */
  async getUltraShortTermObservation(
    baseDate: string,
    baseTime: string,
    nx: number,
    ny: number,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      base_date: baseDate,
      base_time: baseTime,
      nx: String(nx),
      ny: String(ny),
    };

    return this.makeRequest<ForecastData>(
      'VilageFcstInfoService_2.0/getUltraSrtNcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get ultra short-term forecast data (documented endpoint)
   *
   * Documented endpoint: VilageFcstInfoService_2.0/getUltraSrtFcst (OpenAPI)
   *
   * Retrieves ultra short-term forecast data for village forecast grid points.
   * Issued every 30 minutes. Provides hourly forecasts up to 6 hours ahead.
   *
   * @param baseDate - Issue date in YYYYMMDD format (e.g., '20210628')
   * @param baseTime - Issue time in HHmm format (e.g., '0630')
   * @param nx - Forecast grid X coordinate (1~149)
   * @param ny - Forecast grid Y coordinate (1~253)
   * @param params - Optional query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 1000)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @returns Ultra short-term forecast data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getUltraShortTermForecast('20210628', '0630', 55, 127);
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
   */
  async getUltraShortTermForecast(
    baseDate: string,
    baseTime: string,
    nx: number,
    ny: number,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      base_date: baseDate,
      base_time: baseTime,
      nx: String(nx),
      ny: String(ny),
    };

    return this.makeRequest<ForecastData>(
      'VilageFcstInfoService_2.0/getUltraSrtFcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get village short-term forecast data (documented endpoint)
   *
   * Documented endpoint: VilageFcstInfoService_2.0/getVilageFcst (OpenAPI)
   *
   * Retrieves short-term forecast data for village forecast grid points.
   * Issued 8 times daily (02, 05, 08, 11, 14, 17, 20, 23 KST).
   * Provides forecasts up to 3 days ahead.
   *
   * @param baseDate - Issue date in YYYYMMDD format (e.g., '20210628')
   * @param baseTime - Issue time in HHmm format (e.g., '0500')
   * @param nx - Forecast grid X coordinate (1~149)
   * @param ny - Forecast grid Y coordinate (1~253)
   * @param params - Optional query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 1000)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @returns Village short-term forecast data
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getVillageForecast('20210628', '0500', 55, 127);
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
   */
  async getVillageForecast(
    baseDate: string,
    baseTime: string,
    nx: number,
    ny: number,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      base_date: baseDate,
      base_time: baseTime,
      nx: String(nx),
      ny: String(ny),
    };

    return this.makeRequest<ForecastData>(
      'VilageFcstInfoService_2.0/getVilageFcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get forecast version information (documented endpoint)
   *
   * Documented endpoint: VilageFcstInfoService_2.0/getFcstVersion (OpenAPI)
   *
   * Retrieves version information for village forecast data files.
   * Useful for tracking data updates and changes.
   *
   * @param ftype - File type: 'ODAM' (observation), 'VSRT' (ultra short-term), 'SHRT' (short-term)
   * @param basedatetime - Issue date/time in YYYYMMDDHHmm format (e.g., '202106280800')
   * @param params - Optional query parameters
   * @param params.pageNo - Page number (default: 1)
   * @param params.numOfRows - Number of results per page (default: 1000)
   * @param params.dataType - Response data format: 'XML' or 'JSON' (default: 'JSON')
   * @returns Forecast version information
   *
   * @example
   * ```typescript
   * const client = new ForecastClient({ authKey: 'your_key' });
   * const data = await client.getForecastVersion('SHRT', '202106280800');
   * ```
   *
   * Reference: API_ENDPOINT_Forecast.md - Category 4: Village Forecast API
   */
  async getForecastVersion(
    ftype: string,
    basedatetime: string,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      ftype: ftype,
      basedatetime: basedatetime,
    };

    return this.makeRequest<ForecastData>(
      'VilageFcstInfoService_2.0/getFcstVersion',
      requestParams,
      false,
      true
    );
  }

  // ============================================================
  // Category 5: 그래픽 예보 분포도 (Forecast Distribution Maps)
  // ============================================================

  /**
   * Get graphical short-term forecast distribution map
   *
   * Provides graphical distribution maps for short-term village forecasts.
   * Returns images showing spatial distribution of forecast variables.
   *
   * @param data0 - Data type (e.g., 'GEMD' for village forecast)
   * @param data1 - Variable type (e.g., 'PTY', 'TMP', 'SKY')
   * @param tmFc - Forecast issue time in 'YYYYMMDDHHmm' format or Date object
   * @param tmEf - Forecast valid time in 'YYYYMMDDHHmm' format or Date object
   * @param params - Optional parameters
   * @returns Graphical forecast distribution map data/image
   *
   * @example
   * ```typescript
   * const data = await client.getShortTermDistributionMap(
   *   'GEMD',
   *   'PTY',
   *   '202212221400',
   *   '202212260000'
   * );
   * ```
   */
  async getShortTermDistributionMap(
    data0: string,
    data1: string,
    tmFc: string | Date,
    tmEf: string | Date,
    params?: {
      dtm?: string;
      map?: string;
      mask?: string;
      color?: string;
      size?: number;
      effect?: string;
      overlay?: string;
      zoomRate?: number;
      zoomLevel?: number;
      zoomX?: string;
      zoomY?: string;
      autoMan?: string;
      mode?: string;
      interval?: number;
      rand?: number;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      data0: data0,
      data1: data1,
      tm_fc: typeof tmFc === 'string' ? tmFc : this.formatDateTime(tmFc),
      tm_ef: typeof tmEf === 'string' ? tmEf : this.formatDateTime(tmEf),
      dtm: params?.dtm ?? 'H0',
      map: params?.map ?? 'G1',
      mask: params?.mask ?? 'M',
      color: params?.color ?? 'E',
      size: String(params?.size ?? 600),
      effect: params?.effect ?? 'NTL',
      overlay: params?.overlay ?? 'S',
      zoom_rate: String(params?.zoomRate ?? 2),
      zoom_level: String(params?.zoomLevel ?? 0),
      zoom_x: params?.zoomX ?? '0000000',
      zoom_y: params?.zoomY ?? '0000000',
      auto_man: params?.autoMan ?? 'm',
      mode: params?.mode ?? 'I',
      interval: String(params?.interval ?? 1),
      rand: String(params?.rand ?? 1412),
      authKey: this.authKey,
    };

    // This uses typ03 API base URL
    const baseUrl = 'https://apihub.kma.go.kr/api/typ03/cgi/dfs';
    const url = `${baseUrl}/nph-dfs_shrt_ana_5d_test`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  /**
   * Get graphical very-short-term forecast distribution map
   *
   * Same as getShortTermDistributionMap but for very-short-term forecasts.
   *
   * @param data0 - Data type
   * @param data1 - Variable type
   * @param tmFc - Forecast issue time
   * @param tmEf - Forecast valid time
   * @param params - Optional parameters
   * @returns Graphical forecast distribution map data/image
   */
  async getVeryShortTermDistributionMap(
    data0: string,
    data1: string,
    tmFc: string | Date,
    tmEf: string | Date,
    params?: {
      dtm?: string;
      map?: string;
      mask?: string;
      color?: string;
      size?: number;
      effect?: string;
      overlay?: string;
      zoomRate?: number;
      zoomLevel?: number;
      zoomX?: string;
      zoomY?: string;
      autoMan?: string;
      mode?: string;
      interval?: number;
      rand?: number;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      data0: data0,
      data1: data1,
      tm_fc: typeof tmFc === 'string' ? tmFc : this.formatDateTime(tmFc),
      tm_ef: typeof tmEf === 'string' ? tmEf : this.formatDateTime(tmEf),
      dtm: params?.dtm ?? 'H0',
      map: params?.map ?? 'G1',
      mask: params?.mask ?? 'M',
      color: params?.color ?? 'E',
      size: String(params?.size ?? 600),
      effect: params?.effect ?? 'NTL',
      overlay: params?.overlay ?? 'S',
      zoom_rate: String(params?.zoomRate ?? 2),
      zoom_level: String(params?.zoomLevel ?? 0),
      zoom_x: params?.zoomX ?? '0000000',
      zoom_y: params?.zoomY ?? '0000000',
      auto_man: params?.autoMan ?? 'm',
      mode: params?.mode ?? 'I',
      interval: String(params?.interval ?? 1),
      rand: String(params?.rand ?? 1412),
      authKey: this.authKey,
    };

    // This uses typ03 API base URL (same endpoint as short-term)
    const baseUrl = 'https://apihub.kma.go.kr/api/typ03/cgi/dfs';
    const url = `${baseUrl}/nph-dfs_shrt_ana_5d_test`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  // ============================================================
  // Category 6: 동네예보 격자데이터 위경도 (Grid Coordinate Data)
  // ============================================================

  /**
   * Get grid latitude/longitude data
   *
   * @param params - Optional parameters
   * @returns Grid coordinate data
   *
   * @example
   * ```typescript
   * const data = await client.getGridLatlonData();
   * ```
   */
  async getGridLatlonData(
    params?: {
      mode?: string;
      help?: string;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      mode: params?.mode ?? 'DT',
      help: params?.help ?? '1',
      authKey: this.authKey,
    };

    const baseUrl = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/dfs';
    const url = `${baseUrl}/nph-dfs_latlon_api`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  /**
   * Download grid latitude/longitude NetCDF file
   *
   * @param params - Optional parameters
   * @returns NetCDF file data
   *
   * @example
   * ```typescript
   * const data = await client.downloadGridLatlonNetcdf();
   * ```
   */
  async downloadGridLatlonNetcdf(
    params?: {
      mode?: string;
      help?: string;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      mode: params?.mode ?? 'NC',
      help: params?.help ?? '1',
      authKey: this.authKey,
    };

    const baseUrl = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/dfs';
    const url = `${baseUrl}/nph-dfs_latlon_api`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  // ============================================================
  // Category 7: 중기예보 (Medium-term Forecast)
  // ============================================================

  /**
   * Get medium-term forecast regions
   *
   * @param params - Optional parameters
   * @returns Medium-term forecast region list
   */
  async getMediumTermRegion(
    params?: {
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    return this.makeRequest<ForecastData>(
      'fct_medm_reg.php',
      requestParams
    );
  }

  /**
   * Get medium-term forecast overview
   *
   * @param params - Optional parameters
   * @returns Medium-term forecast overview data
   */
  async getMediumTermOverview(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
      authKey?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'fct_afs_ws.php',
      requestParams
    );
  }

  /**
   * Get medium-term land forecast
   *
   * @param params - Optional parameters
   * @returns Medium-term land forecast data
   */
  async getMediumTermLand(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'fct_afs_wl.php',
      requestParams
    );
  }

  /**
   * Get medium-term temperature forecast
   *
   * @param params - Optional parameters
   * @returns Medium-term temperature forecast data
   */
  async getMediumTermTemperature(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'fct_afs_wc.php',
      requestParams
    );
  }

  /**
   * Get medium-term sea forecast
   *
   * @param params - Optional parameters
   * @returns Medium-term sea forecast data
   */
  async getMediumTermSea(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'fct_afs_wo.php',
      requestParams
    );
  }

  /**
   * Get medium-term sea forecast (OpenAPI)
   *
   * @param regId - Region ID
   * @param tmFc - Forecast time
   * @param params - Optional parameters
   * @returns Medium-term sea forecast data
   */
  async getMediumTermSeaForecast(
    regId: string,
    tmFc: string,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      regId: regId,
      tmFc: tmFc,
    };

    return this.makeRequest<ForecastData>(
      'MidFcstInfoService/getMidSeaFcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get medium-term temperature forecast (OpenAPI)
   *
   * @param regId - Region ID
   * @param tmFc - Forecast time
   * @param params - Optional parameters
   * @returns Medium-term temperature forecast data
   */
  async getMediumTermTemperatureForecast(
    regId: string,
    tmFc: string,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      regId: regId,
      tmFc: tmFc,
    };

    return this.makeRequest<ForecastData>(
      'MidFcstInfoService/getMidTa',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get medium-term land forecast (OpenAPI)
   *
   * @param regId - Region ID
   * @param tmFc - Forecast time
   * @param params - Optional parameters
   * @returns Medium-term land forecast data
   */
  async getMediumTermLandForecast(
    regId: string,
    tmFc: string,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      regId: regId,
      tmFc: tmFc,
    };

    return this.makeRequest<ForecastData>(
      'MidFcstInfoService/getMidLandFcst',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get medium-term outlook (OpenAPI)
   *
   * @param stnId - Station ID
   * @param tmFc - Forecast time
   * @param params - Optional parameters
   * @returns Medium-term outlook data
   */
  async getMediumTermOutlook(
    stnId: string,
    tmFc: string,
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
      stnId: stnId,
      tmFc: tmFc,
    };

    return this.makeRequest<ForecastData>(
      'MidFcstInfoService/getMidFcst',
      requestParams,
      false,
      true
    );
  }

  // ============================================================
  // Category 8: 기상특보 (Weather Warnings)
  // ============================================================

  /**
   * Get warning regions
   *
   * @param params - Optional parameters
   * @returns Warning region list
   */
  async getWarningRegion(
    params?: {
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    return this.makeRequest<ForecastData>(
      'wrn_reg.php',
      requestParams
    );
  }

  /**
   * Get warning data
   *
   * @param params - Optional parameters
   * @returns Warning data
   */
  async getWarningData(
    params?: {
      stn?: string;
      tm?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tm !== undefined) {
      requestParams.tm = typeof params.tm === 'string'
        ? params.tm
        : this.formatDateTime(params.tm);
    }

    return this.makeRequest<ForecastData>(
      'wrn_met_data.php',
      requestParams
    );
  }

  /**
   * Get weather information report
   *
   * @param params - Optional parameters
   * @returns Weather information data
   */
  async getWeatherInformation(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'wrn_inf_rpt.php',
      requestParams
    );
  }

  /**
   * Get weather commentary
   *
   * @param params - Optional parameters
   * @returns Weather commentary data
   */
  async getWeatherCommentary(
    params?: {
      stn?: string;
      tmfc?: string | Date;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.stn !== undefined) {
      requestParams.stn = params.stn;
    }
    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'wthr_cmt_rpt.php',
      requestParams
    );
  }

  /**
   * Get current warning status
   *
   * @param params - Optional parameters
   * @returns Current warning status data
   */
  async getCurrentWarningStatus(
    params?: {
      tmfc?: string | Date;
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'wrn_now_data.php',
      requestParams
    );
  }

  /**
   * Get current warning status (new version)
   *
   * @param params - Optional parameters
   * @returns Current warning status data (new format)
   */
  async getCurrentWarningStatusNew(
    params?: {
      tmfc?: string | Date;
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }

    return this.makeRequest<ForecastData>(
      'wrn_now_data_new.php',
      requestParams
    );
  }

  /**
   * Get warning image
   *
   * @param params - Optional parameters
   * @returns Warning image data
   */
  async getWarningImage(
    params?: {
      tm?: string | Date;
      size?: number;
      wrn?: string;
      map?: string;
      legend?: string;
      color?: string;
      lang?: string;
      disp?: number;
      help?: string;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      size: String(params?.size ?? 600),
      wrn: params?.wrn ?? '1',
      map: params?.map ?? '1',
      legend: params?.legend ?? '1',
      color: params?.color ?? '1',
      lang: params?.lang ?? 'ko',
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
      authKey: this.authKey,
    };

    if (params?.tm !== undefined) {
      requestParams.tm = typeof params.tm === 'string'
        ? params.tm
        : this.formatDateTime(params.tm);
    }

    const baseUrl = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/wrn';
    const url = `${baseUrl}/nph-wrn7`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  // ============================================================
  // Category 9: 영향예보 (Impact Forecast)
  // ============================================================

  /**
   * Get impact forecast status
   *
   * @param params - Optional parameters
   * @returns Impact forecast status data
   */
  async getImpactForecastStatus(
    params?: {
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    return this.makeRequest<ForecastData>(
      'ifs_fct_pstt.php',
      requestParams
    );
  }

  /**
   * Get impact risk level zone count
   *
   * @param params - Optional parameters
   * @returns Impact risk level zone count data
   */
  async getImpactRiskLevelZoneCount(
    params?: {
      tmfc?: string | Date;
      tmef?: string | Date;
      riskType?: string;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      help: params?.help ?? '1',
    };

    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }
    if (params?.tmef !== undefined) {
      requestParams.tmef = typeof params.tmef === 'string'
        ? params.tmef
        : this.formatDateTime(params.tmef);
    }
    if (params?.riskType !== undefined) {
      requestParams.risk_type = params.riskType;
    }

    return this.makeRequest<ForecastData>(
      'ifs_ilvl_zone_cnt.php',
      requestParams
    );
  }

  /**
   * Get impact risk level distribution map
   *
   * @param params - Optional parameters
   * @returns Impact risk level distribution map data
   */
  async getImpactRiskLevelDistributionMap(
    params?: {
      tmfc?: string | Date;
      tmef?: string | Date;
      riskType?: string;
      map?: string;
      legend?: string;
      size?: number;
      help?: string;
    }
  ): Promise<Record<string, unknown>> {
    const requestParams: Record<string, string> = {
      map: params?.map ?? '1',
      legend: params?.legend ?? '1',
      size: String(params?.size ?? 600),
      help: params?.help ?? '1',
      authKey: this.authKey,
    };

    if (params?.tmfc !== undefined) {
      requestParams.tmfc = typeof params.tmfc === 'string'
        ? params.tmfc
        : this.formatDateTime(params.tmfc);
    }
    if (params?.tmef !== undefined) {
      requestParams.tmef = typeof params.tmef === 'string'
        ? params.tmef
        : this.formatDateTime(params.tmef);
    }
    if (params?.riskType !== undefined) {
      requestParams.risk_type = params.riskType;
    }

    const baseUrl = 'https://apihub.kma.go.kr/api/typ01/cgi-bin/ifs';
    const url = `${baseUrl}/ifs_ilvl_dmap.php`;
    const response = await axios.get(url, { params: requestParams });
    return response.data;
  }

  // ============================================================
  // Category 10: 예,특보 구역정보 (Region Information)
  // ============================================================

  /**
   * Get forecast zone code (OpenAPI)
   *
   * @param params - Optional parameters
   * @returns Forecast zone code data
   */
  async getForecastZoneCode(
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
    };

    return this.makeRequest<ForecastData>(
      'WthrWrnInfoService/getFcstZoneCd',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get warning zone code (OpenAPI)
   *
   * @param params - Optional parameters
   * @returns Warning zone code data
   */
  async getWarningZoneCode(
    params?: {
      pageNo?: number;
      numOfRows?: number;
      dataType?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      pageNo: String(params?.pageNo ?? 1),
      numOfRows: String(params?.numOfRows ?? 1000),
      dataType: params?.dataType ?? 'JSON',
    };

    return this.makeRequest<ForecastData>(
      'WthrWrnInfoService/getWrnZoneCd',
      requestParams,
      false,
      true
    );
  }

  /**
   * Get AWS warning zone code
   *
   * @param params - Optional parameters
   * @returns AWS warning zone code data
   */
  async getAwsWarningZoneCode(
    params?: {
      disp?: number;
      help?: string;
    }
  ): Promise<ForecastData[]> {
    const requestParams: Record<string, unknown> = {
      disp: String(params?.disp ?? 0),
      help: params?.help ?? '1',
    };

    return this.makeRequest<ForecastData>(
      'wrn_reg_aws2.php',
      requestParams
    );
  }
}
