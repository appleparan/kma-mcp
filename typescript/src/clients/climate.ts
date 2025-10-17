/**
 * Climate Statistics Client
 * 기후통계 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface ClimateNormal {
  stnId: string;       // 지점번호
  stnNm: string;       // 지점명
  avgTa: number;       // 평균기온(°C)
  avgTmax: number;     // 평균최고기온(°C)
  avgTmin: number;     // 평균최저기온(°C)
  sumRn: number;       // 강수량합(mm)
  avgWs: number;       // 평균풍속(m/s)
  avgHm: number;       // 평균습도(%)
}

export class ClimateClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get daily climate normal values for a date range
   * @param startMonth - Start month (1-12)
   * @param startDay - Start day (1-31)
   * @param endMonth - End month (1-12)
   * @param endDay - End day (1-31)
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyNormals(
    startMonth: number,
    startDay: number,
    endMonth: number,
    endDay: number,
    stn: number | string = 0
  ): Promise<ClimateNormal[]> {
    return this.makeRequest<ClimateNormal>('kma_clm_daily.php', {
      mm1: String(startMonth).padStart(2, '0'),
      dd1: String(startDay).padStart(2, '0'),
      mm2: String(endMonth).padStart(2, '0'),
      dd2: String(endDay).padStart(2, '0'),
      stn: String(stn),
    });
  }

  /**
   * Get 10-day (dekad) climate normal values
   * Each month is divided into three periods: 1 (1-10), 2 (11-20), 3 (21-end)
   * @param startMonth - Start month (1-12)
   * @param startPeriod - Start period (1-3)
   * @param endMonth - End month (1-12)
   * @param endPeriod - End period (1-3)
   * @param stn - Station ID (0 for all stations)
   */
  async getTenDayNormals(
    startMonth: number,
    startPeriod: number,
    endMonth: number,
    endPeriod: number,
    stn: number | string = 0
  ): Promise<ClimateNormal[]> {
    return this.makeRequest<ClimateNormal>('kma_clm_tenday.php', {
      mm1: String(startMonth).padStart(2, '0'),
      dd1: String(startPeriod),
      mm2: String(endMonth).padStart(2, '0'),
      dd2: String(endPeriod),
      stn: String(stn),
    });
  }

  /**
   * Get monthly climate normal values
   * @param startMonth - Start month (1-12)
   * @param endMonth - End month (1-12)
   * @param stn - Station ID (0 for all stations)
   */
  async getMonthlyNormals(
    startMonth: number,
    endMonth: number,
    stn: number | string = 0
  ): Promise<ClimateNormal[]> {
    return this.makeRequest<ClimateNormal>('kma_clm_month.php', {
      mm1: String(startMonth).padStart(2, '0'),
      mm2: String(endMonth).padStart(2, '0'),
      stn: String(stn),
    });
  }

  /**
   * Get annual climate normal values
   * @param stn - Station ID (0 for all stations)
   */
  async getAnnualNormals(
    stn: number | string = 0
  ): Promise<ClimateNormal[]> {
    return this.makeRequest<ClimateNormal>('kma_clm_year.php', {
      stn: String(stn),
    });
  }

  /**
   * Get climate normals with flexible period specification
   * @param periodType - Type of period ('daily', 'tenday', 'monthly', 'annual')
   * @param startMonth - Start month (required for daily, tenday, monthly)
   * @param startDay - Start day (required for daily) or period (1-3 for tenday)
   * @param endMonth - End month (required for daily, tenday, monthly)
   * @param endDay - End day (required for daily) or period (1-3 for tenday)
   * @param stn - Station ID (0 for all stations)
   */
  async getNormalsByPeriod(
    periodType: 'daily' | 'tenday' | 'monthly' | 'annual',
    startMonth?: number,
    startDay?: number,
    endMonth?: number,
    endDay?: number,
    stn: number | string = 0
  ): Promise<ClimateNormal[]> {
    switch (periodType) {
      case 'daily':
        if (
          startMonth === undefined ||
          startDay === undefined ||
          endMonth === undefined ||
          endDay === undefined
        ) {
          throw new Error(
            'Daily normals require startMonth, startDay, endMonth, endDay'
          );
        }
        return this.getDailyNormals(startMonth, startDay, endMonth, endDay, stn);
      case 'tenday':
        if (
          startMonth === undefined ||
          startDay === undefined ||
          endMonth === undefined ||
          endDay === undefined
        ) {
          throw new Error(
            'Ten-day normals require startMonth, startPeriod, endMonth, endPeriod'
          );
        }
        return this.getTenDayNormals(startMonth, startDay, endMonth, endDay, stn);
      case 'monthly':
        if (startMonth === undefined || endMonth === undefined) {
          throw new Error('Monthly normals require startMonth and endMonth');
        }
        return this.getMonthlyNormals(startMonth, endMonth, stn);
      case 'annual':
        return this.getAnnualNormals(stn);
      default:
        throw new Error(
          `Invalid periodType: ${periodType}. Must be 'daily', 'tenday', 'monthly', or 'annual'`
        );
    }
  }
}
