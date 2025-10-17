/**
 * AMOS (Aerodrome Meteorological Observation Station) Client
 * 항공기상관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface AMOSObservation {
  tm: string; // 관측시각
  icao: string; // ICAO 코드
  airportNm: string; // 공항명
  ta: number; // 기온(°C)
  td: number; // 이슬점온도(°C)
  ws: number; // 풍속(m/s)
  wd: number; // 풍향(deg)
  pa: number; // 기압(hPa)
  vis: number; // 시정(m)
}

export interface AMDARData {
  tm: string; // 관측시각
  flightId: string; // 항공편명
  lat: number; // 위도
  lon: number; // 경도
  alt: number; // 고도(ft)
  ta: number; // 기온(°C)
  ws: number; // 풍속(m/s)
  wd: number; // 풍향(deg)
}

export class AMOSClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get aerodrome meteorological observations
   * @param tm - Observation time in YYYYMMDDHHmm format
   * @param dtm - Data time range in minutes before tm (default: 60)
   */
  async getAirportObservations(tm: string, dtm: number = 60): Promise<AMOSObservation[]> {
    return this.makeRequest<AMOSObservation>('amos.php', {
      tm,
      dtm: String(dtm),
    });
  }

  /**
   * Get AMDAR aircraft meteorological data
   * @param tm1 - Start time in YYYYMMDDHHmm format
   * @param tm2 - End time in YYYYMMDDHHmm format
   * @param st - Station type filter (default: 'E' for all)
   */
  async getAmdarData(tm1: string, tm2: string, st: string = 'E'): Promise<AMDARData[]> {
    return this.makeRequest<AMDARData>('amdar_kma.php', {
      tm1,
      tm2,
      st,
    });
  }
}
