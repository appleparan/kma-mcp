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
  // Legacy methods - marked as undocumented
  // ============================================================================

  /**
   * @deprecated This endpoint (kma_sfcfct.php) is not documented in the official API.
   * Consider using getShortTermRegion() with the documented fct_shrt_reg.php endpoint.
   *
   * Get short-term weather forecast (up to 3 days) - undocumented endpoint
   */
  async getShortTermForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_sfcfct.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }

  /**
   * @deprecated This endpoint (kma_mtfcst.php) is not documented in the official API.
   *
   * Get medium-term weather forecast (3-10 days) - undocumented endpoint
   */
  async getMediumTermForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_mtfcst.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }

  /**
   * @deprecated This endpoint (kma_wkfcst.php) is not documented in the official API.
   *
   * Get weekly weather forecast - undocumented endpoint
   */
  async getWeeklyForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_wkfcst.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }
}
