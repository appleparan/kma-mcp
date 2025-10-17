/**
 * Station Information Client
 * 지상관측 지점정보 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface StationInfo {
  stnId: string;       // 지점번호
  stnNm: string;       // 지점명
  lat: number;         // 위도
  lon: number;         // 경도
  stnEl: number;       // 해발고도(m)
  stnType: string;     // 지점유형
  startDate: string;   // 운영시작일
}

export class StationClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get ASOS station information
   * @param stn - Station ID (0 for all stations)
   */
  async getAsosStations(
    stn: number | string = 0
  ): Promise<StationInfo[]> {
    return this.makeRequest<StationInfo>('kma_stnlist.php', {
      stn: String(stn),
    });
  }

  /**
   * Get AWS station information
   * @param stn - Station ID (0 for all stations)
   */
  async getAwsStations(
    stn: number | string = 0
  ): Promise<StationInfo[]> {
    return this.makeRequest<StationInfo>('kma_aws_stnlist.php', {
      stn: String(stn),
    });
  }
}
