/**
 * Snow Depth Client
 * 적설관측 클라이언트
 *
 * The snow depth observation system monitors snow accumulation
 * and provides critical data for winter weather analysis,
 * transportation safety, and disaster prevention.
 *
 * Snow depth types:
 * - tot: Total snow depth (적설)
 * - day: Daily new snow (일신적설)
 * - 3hr: 3-hour new snow (3시간 신적설)
 * - 24h: 24-hour new snow (24시간 신적설)
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface SnowObservation {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  sd: number; // 적설(cm)
  sdQcflg: string; // 적설 QC 플래그
}

export type SnowDepthType = 'tot' | 'day' | '3hr' | '24h';
export type MaxSnowDepthType = 'tot' | 'day';

export class SnowClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get snow depth observation data (documented endpoint)
   *
   * Documented endpoint: kma_snow1.php
   *
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param sdType - Snow depth type:
   *   - 'tot': Total snow depth (적설)
   *   - 'day': Daily new snow (일신적설)
   *   - '3hr': 3-hour new snow
   *   - '24h': 24-hour new snow
   * @returns Snow depth observation data
   *
   * @example
   * ```typescript
   * const client = new SnowClient({ authKey: 'your_key' });
   * // Get total snow depth
   * const data = await client.getSnowDepth('201412051800', 'tot');
   * // Get daily new snow
   * const data2 = await client.getSnowDepth('201412051800', 'day');
   * ```
   */
  async getSnowDepth(tm: string | Date, sdType: SnowDepthType = 'tot'): Promise<SnowObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<SnowObservation>('kma_snow1.php', {
      sd: sdType,
      tm: timeStr,
      help: '1',
    });
  }

  /**
   * Get snow depth data for a period (documented endpoint)
   *
   * Documented endpoint: kma_snow2.php
   *
   * @param tm - End time in YYYYMMDDHHmm format or Date object
   * @param tmSt - Start time in YYYYMMDDHHmm format or Date object
   * @param snow - Snow parameter (default: 0)
   * @returns Snow depth data for the period
   *
   * @example
   * ```typescript
   * const client = new SnowClient({ authKey: 'your_key' });
   * const data = await client.getSnowPeriod('201412051800', '201412040100');
   * ```
   */
  async getSnowPeriod(
    tm: string | Date,
    tmSt: string | Date,
    snow: number = 0
  ): Promise<SnowObservation[]> {
    const tmStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    const tmStStr = typeof tmSt === 'string' ? tmSt : this.formatDateTime(tmSt);
    return this.makeRequest<SnowObservation>('kma_snow2.php', {
      tm: tmStr,
      tm_st: tmStStr,
      snow: String(snow),
      help: '1',
    });
  }

  /**
   * Get maximum snow depth for a period (documented endpoint)
   *
   * Documented endpoint: kma_snow_day.php
   *
   * @param tm - End date in YYYYMMDD format or Date object
   * @param tmSt - Start date in YYYYMMDD format or Date object
   * @param sdType - Snow depth type:
   *   - 'tot': Maximum total snow depth (최심적설)
   *   - 'day': Maximum daily new snow (최심신적설)
   * @param stn - Station number (0 for all stations)
   * @param snow - Snow parameter (default: 0)
   * @returns Maximum snow depth data for the period
   *
   * @example
   * ```typescript
   * const client = new SnowClient({ authKey: 'your_key' });
   * // Get maximum total snow depth
   * const data = await client.getMaxSnowDepth('20150131', '20150125', 'tot');
   * // Get maximum daily new snow
   * const data2 = await client.getMaxSnowDepth('20150131', '20150125', 'day');
   * ```
   */
  async getMaxSnowDepth(
    tm: string | Date,
    tmSt: string | Date,
    sdType: MaxSnowDepthType = 'tot',
    stn: number | string = 0,
    snow: number = 0
  ): Promise<SnowObservation[]> {
    const tmStr = typeof tm === 'string' ? tm : this.formatDateTime(tm, false);
    const tmStStr = typeof tmSt === 'string' ? tmSt : this.formatDateTime(tmSt, false);
    return this.makeRequest<SnowObservation>('kma_snow_day.php', {
      sd: sdType,
      tm: tmStr,
      tm_st: tmStStr,
      stn: String(stn),
      snow: String(snow),
      help: '1',
    });
  }
}
