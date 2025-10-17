/**
 * ASOS Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { ASOSClient, ASOSObservation } from '../../src/clients/asos';

describe('ASOSClient', () => {
  let client: ASOSClient;
  const mockObservation: ASOSObservation = {
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
    ps: 1015.2,
    psQcflg: '0',
    ss: 0.0,
    ssQcflg: '0',
    icsr: 0.0,
    icsrQcflg: '0',
    dsnw: 0.0,
    dsnwQcflg: '0',
  };

  beforeEach(() => {
    client = new ASOSClient({ authKey: 'test-key' });
  });

  describe('initialization', () => {
    test('should create ASOS client', () => {
      expect(client).toBeDefined();
      expect(client).toBeInstanceOf(ASOSClient);
    });
  });

  describe('getHourlyData', () => {
    test('should get hourly data with string time', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getHourlyData('202501011200', 108);

      expect(result).toEqual([mockObservation]);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfctm2.php', {
        tm: '202501011200',
        stn: 108,
      });
    });

    test('should get hourly data with Date object', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date = new Date('2025-01-01T12:00:00');
      const result = await client.getHourlyData(date, 108);

      expect(result).toEqual([mockObservation]);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfctm2.php', {
        tm: '202501011200',
        stn: 108,
      });
    });

    test('should default to station 0 (all stations)', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      await client.getHourlyData('202501011200');

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfctm2.php', {
        tm: '202501011200',
        stn: 0,
      });
    });
  });

  describe('getHourlyPeriod', () => {
    test('should get hourly period data with string times', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation, mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getHourlyPeriod(
        '202501010000',
        '202501011200',
        108
      );

      expect(result).toHaveLength(2);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfctm2.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: 108,
      });
    });

    test('should get hourly period data with Date objects', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date1 = new Date('2025-01-01T00:00:00');
      const date2 = new Date('2025-01-01T12:00:00');
      await client.getHourlyPeriod(date1, date2, 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfctm2.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: 108,
      });
    });
  });

  describe('getDailyData', () => {
    test('should get daily data with string date', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getDailyData('20250101', 108);

      expect(result).toEqual([mockObservation]);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcdd2.php', {
        tm: '20250101',
        stn: 108,
      });
    });

    test('should get daily data with Date object', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date = new Date('2025-01-01T12:00:00');
      await client.getDailyData(date, 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcdd2.php', {
        tm: '20250101',
        stn: 108,
      });
    });
  });

  describe('getDailyPeriod', () => {
    test('should get daily period data with string dates', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation, mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getDailyPeriod('20250101', '20250131', 108);

      expect(result).toHaveLength(2);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcdd2.php', {
        tm1: '20250101',
        tm2: '20250131',
        stn: 108,
      });
    });

    test('should get daily period data with Date objects', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date1 = new Date('2025-01-01');
      const date2 = new Date('2025-01-31');
      await client.getDailyPeriod(date1, date2, 108);

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcdd2.php', {
        tm1: '20250101',
        tm2: '20250131',
        stn: 108,
      });
    });
  });

  describe('getElementData', () => {
    test('should get element data with string times', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const result = await client.getElementData(
        '202501010000',
        '202501011200',
        108,
        'ta'
      );

      expect(result).toEqual([mockObservation]);
      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcelm.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: 108,
        elm: 'ta',
      });
    });

    test('should get element data with Date objects', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const date1 = new Date('2025-01-01T00:00:00');
      const date2 = new Date('2025-01-01T12:00:00');
      await client.getElementData(date1, date2, 108, 'rn');

      expect(mockMakeRequest).toHaveBeenCalledWith('kma_sfcelm.php', {
        tm1: '202501010000',
        tm2: '202501011200',
        stn: 108,
        elm: 'rn',
      });
    });

    test('should support different element codes', async () => {
      const mockMakeRequest = mock(() => Promise.resolve([mockObservation]));
      client['makeRequest'] = mockMakeRequest;

      const elements = ['ta', 'rn', 'ws', 'wd', 'hm'];

      for (const element of elements) {
        await client.getElementData('202501010000', '202501011200', 108, element);
        expect(mockMakeRequest).toHaveBeenCalledWith(
          'kma_sfcelm.php',
          expect.objectContaining({ elm: element })
        );
      }
    });
  });
});
