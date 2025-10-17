/**
 * Climate Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { ClimateClient, ClimateNormal } from '../../src/clients/climate';

describe('ClimateClient', () => {
  let client: ClimateClient;
  const mockNormal: ClimateNormal = {
    stnId: '108',
    stnNm: '서울',
    avgTa: 12.5,
    avgTmax: 18.0,
    avgTmin: 7.0,
    sumRn: 45.5,
    avgWs: 2.5,
    avgHm: 65.0,
  };

  beforeEach(() => {
    client = new ClimateClient({ authKey: 'test-key' });
  });

  test('should get daily normals', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockNormal]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getDailyNormals(1, 1, 1, 31, 108);

    expect(result).toEqual([mockNormal]);
    expect(mockMakeRequest).toHaveBeenCalledWith('kma_clm_daily.php', {
      mm1: '01',
      dd1: '01',
      mm2: '01',
      dd2: '31',
      stn: '108',
    });
  });

  test('should get ten-day normals', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockNormal]));
    client['makeRequest'] = mockMakeRequest;

    await client.getTenDayNormals(1, 1, 1, 3, 108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_clm_tenday.php', {
      mm1: '01',
      dd1: '1',
      mm2: '01',
      dd2: '3',
      stn: '108',
    });
  });

  test('should get monthly normals', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockNormal]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMonthlyNormals(1, 12, 108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_clm_month.php', {
      mm1: '01',
      mm2: '12',
      stn: '108',
    });
  });

  test('should get annual normals', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockNormal]));
    client['makeRequest'] = mockMakeRequest;

    await client.getAnnualNormals(108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_clm_year.php', {
      stn: '108',
    });
  });
});
