/**
 * Typhoon Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { TyphoonClient, TyphoonInfo } from '../../src/clients/typhoon';

describe('TyphoonClient', () => {
  let client: TyphoonClient;
  const mockTyphoon: TyphoonInfo = {
    typId: '2501',
    typNm: '태풍1호',
    typIntlNm: 'TYPHOON-1',
    tm: '202501011200',
    lat: 25.5,
    lon: 130.2,
    pres: 990,
    ws: 35,
    mvDir: 'NNW',
    mvSpd: 15,
  };

  beforeEach(() => {
    client = new TyphoonClient({ authKey: 'test-key' });
  });

  test('should get current typhoons', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockTyphoon]));
    client['makeRequest'] = mockMakeRequest;

    const result = await client.getCurrentTyphoons();

    expect(result).toEqual([mockTyphoon]);
    expect(mockMakeRequest).toHaveBeenCalledWith('kma_typ.php', {});
  });

  test('should get typhoon by ID', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockTyphoon]));
    client['makeRequest'] = mockMakeRequest;

    await client.getTyphoonById('2501');

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_typ_dtl.php', {
      typ_id: '2501',
    });
  });

  test('should get typhoon forecast', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockTyphoon]));
    client['makeRequest'] = mockMakeRequest;

    await client.getTyphoonForecast('2501');

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_typ_fcst.php', {
      typ_id: '2501',
    });
  });

  test('should get typhoon history', async () => {
    const mockMakeRequest = mock(() => Promise.resolve([mockTyphoon]));
    client['makeRequest'] = mockMakeRequest;

    await client.getTyphoonHistory(2025);

    expect(mockMakeRequest).toHaveBeenCalledWith('kma_typ_hist.php', {
      year: '2025',
    });
  });
});
