/**
 * Integrated Meteorology Client
 * 융합기상 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface LightningData {
  tm: string;          // 관측시각
  lat: number;         // 위도
  lon: number;         // 경도
  intensity: number;   // 강도
  type: string;        // 낙뢰 유형
}

export interface WindProfilerData {
  tm: string;          // 관측시각
  stnId: string;       // 지점번호
  height: number;      // 고도(m)
  ws: number;          // 풍속(m/s)
  wd: number;          // 풍향(deg)
}

export class IntegratedClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get lightning detection data
   * @param tm1 - Start time in YYYYMMDDHHmm format
   * @param tm2 - End time in YYYYMMDDHHmm format
   */
  async getLightningData(
    tm1: string,
    tm2: string
  ): Promise<LightningData[]> {
    return this.makeRequest<LightningData>('lgt_kma_np3.php', {
      tm1,
      tm2,
    });
  }

  /**
   * Get wind profiler data
   * @param tm - Observation time in YYYYMMDDHHmm format
   * @param stn - Station ID (0 for all stations, default: 0)
   * @param mode - Data mode: 'L' (low) or 'H' (high), default: 'L'
   */
  async getWindProfilerData(
    tm: string,
    stn: number = 0,
    mode: string = 'L'
  ): Promise<WindProfilerData[]> {
    return this.makeRequest<WindProfilerData>('kma_wpf.php', {
      tm,
      stn: String(stn),
      mode,
    });
  }
}
