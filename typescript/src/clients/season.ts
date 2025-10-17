/**
 * Season (Seasonal/Phenological Observation) Client
 * 계절관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface SeasonObservation {
  year: string; // 연도
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  event: string; // 관측 이벤트 (벚꽃개화, 단풍 등)
  date: string; // 관측일
}

export class SeasonClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get seasonal observation data for a specific year
   * @param year - Year in YYYY format
   * @param stn - Station ID (0 for all stations)
   */
  async getObservationData(
    year: number | string,
    stn: number | string = 0
  ): Promise<SeasonObservation[]> {
    return this.makeRequest<SeasonObservation>('kma_season.php', {
      year: String(year),
      stn: String(stn),
    });
  }

  /**
   * Get seasonal observation data for a year range
   * @param startYear - Start year in YYYY format
   * @param endYear - End year in YYYY format
   * @param stn - Station ID (0 for all stations)
   */
  async getObservationPeriod(
    startYear: number | string,
    endYear: number | string,
    stn: number | string = 0
  ): Promise<SeasonObservation[]> {
    return this.makeRequest<SeasonObservation>('kma_season_2.php', {
      year1: String(startYear),
      year2: String(endYear),
      stn: String(stn),
    });
  }
}
