/**
 * Dust Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { DustClient, DustObservation } from '../../src/clients/dust';

describe('DustClient', () => {
  let client: DustClient;
  const mockObservation: DustObservation = {
    tm: '202501011200',
    stnId: '108',
    stnNm: '서울',
    pm10: 45.5,
    pm10Flag: '0',
  };

  beforeEach(() => {
    client = new DustClient({ authKey: 'test-key' });
  });

  test('should get hourly PM10 data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getHourlyData('202501011200', 108);

    expect(result).toEqual([mockObservation]);
    expect(mockMakeRequest).toHaveBeenCalledWith('kma_pm10.php', {
      tm: '202501011200',
      stn: '108',
    });
  });

  test('should get hourly period PM10 data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
    client['makeRequest'] = mockMakeRequest;

    await client.getHourlyPeriod('202501010000', '202501011200', 108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_pm10_2.php', {
      tm1: '202501010000',
      tm2: '202501011200',
      stn: '108',
    });
  });

  test('should get daily PM10 data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
    client['makeRequest'] = mockMakeRequest;

    await client.getDailyData('20250101', 108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_pm10_day.php', {
      tm: '20250101',
      stn: '108',
    });
  });

  test('should get daily period PM10 data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
    client['makeRequest'] = mockMakeRequest;

    await client.getDailyPeriod('20250101', '20250131', 108);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_pm10_day2.php', {
      tm1: '20250101',
      tm2: '20250131',
      stn: '108',
    });
  });
});
