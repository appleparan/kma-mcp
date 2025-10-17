/**
 * Earthquake Monitoring Client
 * 지진 모니터링 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface EarthquakeData {
  tm: string;          // 발생시각
  loc: string;         // 발생위치
  lat: number;         // 위도
  lon: number;         // 경도
  mag: number;         // 규모
  dep: number;         // 깊이(km)
  int: string;         // 진도
}

export class EarthquakeClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get the most recent earthquake information
   * @param tm - Reference time in YYYYMMDDHHmm format or Date object (default: now)
   * @param disp - Output format (0/1/2, default: 0)
   */
  async getRecentEarthquake(
    tm?: string | Date,
    disp: number = 0
  ): Promise<EarthquakeData[]> {
    const timeStr = tm
      ? typeof tm === 'string'
        ? tm
        : this.formatDateTime(tm)
      : new Date().toISOString().replace(/[-:]/g, '').slice(0, 12);

    return this.makeRequest<EarthquakeData>('eqk_now.php', {
      tm: timeStr,
      disp: String(disp),
    });
  }

  /**
   * Get earthquake list for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param disp - Output format (0/1/2, default: 0)
   */
  async getEarthquakeList(
    tm1: string | Date,
    tm2: string | Date,
    disp: number = 0
  ): Promise<EarthquakeData[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);

    return this.makeRequest<EarthquakeData>('eqk_list.php', {
      tm1: time1Str,
      tm2: time2Str,
      disp: String(disp),
    });
  }
}
