/**
 * AWS Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { AWSClient, AWSObservation } from '../../src/clients/aws';

describe('AWSClient', () => {
  let client: AWSClient;
  const mockObservation: AWSObservation = {
    tm: '202501011200',
    stnId: '108',
    stnNm: '서울',
    ta: 15.2,
    taQcflg: '0',
    rn: 0.0,
    rnQcflg: '0',
    ws: 3.2,
    wsQcflg: '0',
    wd: 270,
    wdQcflg: '0',
    hm: 65,
    hmQcflg: '0',
    pa: 1013.5,
    paQcflg: '0',
  };

  beforeEach(() => {
    client = new AWSClient({ authKey: 'test-key' });
  });

  describe('initialization', () => {
    test('should create AWS client', () => {
      expect(client).toBeDefined();
      expect(client).toBeInstanceOf(AWSClient);
    });
  });

  describe('getMinutelyData', () => {
    test('should get minutely data with string time', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getMinutelyData(undefined, '202501011200', 108);

      expect(result).toEqual([mockObservation]);
      expect(mockMakeRequest).toHaveBeenCalledWith(
        'nph-aws2_min',
        {
          tm2: '202501011200',
          stn: '108',
          disp: '0',
          help: '1',
        },
        true
      );
    });

    test('should get minutely data with Date object', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date = new Date('2025-01-01T12:00:00');
      await client.getMinutelyData(undefined, date, 108);

      expect(mockMakeRequest).toHaveBeenCalledWith(
        'nph-aws2_min',
        {
          tm2: '202501011200',
          stn: '108',
          disp: '0',
          help: '1',
        },
        true
      );
    });
  });

  describe('getMinutelyPeriod', () => {
    test('should get minutely period data', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getMinutelyPeriod('202501010000', '202501011200', 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_aws2.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: '108',
      });
    });
  });

  describe('getHourlyData', () => {
    test('should get hourly data', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getHourlyData('202501011200', 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_aws3.php', {
        tm: '202501011200',
        stn: '108',
      });
    });
  });

  describe('getHourlyPeriod', () => {
    test('should get hourly period data', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getHourlyPeriod('202501010000', '202501011200', 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_aws4.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: '108',
      });
    });
  });

  describe('getDailyData', () => {
    test('should get daily data', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getDailyData('20250101', 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_aws5.php', {
        tm: '20250101',
        stn: '108',
      });
    });
  });

  describe('getDailyPeriod', () => {
    test('should get daily period data', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getDailyPeriod('20250101', '20250131', 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_aws6.php', {
        tm1: '20250101',
        tm2: '20250131',
        stn: '108',
      });
    });
  });
});
