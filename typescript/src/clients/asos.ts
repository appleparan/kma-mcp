/**
 * ASOS (Automated Synoptic Observing System) Client
 * 종관기상관측 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface ASOSObservation {
  tm: string; // 관측시각
  stnId: string; // 지점번호
  stnNm: string; // 지점명
  ta: number; // 기온(°C)
  taQcflg: string; // 기온 QC 플래그
  rn: number; // 강수량(mm)
  rnQcflg: string; // 강수량 QC 플래그
  ws: number; // 풍속(m/s)
  wsQcflg: string; // 풍속 QC 플래그
  wd: number; // 풍향(deg)
  wdQcflg: string; // 풍향 QC 플래그
  hm: number; // 습도(%)
  hmQcflg: string; // 습도 QC 플래그
  pa: number; // 현지기압(hPa)
  paQcflg: string; // 현지기압 QC 플래그
  ps: number; // 해면기압(hPa)
  psQcflg: string; // 해면기압 QC 플래그
  ss: number; // 일조(hr)
  ssQcflg: string; // 일조 QC 플래그
  icsr: number; // 일사(MJ/m²)
  icsrQcflg: string; // 일사 QC 플래그
  dsnw: number; // 적설(cm)
  dsnwQcflg: string; // 적설 QC 플래그
}

export class ASOSClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get hourly ASOS observation data for a single time
   * @param tm - Time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyData(tm: string | Date, stn = 0): Promise<ASOSObservation[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<ASOSObservation>('kma_sfctm2.php', {
      tm: timeStr,
      stn,
    });
  }

  /**
   * Get hourly ASOS observation data for a time period
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getHourlyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn = 0
  ): Promise<ASOSObservation[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<ASOSObservation>('kma_sfctm2.php', {
      tm1: time1Str,
      tm2: time2Str,
      stn,
    });
  }

  /**
   * Get daily ASOS observation data for a single date
   * @param tm - Date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyData(tm: string | Date, stn = 0): Promise<ASOSObservation[]> {
    const dateStr = typeof tm === 'string' ? tm : this.formatDateTime(tm, false);
    return this.makeRequest<ASOSObservation>('kma_sfcdd2.php', {
      tm: dateStr,
      stn,
    });
  }

  /**
   * Get daily ASOS observation data for a date range
   * @param tm1 - Start date in YYYYMMDD format or Date object
   * @param tm2 - End date in YYYYMMDD format or Date object
   * @param stn - Station ID (0 for all stations)
   */
  async getDailyPeriod(
    tm1: string | Date,
    tm2: string | Date,
    stn = 0
  ): Promise<ASOSObservation[]> {
    const date1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1, false);
    const date2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2, false);
    return this.makeRequest<ASOSObservation>('kma_sfcdd2.php', {
      tm1: date1Str,
      tm2: date2Str,
      stn,
    });
  }

  /**
   * Get specific weather element data
   * @param tm1 - Start time
   * @param tm2 - End time
   * @param stn - Station ID
   * @param element - Element code (e.g., 'ta' for temperature, 'rn' for precipitation)
   */
  async getElementData(
    tm1: string | Date,
    tm2: string | Date,
    stn: number,
    element: string
  ): Promise<ASOSObservation[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<ASOSObservation>('kma_sfcelm.php', {
      tm1: time1Str,
      tm2: time2Str,
      stn,
      elm: element,
    });
  }
}
