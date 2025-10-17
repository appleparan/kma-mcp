/**
 * Weather Forecast Client
 * 예보 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface ForecastData {
  tmFc: string; // 예보시각
  regId: string; // 지역코드
  taMin: number; // 최저기온(°C)
  taMax: number; // 최고기온(°C)
  wf: string; // 날씨
  rnSt: number; // 강수확률(%)
}

export class ForecastClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get short-term weather forecast (up to 3 days)
   * @param tmFc - Forecast time in YYYYMMDDHHmm format
   * @param stn - Station/region code (0 for all regions)
   */
  async getShortTermForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_sfcfct.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }

  /**
   * Get medium-term weather forecast (3-10 days)
   * @param tmFc - Forecast time in YYYYMMDDHHmm format
   * @param stn - Station/region code (0 for all regions)
   */
  async getMediumTermForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_mtfcst.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }

  /**
   * Get weekly weather forecast
   * @param tmFc - Forecast time in YYYYMMDDHHmm format
   * @param stn - Station/region code (0 for all regions)
   */
  async getWeeklyForecast(tmFc: string, stn: number | string = 0): Promise<ForecastData[]> {
    return this.makeRequest<ForecastData>('kma_wkfcst.php', {
      tm_fc: tmFc,
      stn: String(stn),
    });
  }
}
