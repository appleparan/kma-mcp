/**
 * Weather Warning Client
 * 특보 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface WarningData {
  tmFc: string;        // 발표시각
  tmSeq: string;       // 순번
  warnVar: string;     // 특보종류
  warnStress: string;  // 특보단계
  regId: string;       // 지역코드
  regNm: string;       // 지역명
  t1: string;          // 발효시각
  t2: string;          // 해제시각
}

export class WarningClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get current active weather warnings
   */
  async getCurrentWarnings(): Promise<WarningData[]> {
    return this.makeRequest<WarningData>('kma_wn.php', {});
  }

  /**
   * Get warning history for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format
   * @param tm2 - End time in YYYYMMDDHHmm format
   */
  async getWarningHistory(
    tm1: string,
    tm2: string
  ): Promise<WarningData[]> {
    return this.makeRequest<WarningData>('kma_wn_2.php', {
      tm1,
      tm2,
    });
  }

  /**
   * Get special weather report
   * @param tm - Time in YYYYMMDDHHmm format
   */
  async getSpecialWeatherReport(tm: string): Promise<WarningData[]> {
    return this.makeRequest<WarningData>('kma_swr.php', {
      tm,
    });
  }
}
