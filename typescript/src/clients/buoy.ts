/**
 * Marine Buoy Client
 * 해양기상관측 (부이) 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface BuoyObservation {
  tm: string; // 관측시각
  buoyId: string; // 부이번호
  buoyNm: string; // 부이이름
  lat: number; // 위도
  lon: number; // 경도
  ta: number; // 기온(°C)
  wh: number; // 파고(m)
  wt: number; // 수온(°C)
  ws: number; // 풍속(m/s)
  wd: number; // 풍향(deg)
}

export class BuoyClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get buoy observation data for a specific time
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param buoyId - Buoy ID (0 for all buoys)
   */
  async getBuoyData(tm: string | Date, buoyId: number | string = 0): Promise<BuoyObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<BuoyObservation>('kma_buoy.php', {
      tm: timeStr,
      buoy: String(buoyId),
    });
  }

  /**
   * Get buoy observation data for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param buoyId - Buoy ID (0 for all buoys)
   */
  async getBuoyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    buoyId: number | string = 0
  ): Promise<BuoyObservation[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<BuoyObservation>('kma_buoy_2.php', {
      tm1: time1Str,
      tm2: time2Str,
      buoy: String(buoyId),
    });
  }

  /**
   * Get comprehensive marine data (buoys, tide, wave)
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   */
  async getComprehensiveMarineData(tm: string | Date): Promise<BuoyObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<BuoyObservation>('kma_marine_all.php', {
      tm: timeStr,
    });
  }
}
