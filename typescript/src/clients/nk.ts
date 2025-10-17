/**
 * NK (North Korea Meteorological Observation) Client
 * 북한기상관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface NKObservation {
  tm: string;          // 관측시각
  stnId: string;       // 지점번호
  stnNm: string;       // 지점명
  ta: number;          // 기온(°C)
  rn: number;          // 강수량(mm)
  ws: number;          // 풍속(m/s)
  wd: number;          // 풍향(deg)
  hm: number;          // 습도(%)
  pa: number;          // 기압(hPa)
}

export class NKClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get hourly North Korea meteorological observation data for a single time
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyData(
    tm: string | Date,
    stn: number | string = 0
  ): Promise<NKObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<NKObservation>('kma_nkobs.php', {
      tm: timeStr,
      stn: String(stn),
    });
  }

  /**
   * Get hourly North Korea meteorological observation data for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn: number | string = 0
  ): Promise<NKObservation[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<NKObservation>('kma_nkobs_2.php', {
      tm1: time1Str,
      tm2: time2Str,
      stn: String(stn),
    });
  }

  /**
   * Get daily North Korea meteorological observation data for a single day
   * @param tm - Date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyData(
    tm: string | Date,
    stn: number | string = 0
  ): Promise<NKObservation[]> {
    const dateStr = typeof tm === 'string' ? tm : this.formatDateTime(tm, false);
    return this.makeRequest<NKObservation>('kma_nkobs_day.php', {
      tm: dateStr,
      stn: String(stn),
    });
  }

  /**
   * Get daily North Korea meteorological observation data for a date range
   * @param tm1 - Start date in YYYYMMDD format or Date object
   * @param tm2 - End date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn: number | string = 0
  ): Promise<NKObservation[]> {
    const date1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1, false);
    const date2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2, false);
    return this.makeRequest<NKObservation>('kma_nkobs_day2.php', {
      tm1: date1Str,
      tm2: date2Str,
      stn: String(stn),
    });
  }
}
