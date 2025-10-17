/**
 * Dust (Yellow Dust PM10) Client
 * 황사관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface DustObservation {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  pm10: number; // PM10 농도(μg/m³)
  pm10Flag: string; // PM10 QC 플래그
}

export class DustClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get hourly PM10 observation data for a single time
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyData(tm: string | Date, stn: number | string = 0): Promise<DustObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<DustObservation>('kma_pm10.php', {
      tm: timeStr,
      stn: String(stn),
    });
  }

  /**
   * Get hourly PM10 observation data for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn: number | string = 0
  ): Promise<DustObservation[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<DustObservation>('kma_pm10_2.php', {
      tm1: time1Str,
      tm2: time2Str,
      stn: String(stn),
    });
  }

  /**
   * Get daily PM10 observation data for a single day
   * @param tm - Date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyData(tm: string | Date, stn: number | string = 0): Promise<DustObservation[]> {
    const dateStr = typeof tm === 'string' ? tm : this.formatDateTime(tm, false);
    return this.makeRequest<DustObservation>('kma_pm10_day.php', {
      tm: dateStr,
      stn: String(stn),
    });
  }

  /**
   * Get daily PM10 observation data for a date range
   * @param tm1 - Start date in YYYYMMDD format or Date object
   * @param tm2 - End date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn: number | string = 0
  ): Promise<DustObservation[]> {
    const date1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1, false);
    const date2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2, false);
    return this.makeRequest<DustObservation>('kma_pm10_day2.php', {
      tm1: date1Str,
      tm2: date2Str,
      stn: String(stn),
    });
  }
}
