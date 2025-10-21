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
});
