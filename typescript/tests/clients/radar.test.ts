/**
 * Radar Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { RadarClient, RadarImage } from '../../src/clients/radar';

describe('RadarClient', () => {
  let client: RadarClient;
  const mockImage: RadarImage = {
    tm: '202501011200',
    radarId: 'KWK',
    imageData: 'base64data',
    imageType: 'CAPPI',
  };

  beforeEach(() => {
    client = new RadarClient({ authKey: 'test-key' });
  });

  test('should get radar image', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockImage]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getRadarImage('202501011200', 'KWK');

    expect(result).toEqual([mockImage]);
    expect(mockMakeRequest).toHaveBeenCalledWith('kma_radar.php', {
      tm: '202501011200',
      radar_id: 'KWK',
    });
  });

  test('should get radar image sequence', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockImage, mockImage]));
    client['makeRequest'] = mockMakeRequest;

    await client.getRadarImageSequence('202501010000', '202501011200', 'KWK');

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_radar_2.php', {
      tm1: '202501010000',
      tm2: '202501011200',
      radar_id: 'KWK',
    });
  });

  test('should get radar reflectivity', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([]));
    client['makeRequest'] = mockMakeRequest;

    await client.getRadarReflectivity('202501011200', 37.5, 127.0);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_radar_ref.php', {
      tm: '202501011200',
      lat: '37.5',
      lon: '127',
    });
  });
});
