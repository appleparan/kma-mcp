/**
 * Satellite Data Client
 * 위성 데이터 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface SatelliteFile {
  fileName: string; // 파일명
  fileSize: number; // 파일크기
  fileDate: string; // 파일날짜
  sat: string; // 위성명
  area: string; // 지역코드
  product: string; // 산출물
}

export interface SatelliteImagery {
  level: string; // 데이터레벨
  product: string; // 산출물/채널
  area: string; // 지역코드
  tm: string; // 관측시각
  data: string; // 이미지 데이터
}

export class SatelliteClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super({ ...config, timeout: config.timeout || 60000 }); // Longer timeout for large files
  }

  /**
   * Get list of available satellite files
   * @param sat - Satellite identifier (default: 'GK2A')
   * @param vars - Variable/product type (default: 'L1B')
   * @param area - Region code (default: 'FD' for Full Disk)
   * @param fmt - File format (default: 'NetCDF')
   * @param tm - Time filter in YYYYMMDDHHmm format (optional)
   */
  async getSatelliteFileList(
    sat: string = 'GK2A',
    vars: string = 'L1B',
    area: string = 'FD',
    fmt: string = 'NetCDF',
    tm?: string
  ): Promise<SatelliteFile[]> {
    const params: Record<string, string> = {
      sat,
      vars,
      area,
      fmt,
    };
    if (tm) {
      params.tm = tm;
    }
    return this.makeRequest<SatelliteFile>('sat_file_list.php', params);
  }

  /**
   * Get satellite imagery data
   * @param level - Data level ('l1b' or 'l2')
   * @param product - Product type/channel
   * @param area - Area code (FD, KO, EA, ELA, TP)
   * @param tm - Time in YYYYMMDDHHmm format
   */
  async getSatelliteImagery(
    level: string,
    product: string,
    area: string,
    tm: string
  ): Promise<SatelliteImagery[]> {
    return this.makeRequest<SatelliteImagery>('sat_file_down2.php', {
      lvl: level,
      dat: product,
      are: area,
      tm,
      typ: 'img',
    });
  }
}
