/**
 * Weather Radar Client
 * 기상 레이더 클라이언트
 */
import { BaseKMAClient, KMAClientConfig } from './base.js';

export interface RadarImage {
  tm: string;          // 관측시각
  radarId: string;     // 레이더ID
  imageData: string;   // 이미지 데이터
  imageType: string;   // 이미지 유형
}

export interface RadarReflectivity {
  tm: string;          // 관측시각
  lat: number;         // 위도
  lon: number;         // 경도
  ref: number;         // 반사도(dBZ)
}

export class RadarClient extends BaseKMAClient {
  constructor(config: KMAClientConfig) {
    super(config);
  }

  /**
   * Get radar image for a specific time
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param radarId - Radar station ID (default: 'KWK' for nationwide composite)
   */
  async getRadarImage(
    tm: string | Date,
    radarId: string = 'KWK'
  ): Promise<RadarImage[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<RadarImage>('kma_radar.php', {
      tm: timeStr,
      radar_id: radarId,
    });
  }

  /**
   * Get radar image sequence (animation)
   * @param tm1 - Start time in YYYYMMDDHHmm format or Date object
   * @param tm2 - End time in YYYYMMDDHHmm format or Date object
   * @param radarId - Radar station ID (default: 'KWK')
   */
  async getRadarImageSequence(
    tm1: string | Date,
    tm2: string | Date,
    radarId: string = 'KWK'
  ): Promise<RadarImage[]> {
    const time1Str = typeof tm1 === 'string' ? tm1 : this.formatDateTime(tm1);
    const time2Str = typeof tm2 === 'string' ? tm2 : this.formatDateTime(tm2);
    return this.makeRequest<RadarImage>('kma_radar_2.php', {
      tm1: time1Str,
      tm2: time2Str,
      radar_id: radarId,
    });
  }

  /**
   * Get radar reflectivity data for a specific location
   * @param tm - Observation time in YYYYMMDDHHmm format or Date object
   * @param lat - Latitude
   * @param lon - Longitude
   */
  async getRadarReflectivity(
    tm: string | Date,
    lat: number,
    lon: number
  ): Promise<RadarReflectivity[]> {
    const timeStr = typeof tm === 'string' ? tm : this.formatDateTime(tm);
    return this.makeRequest<RadarReflectivity>('kma_radar_ref.php', {
      tm: timeStr,
      lat: String(lat),
      lon: String(lon),
    });
  }
}
