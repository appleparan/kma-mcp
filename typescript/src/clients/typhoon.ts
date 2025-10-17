/**
 * Typhoon Information Client
 * 태풍 정보 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface TyphoonInfo {
  typId: string;       // 태풍번호
  typNm: string;       // 태풍이름
  typIntlNm: string;   // 국제명
  tm: string;          // 발표시각
  lat: number;         // 위도
  lon: number;         // 경도
  pres: number;        // 중심기압(hPa)
  ws: number;          // 최대풍속(m/s)
  mvDir: string;       // 이동방향
  mvSpd: number;       // 이동속도(km/h)
}

export class TyphoonClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get information on currently active typhoons
   */
  async getCurrentTyphoons(): Promise<TyphoonInfo[]> {
    return this.makeRequest<TyphoonInfo>('kma_typ.php', {});
  }

  /**
   * Get detailed information for a specific typhoon
   * @param typhoonId - Typhoon identification number (e.g., '2501')
   */
  async getTyphoonById(typhoonId: string): Promise<TyphoonInfo[]> {
    return this.makeRequest<TyphoonInfo>('kma_typ_dtl.php', {
      typ_id: typhoonId,
    });
  }

  /**
   * Get forecast track for a specific typhoon
   * @param typhoonId - Typhoon identification number
   */
  async getTyphoonForecast(typhoonId: string): Promise<TyphoonInfo[]> {
    return this.makeRequest<TyphoonInfo>('kma_typ_fcst.php', {
      typ_id: typhoonId,
    });
  }

  /**
   * Get typhoon history for a specific year
   * @param year - Year in YYYY format
   */
  async getTyphoonHistory(year: number | string): Promise<TyphoonInfo[]> {
    return this.makeRequest<TyphoonInfo>('kma_typ_hist.php', {
      year: String(year),
    });
  }
}
