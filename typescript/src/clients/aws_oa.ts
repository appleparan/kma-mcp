/**
 * AWS OA (AWS Objective Analysis) Client
 * AWS 객관분석 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface AWSOAData {
  tm: string; // 분석시각
  x: number; // 경도
  y: number; // 위도
  ta: number; // 기온(°C)
  rn: number; // 강수량(mm)
  ws: number; // 풍속(m/s)
  wd: number; // 풍향(deg)
  hm: number; // 습도(%)
  pa: number; // 기압(hPa)
}

export class AWSOAClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get AWS objective analysis data for a specific location and time
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param x - Longitude coordinate
   * @param y - Latitude coordinate
   */
  async getAnalysisData(tm: string | Date, x: number, y: number): Promise<AWSOAData[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<AWSOAData>('kma_awsoa.php', {
      tm: timeStr,
      x: String(x),
      y: String(y),
    });
  }

  /**
   * Get AWS objective analysis data for a location over a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param x - Longitude coordinate
   * @param y - Latitude coordinate
   */
  async getAnalysisPeriod(
    tm1: string | Date,
    tm2: string | Date,
    x: number,
    y: number
  ): Promise<AWSOAData[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<AWSOAData>('kma_awsoa_2.php', {
      tm1: time1Str,
      tm2: time2Str,
      x: String(x),
      y: String(y),
    });
  }
}
