/**
 * Earthquake Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { EarthquakeClient, EarthquakeData } from '../../src/clients/earthquake';

describe('EarthquakeClient', () => {
  let client: EarthquakeClient;
  const mockEarthquake: EarthquakeData = {
    tm: '202501011200',
    loc: '경북 경주시',
    lat: 36.0,
    lon: 129.0,
    mag: 3.5,
    dep: 10.0,
    int: 'II',
  };

  beforeEach(() => {
    client = new EarthquakeClient({ authKey: 'test-key' });
  });

  test('should get recent earthquake', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockEarthquake]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getRecentEarthquake('202501011200', 0);

    expect(result).toEqual([mockEarthquake]);
    expect(mockMakeRequest).toHaveBeenCalledWith(
      'eqk_now.php',
      expect.objectContaining({
        disp: '0',
      })
    );
  });

  test('should get earthquake list', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockEarthquake]));
    client['makeRequest'] = mockMakeRequest;

    await client.getEarthquakeList('202501010000', '202501011200', 0);

    expect(mockMakeRequest).toHaveBeenCalledWith('eqk_list.php', {
      tm1: '202501010000',
      tm2: '202501011200',
      disp: '0',
    });
  });
});
