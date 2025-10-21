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

  // Category 1: Short-term Forecast Tests
  test('should get short-term forecast by region', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getShortTermRegion({ tmfc: '202501011200' });

    expect(result).toEqual([mockForecast]);
    expect(mockMakeRequest).toHaveBeenCalledWith('fct_shrt_reg.php', {
      disp: '0',
      help: '1',
      tmfc: '202501011200',
    });
  });

  test('should get short-term forecast overview', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getShortTermOverview({ tmfc: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_ds.php', {
      disp: '0',
      tmfc: '202501011200',
    });
  });

  test('should get short-term land forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getShortTermLand({ tmfc: '202501011200', reg: '11B00000' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_dl.php', {
      disp: '0',
      help: '1',
      tmfc: '202501011200',
      reg: '11B00000',
    });
  });

  test('should get short-term land forecast v2', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getShortTermLandV2({ tmfc1: '202501010000', tmfc2: '202501020000' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_dl2.php', {
      disp: '0',
      help: '1',
      tmfc1: '202501010000',
      tmfc2: '202501020000',
    });
  });

  test('should get short-term sea forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getShortTermSea({ tmef1: '202501011200', tmef2: '202501021200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_do.php', {
      disp: '0',
      help: '1',
      tmef1: '202501011200',
      tmef2: '202501021200',
    });
  });
});
