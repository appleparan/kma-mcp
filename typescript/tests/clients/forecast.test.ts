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

  // Category 2: Village Forecast Grid Data Tests
  test('should get village short-term forecast grid data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getVillageShortTermGrid({
      tmfc: '202402250500',
      tmef: '202402250600',
      vars: 'TMP,SKY',
    });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'nph-dfs_shrt_grd',
      {
        help: '1',
        tmfc: '202402250500',
        tmef: '202402250600',
        vars: 'TMP,SKY',
      },
      true
    );
  });

  test('should get village very short-term forecast grid data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getVillageVeryShortTermGrid({
      tmfc: '202403011010',
      tmef: '202403011100',
      vars: 'T1H,SKY',
    });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'nph-dfs_vsrt_grd',
      {
        help: '1',
        tmfc: '202403011010',
        tmef: '202403011100',
        vars: 'T1H,SKY',
      },
      true
    );
  });

  test('should get village observation grid data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getVillageObservationGrid({ tmfc: '202403051010', vars: 'T1H,RN1' });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'nph-dfs_odam_grd',
      {
        help: '1',
        tmfc: '202403051010',
        vars: 'T1H,RN1',
      },
      true
    );
  });

  test('should convert grid numbers to coordinates', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.convertGridToCoords(60, 127);

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'nph-dfs_xy_lonlat',
      {
        x: '60',
        y: '127',
        help: '1',
      },
      true
    );
  });

  test('should convert coordinates to grid numbers', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.convertCoordsToGrid(127.5, 36.5);

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'nph-dfs_xy_lonlat',
      {
        lon: '127.5',
        lat: '36.5',
        help: '1',
      },
      true
    );
  });

  // Category 3: Village Forecast Messages Tests
  test('should get weather situation messages', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWeatherSituation({ stnId: '108', numOfRows: 5 });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstMsgService/getWthrSituation',
      {
        pageNo: '1',
        numOfRows: '5',
        dataType: 'JSON',
        stnId: '108',
      },
      false,
      true
    );
  });

  test('should get land forecast messages', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getLandForecastMessage({ regId: '11B10101', numOfRows: 5 });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstMsgService/getLandFcst',
      {
        pageNo: '1',
        numOfRows: '5',
        dataType: 'JSON',
        regId: '11B10101',
      },
      false,
      true
    );
  });

  test('should get sea forecast messages', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getSeaForecastMessage({ regId: '12A20100', numOfRows: 5 });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstMsgService/getSeaFcst',
      {
        pageNo: '1',
        numOfRows: '5',
        dataType: 'JSON',
        regId: '12A20100',
      },
      false,
      true
    );
  });
});
