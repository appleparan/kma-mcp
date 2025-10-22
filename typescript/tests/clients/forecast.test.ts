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

  // Category 4: Village Forecast API Tests
  test('should get ultra short-term observation data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getUltraShortTermObservation('20210628', '0600', 55, 127);

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstInfoService_2.0/getUltraSrtNcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        base_date: '20210628',
        base_time: '0600',
        nx: '55',
        ny: '127',
      },
      false,
      true
    );
  });

  test('should get ultra short-term forecast data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getUltraShortTermForecast('20210628', '0630', 55, 127);

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstInfoService_2.0/getUltraSrtFcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        base_date: '20210628',
        base_time: '0630',
        nx: '55',
        ny: '127',
      },
      false,
      true
    );
  });

  test('should get village forecast data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getVillageForecast('20210628', '0500', 55, 127);

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstInfoService_2.0/getVilageFcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        base_date: '20210628',
        base_time: '0500',
        nx: '55',
        ny: '127',
      },
      false,
      true
    );
  });

  test('should get forecast version information', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getForecastVersion('SHRT', '202106280800');

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'VilageFcstInfoService_2.0/getFcstVersion',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        ftype: 'SHRT',
        basedatetime: '202106280800',
      },
      false,
      true
    );
  });

  // Category 5: Forecast Distribution Maps Tests
  test('should get short-term distribution map', async () => {
    const mockAxiosGet = mock(() =>
      Promise.resolve({ data: { image: 'test_image_data' } })
    );
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.getShortTermDistributionMap(
      'GEMD',
      'PTY',
      '202212221400',
      '202212260000'
    );

    expect(mockAxiosGet).toHaveBeenCalled();
    const callArgs = mockAxiosGet.mock.calls[0];
    expect(callArgs[0]).toBe(
      'https://apihub.kma.go.kr/api/typ03/cgi/dfs/nph-dfs_shrt_ana_5d_test'
    );
    expect(callArgs[1].params.data0).toBe('GEMD');
    expect(callArgs[1].params.data1).toBe('PTY');
  });

  test('should get very short-term distribution map', async () => {
    const mockAxiosGet = mock(() =>
      Promise.resolve({ data: { image: 'test_image_data' } })
    );
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.getVeryShortTermDistributionMap(
      'GEMD',
      'TMP',
      '202212221400',
      '202212260000'
    );

    expect(mockAxiosGet).toHaveBeenCalled();
  });

  // Category 6: Grid Coordinate Data Tests
  test('should get grid lat/lon data', async () => {
    const mockAxiosGet = mock(() => Promise.resolve({ data: { grid: 'data' } }));
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.getGridLatlonData();

    expect(mockAxiosGet).toHaveBeenCalled();
    const callArgs = mockAxiosGet.mock.calls[0];
    expect(callArgs[0]).toBe(
      'https://apihub.kma.go.kr/api/typ01/cgi-bin/dfs/nph-dfs_latlon_api'
    );
  });

  test('should download grid lat/lon NetCDF', async () => {
    const mockAxiosGet = mock(() => Promise.resolve({ data: { nc: 'data' } }));
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.downloadGridLatlonNetcdf();

    expect(mockAxiosGet).toHaveBeenCalled();
    const callArgs = mockAxiosGet.mock.calls[0];
    expect(callArgs[1].params.mode).toBe('NC');
  });

  // Category 7: Medium-term Forecast Tests
  test('should get medium-term region', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermRegion();

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_medm_reg.php', {
      disp: '0',
      help: '1',
    });
  });

  test('should get medium-term overview', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermOverview({ stn: '108', tmfc: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_ws.php', {
      help: '1',
      stn: '108',
      tmfc: '202501011200',
    });
  });

  test('should get medium-term land forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermLand({ stn: '108' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_wl.php', {
      help: '1',
      stn: '108',
    });
  });

  test('should get medium-term temperature forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermTemperature({ stn: '108' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_wc.php', {
      help: '1',
      stn: '108',
    });
  });

  test('should get medium-term sea forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermSea({ stn: '108' });

    expect(mockMakeRequest).toHaveBeenCalledWith('fct_afs_wo.php', {
      help: '1',
      stn: '108',
    });
  });

  test('should get medium-term sea forecast (OpenAPI)', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermSeaForecast('11B00000', '202501011800');

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'MidFcstInfoService/getMidSeaFcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        regId: '11B00000',
        tmFc: '202501011800',
      },
      false,
      true
    );
  });

  test('should get medium-term temperature forecast (OpenAPI)', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermTemperatureForecast('11B10101', '202501011800');

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'MidFcstInfoService/getMidTa',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        regId: '11B10101',
        tmFc: '202501011800',
      },
      false,
      true
    );
  });

  test('should get medium-term land forecast (OpenAPI)', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermLandForecast('11B00000', '202501011800');

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'MidFcstInfoService/getMidLandFcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        regId: '11B00000',
        tmFc: '202501011800',
      },
      false,
      true
    );
  });

  test('should get medium-term outlook', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getMediumTermOutlook('108', '202501011800');

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'MidFcstInfoService/getMidFcst',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
        stnId: '108',
        tmFc: '202501011800',
      },
      false,
      true
    );
  });

  // Category 8: Weather Warnings Tests
  test('should get warning region', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWarningRegion();

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_reg.php', {
      disp: '0',
      help: '1',
    });
  });

  test('should get warning data', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWarningData({ stn: '108', tm: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_met_data.php', {
      help: '1',
      stn: '108',
      tm: '202501011200',
    });
  });

  test('should get weather information', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWeatherInformation({ stn: '108', tmfc: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_inf_rpt.php', {
      help: '1',
      stn: '108',
      tmfc: '202501011200',
    });
  });

  test('should get weather commentary', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWeatherCommentary({ stn: '108' });

    expect(mockMakeRequest).toHaveBeenCalledWith('wthr_cmt_rpt.php', {
      help: '1',
      stn: '108',
    });
  });

  test('should get current warning status', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getCurrentWarningStatus({ tmfc: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_now_data.php', {
      disp: '0',
      help: '1',
      tmfc: '202501011200',
    });
  });

  test('should get current warning status (new)', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getCurrentWarningStatusNew({ tmfc: '202501011200' });

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_now_data_new.php', {
      disp: '0',
      help: '1',
      tmfc: '202501011200',
    });
  });

  test('should get warning image', async () => {
    const mockAxiosGet = mock(() =>
      Promise.resolve({ data: { image: 'warning_image' } })
    );
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.getWarningImage({ tm: '202501011200' });

    expect(mockAxiosGet).toHaveBeenCalled();
    const callArgs = mockAxiosGet.mock.calls[0];
    expect(callArgs[0]).toBe(
      'https://apihub.kma.go.kr/api/typ01/cgi-bin/wrn/nph-wrn7'
    );
  });

  // Category 9: Impact Forecast Tests
  test('should get impact forecast status', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getImpactForecastStatus();

    expect(mockMakeRequest).toHaveBeenCalledWith('ifs_fct_pstt.php', {
      disp: '0',
      help: '1',
    });
  });

  test('should get impact risk level zone count', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getImpactRiskLevelZoneCount({
      tmfc: '202501011200',
      tmef: '202501021200',
      riskType: 'HEAT',
    });

    expect(mockMakeRequest).toHaveBeenCalledWith('ifs_ilvl_zone_cnt.php', {
      help: '1',
      tmfc: '202501011200',
      tmef: '202501021200',
      risk_type: 'HEAT',
    });
  });

  test('should get impact risk level distribution map', async () => {
    const mockAxiosGet = mock(() =>
      Promise.resolve({ data: { map: 'impact_map' } })
    );
    const axios = await import('axios');
    axios.default.get = mockAxiosGet;

    await client.getImpactRiskLevelDistributionMap({
      tmfc: '202501011200',
      riskType: 'HEAT',
    });

    expect(mockAxiosGet).toHaveBeenCalled();
    const callArgs = mockAxiosGet.mock.calls[0];
    expect(callArgs[0]).toBe(
      'https://apihub.kma.go.kr/api/typ01/cgi-bin/ifs/ifs_ilvl_dmap.php'
    );
  });

  // Category 10: Region Information Tests
  test('should get forecast zone code', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getForecastZoneCode({ numOfRows: 100 });

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'WthrWrnInfoService/getFcstZoneCd',
      {
        pageNo: '1',
        numOfRows: '100',
        dataType: 'JSON',
      },
      false,
      true
    );
  });

  test('should get warning zone code', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getWarningZoneCode();

    expect(mockMakeRequest).toHaveBeenCalledWith(
      'WthrWrnInfoService/getWrnZoneCd',
      {
        pageNo: '1',
        numOfRows: '1000',
        dataType: 'JSON',
      },
      false,
      true
    );
  });

  test('should get AWS warning zone code', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockForecast]));
    client['makeRequest'] = mockMakeRequest;

    await client.getAwsWarningZoneCode();

    expect(mockMakeRequest).toHaveBeenCalledWith('wrn_reg_aws2.php', {
      disp: '0',
      help: '1',
    });
  });
});
