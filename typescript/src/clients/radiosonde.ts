/**
 * Radiosonde (Upper Air) Client
 * 고층기상관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface RadiosondeData {
  tm: string;          // 관측시각
  stnId: string;       // 지점번호
  pres: number;        // 기압(hPa)
  height: number;      // 고도(m)
  ta: number;          // 기온(°C)
  td: number;          // 이슬점온도(°C)
  ws: number;          // 풍속(m/s)
  wd: number;          // 풍향(deg)
}

export interface StabilityIndex {
  stnId: string;       // 지점번호
  ki: number;          // K-Index
  li: number;          // Lifted Index
  si: number;          // Showalter Index
  tt: number;          // Total Totals
}

export class RadiosondeClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get upper air observation data
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getUpperAirData(
    tm: string | Date,
    stn: number | string = 0
  ): Promise<RadiosondeData[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<RadiosondeData>('kma_radiosonde.php', {
      tm: timeStr,
      stn: String(stn),
    });
  }

  /**
   * Get atmospheric stability indices
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getStabilityIndices(
    tm: string | Date,
    stn: number | string = 0
  ): Promise<StabilityIndex[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<StabilityIndex>('kma_stability.php', {
      tm: timeStr,
      stn: String(stn),
    });
  }

  /**
   * Get maximum altitude data
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getMaximumAltitudeData(
    tm: string | Date,
    stn: number | string = 0
  ): Promise<RadiosondeData[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<RadiosondeData>('kma_radiosonde_max.php', {
      tm: timeStr,
      stn: String(stn),
    });
  }
}
