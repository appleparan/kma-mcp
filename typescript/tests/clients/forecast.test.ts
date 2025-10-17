/**
 * Forecast Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { ForecastClient, ForecastData } from '../../src/clients/forecast';

describe('ForecastClient', () => {
  let client: ForecastClient;
  const mockForecast: ForecastData = {
    tmFc: '202501011200',
    regId: '11B00000',
    taMin: 5,
    taMax: 15,
    wf: '맑음',
    rnSt: 10,
  };

  beforeEach(() => {
    client = new ForecastClient({ authKey: 'test-key' });
  });

  test('should get short-term forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getShortTermForecast('202501011200', 0);

    expect(result).toEqual([mockForecast]);
    expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcfct.php', {
      tm_fc: '202501011200',
      stn: '0',
    });
  });

  test('should get medium-term forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermForecast('202501011200', 0);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_mtfcst.php', {
      tm_fc: '202501011200',
      stn: '0',
    });
  });

  test('should get weekly forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWeeklyForecast('202501011200', 0);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_wkfcst.php', {
      tm_fc: '202501011200',
      stn: '0',
    });
  });
});
