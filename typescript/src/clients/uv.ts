/**
 * UV (Ultraviolet Radiation) Client
 * 자외선관측 클라이언트
 *
 * This client provides access to KMA's UV Radiation observation API.
 * UV observations monitor ultraviolet A and erythema B radiation levels.
 *
 * Note: Only get_observation_data() uses the documented API endpoint.
 * Other methods are deprecated and raise errors as they use undocumented endpoints.
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface UVObservation {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  uva: number; // UVA (320-400nm)
  uvaQcflg: string; // UVA QC 플래그
  uvb: number; // Erythema UVB (280-320nm)
  uvbQcflg: string; // UVB QC 플래그
}

export class UVClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get UV radiation observation data for a single time.
   *
   * This is the only documented API endpoint for UV observations.
   * UV observations monitor ultraviolet A and erythema B radiation levels.
   *
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param stn - Station number (0 for all stations)
   * @returns UV radiation observation data
   *
   * @example
   * ```typescript
   * const client = new UVClient({ authKey: 'your_key' });
   * const data = await client.getObservationData('202203211500');
   * // Or using Date object
   * const data2 = await client.getObservationData(new Date(2022, 2, 21, 15, 0));
   * ```
   *
   * @remarks
   * - UV observation stations: Anmyeondo, Gosan, Ulleungdo, Seoul,
   *   Pohang, Mokpo, Gangneung (7 stations)
   * - Measures UVA (320-400nm) and erythema UVB (280-320nm)
   * - Data available from January 1994 to present
   */
  async getObservationData(tm: string | Date, stn: number | string = 0): Promise<UVObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<UVObservation>('kma_sfctm_uv.php', {
      tm: timeStr,
      stn: String(stn),
      help: '1',
    });
  }

  /**
   * @deprecated Legacy method - not documented in official API.
   * Use getObservationData() instead for UV observation data.
   *
   * @throws {Error} This endpoint is not documented in the official KMA API.
   */
  async getHourlyData(_tm: string | Date, _stn: number | string = 0): Promise<UVObservation[]> {
    throw new Error(
      'getHourlyData() is not documented in the official KMA API. ' +
        'Use getObservationData(tm, stn) instead for UV observation data.'
    );
  }

  /**
   * @deprecated Legacy method - not documented in official API.
   * Period queries may need to be implemented using multiple calls to getObservationData().
   *
   * @throws {Error} This endpoint is not documented in the official KMA API.
   */
  async getHourlyPeriod(
    _tm1: string | Date,
    _tm2: string | Date,
    _stn: number | string = 0
  ): Promise<UVObservation[]> {
    throw new Error(
      'getHourlyPeriod() is not documented in the official KMA API. ' +
        'Period queries may need to be implemented using multiple calls to getObservationData().'
    );
  }

  /**
   * @deprecated Legacy method - not documented in official API.
   *
   * @throws {Error} This endpoint is not documented in the official KMA API.
   */
  async getDailyData(_tm: string | Date, _stn: number | string = 0): Promise<UVObservation[]> {
    throw new Error('getDailyData() is not documented in the official KMA API.');
  }

  /**
   * @deprecated Legacy method - not documented in official API.
   *
   * @throws {Error} This endpoint is not documented in the official KMA API.
   */
  async getDailyPeriod(
    _tm1: string | Date,
    _tm2: string | Date,
    _stn: number | string = 0
  ): Promise<UVObservation[]> {
    throw new Error('getDailyPeriod() is not documented in the official KMA API.');
  }
}
