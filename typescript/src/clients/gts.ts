/**
 * GTS (Global Telecommunication System) Client
 * 국제기상통신망 (전지구관측) 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface SynopObservation {
  tm: string;          // 관측시각
  stnId: string;       // 지점번호
  lat: number;         // 위도
  lon: number;         // 경도
  ta: number;          // 기온(°C)
  pa: number;          // 기압(hPa)
  ws: number;          // 풍속(m/s)
  wd: number;          // 풍향(deg)
}

export interface ShipObservation {
  tm: string;          // 관측시각
  shipId: string;      // 선박식별부호
  lat: number;         // 위도
  lon: number;         // 경도
  ta: number;          // 기온(°C)
  wt: number;          // 수온(°C)
  ws: number;          // 풍속(m/s)
  wd: number;          // 풍향(deg)
}

export interface ChartData {
  tm: string;          // 발표시각
  chartType: string;   // 천기도 종류
  imageData: string;   // 이미지 데이터
}

export class GTSClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get SYNOP (land station) observations
   * @param tm - Observation time in YYYYMMDDHHmm format
   */
  async getSynopObservations(tm: string): Promise<SynopObservation[]> {
    return this.makeRequest<SynopObservation>('gts_synop.php', {
      tm,
    });
  }

  /**
   * Get ship observations
   * @param tm - Observation time in YYYYMMDDHHmm format
   */
  async getShipObservations(tm: string): Promise<ShipObservation[]> {
    return this.makeRequest<ShipObservation>('gts_ship.php', {
      tm,
    });
  }

  /**
   * Get buoy observations from GTS network
   * @param tm - Observation time in YYYYMMDDHHmm format
   */
  async getBuoyObservations(tm: string): Promise<SynopObservation[]> {
    return this.makeRequest<SynopObservation>('gts_buoy.php', {
      tm,
    });
  }

  /**
   * Get aircraft reports (AIREP)
   * @param tm - Observation time in YYYYMMDDHHmm format
   */
  async getAircraftReports(tm: string): Promise<SynopObservation[]> {
    return this.makeRequest<SynopObservation>('gts_airep.php', {
      tm,
    });
  }

  /**
   * Get surface weather chart
   * @param tm - Chart time in YYYYMMDDHHmm format
   */
  async getSurfaceChart(tm: string): Promise<ChartData[]> {
    return this.makeRequest<ChartData>('gts_sfc_chart.php', {
      tm,
    });
  }

  /**
   * Get SYNOP chart (observation plot)
   * @param tm - Chart time in YYYYMMDDHHmm format
   */
  async getSynopChart(tm: string): Promise<ChartData[]> {
    return this.makeRequest<ChartData>('gts_synop_chart.php', {
      tm,
    });
  }
}
