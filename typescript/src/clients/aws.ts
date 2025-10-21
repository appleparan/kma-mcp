/**
 * AWS (Automated Weather Station) Client
 * 방재기상관측 클라이언트
 *
 * The AWS system provides real-time weather observations from automated weather
 * stations for disaster prevention purposes. It typically has more observation
 * points than ASOS and focuses on real-time monitoring.
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface AWSObservation {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  ta: number; // 기온(°C)
  taQcflg: string; // 기온 QC 플래그
  rn: number; // 강수량(mm)
  rnQcflg: string; // 강수량 QC 플래그
  ws: number; // 풍속(m/s)
  wsQcflg: string; // 풍속 QC 플래그
  wd: number; // 풍향(deg)
  wdQcflg: string; // 풍향 QC 플래그
  hm: number; // 습도(%)
  hmQcflg: string; // 습도 QC 플래그
  pa: number; // 현지기압(hPa)
  paQcflg: string; // 현지기압 QC 플래그
}

export interface AWSLandSurfaceTemperature {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  lst: number; // 지표온도(°C)
  lstQcflg: string; // 지표온도 QC 플래그
}

export interface AWSCloudData {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  clfm: number; // 운저고도(m)
  clfmQcflg: string; // 운저고도 QC 플래그
  ca: number; // 운량(0-10)
  caQcflg: string; // 운량 QC 플래그
}

export class AWSClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get AWS minutely observation data (documented endpoint)
   *
   * Documented endpoint: nph-aws2_min
   *
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object (optional, defaults to tm2)
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object (optional, defaults to current time)
   * @param stn - Station number (0 for all stations)
   * @param disp - Display format: 0 = Fortran format (default), 1 = Excel format
   * @returns Minutely AWS observation data
   *
   * @example
   * ```typescript
   * const client = new AWSClient({ authKey: 'your_key' });
   * // Get data for a specific time
   * const data = await client.getMinutelyData(undefined, '202302010900');
   * // Get data for a period
   * const data2 = await client.getMinutelyData('202302010800', '202302010900');
   * ```
   */
  async getMinutelyData(
    tm1?: string | Date,
    tm2?: string | Date,
    stn: number | string = 0,
    disp: number = 0
  ): Promise<AWSObservation[]> {
    const params: Record<string, unknown> = {
      stn: String(stn),
      disp: String(disp),
      help: '1',
    };

    if (tm1) {
      params.tm1 = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    }
    if (tm2) {
      params.tm2 = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    }

    return this.makeRequest<AWSObservation>('nph-aws2_min', params, true);
  }

  /**
   * Get AWS land surface temperature data (documented endpoint)
   *
   * Documented endpoint: nph-aws2_min_lst
   *
   * @param tm - Time in YYYYMMDDHHmm format (optional, defaults to current time)
   * @param tm1 - Start time (optional, defaults to tm2)
   * @param tm2 - End time (optional, defaults to current time)
   * @param stn - Station number (0 for all stations)
   * @param disp - Display format: 0 = Fortran, 1 = Excel
   * @returns Land surface temperature data
   *
   * @example
   * ```typescript
   * const client = new AWSClient({ authKey: 'your_key' });
   * const data = await client.getLandSurfaceTemperature(undefined, undefined, '202302010900');
   * ```
   */
  async getLandSurfaceTemperature(
    tm?: string | Date,
    tm1?: string | Date,
    tm2?: string | Date,
    stn: number | string = 0,
    disp: number = 0
  ): Promise<AWSLandSurfaceTemperature[]> {
    const params: Record<string, unknown> = {
      stn: String(stn),
      disp: String(disp),
      help: '1',
    };

    if (tm) {
      params.tm = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    }
    if (tm1) {
      params.tm1 = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    }
    if (tm2) {
      params.tm2 = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    }

    return this.makeRequest<AWSLandSurfaceTemperature>('nph-aws2_min_lst', params, true);
  }

  /**
   * Get AWS cloud height and amount data (documented endpoint)
   *
   * Documented endpoint: nph-aws2_min_cloud
   *
   * @param tm1 - Start time (optional, defaults to tm2)
   * @param tm2 - End time (optional, defaults to current time)
   * @param stn - Station number (0 for all stations)
   * @param itv - Time interval in minutes (optional)
   * @param sms - Smoothing flag, 0 or 1 (optional)
   * @param disp - Display format: 0 = Fortran, 1 = Excel
   * @returns Cloud height and amount data
   *
   * @example
   * ```typescript
   * const client = new AWSClient({ authKey: 'your_key' });
   * const data = await client.getCloudData(undefined, '202302010900', 0, 10);
   * ```
   */
  async getCloudData(
    tm1?: string | Date,
    tm2?: string | Date,
    stn: number | string = 0,
    itv?: number,
    sms?: number,
    disp: number = 0
  ): Promise<AWSCloudData[]> {
    const params: Record<string, unknown> = {
      stn: String(stn),
      disp: String(disp),
      help: '1',
    };

    if (tm1) {
      params.tm1 = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    }
    if (tm2) {
      params.tm2 = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    }
    if (itv !== undefined) {
      params.itv = String(itv);
    }
    if (sms !== undefined) {
      params.sms = String(sms);
    }

    return this.makeRequest<AWSCloudData>('nph-aws2_min_cloud', params, true);
  }

  /**
   * Get AWS cloud data with period average (documented endpoint)
   *
   * Documented endpoint: nph-aws2_min_ca2
   *
   * @param tm1 - Start time (optional, defaults to tm2)
   * @param tm2 - End time (optional, defaults to current time)
   * @param stn - Station number (0 for all stations)
   * @param itv - Time interval in minutes (default: 10)
   * @param range - Accumulation period for average in minutes (default: 10)
   * @param disp - Display format: 0 = Fortran, 1 = Excel
   * @returns Cloud average data for the period
   *
   * @example
   * ```typescript
   * const client = new AWSClient({ authKey: 'your_key' });
   * const data = await client.getCloudAverage(undefined, '201503221200', 0, 10, 10);
   * ```
   */
  async getCloudAverage(
    tm1?: string | Date,
    tm2?: string | Date,
    stn: number | string = 0,
    itv: number = 10,
    range: number = 10,
    disp: number = 0
  ): Promise<AWSCloudData[]> {
    const params: Record<string, unknown> = {
      stn: String(stn),
      itv: String(itv),
      range: String(range),
      disp: String(disp),
      help: '1',
    };

    if (tm1) {
      params.tm1 = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    }
    if (tm2) {
      params.tm2 = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    }

    return this.makeRequest<AWSCloudData>('nph-aws2_min_ca2', params, true);
  }

  /**
   * Get AWS cloud data with period min/max (documented endpoint)
   *
   * Documented endpoint: nph-aws2_min_ca3
   *
   * @param tm1 - Start time (optional, defaults to tm2)
   * @param tm2 - End time (optional, defaults to current time)
   * @param stn - Station number (0 for all stations)
   * @param itv - Time interval in minutes (default: 10)
   * @param range - Accumulation period for min/max in minutes (default: 10)
   * @param disp - Display format: 0 = Fortran, 1 = Excel
   * @returns Cloud min/max data for the period
   *
   * @example
   * ```typescript
   * const client = new AWSClient({ authKey: 'your_key' });
   * const data = await client.getCloudMinMax(undefined, '201503221200', 0, 10, 10);
   * ```
   */
  async getCloudMinMax(
    tm1?: string | Date,
    tm2?: string | Date,
    stn: number | string = 0,
    itv: number = 10,
    range: number = 10,
    disp: number = 0
  ): Promise<AWSCloudData[]> {
    const params: Record<string, unknown> = {
      stn: String(stn),
      itv: String(itv),
      range: String(range),
      disp: String(disp),
      help: '1',
    };

    if (tm1) {
      params.tm1 = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    }
    if (tm2) {
      params.tm2 = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    }

    return this.makeRequest<AWSCloudData>('nph-aws2_min_ca3', params, true);
  }
}
