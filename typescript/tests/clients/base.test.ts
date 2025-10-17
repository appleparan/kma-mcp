/**
 * Base KMA Client Tests
 */
import { describe, test, expect, beforeEach, mock } from 'bun:test';
import { BaseKMAClient, KMAAPIError } from '../../src/clients/base';

// Create a concrete implementation for testing
class TestKMAClient extends BaseKMAClient {
  async testRequest<T>(endpoint: string, params: Record<string, unknown>): Promise<T[]> {
    return this.makeRequest<T>(endpoint, params);
  }

  testFormatDateTime(date: Date, includeTime = true): string {
    return this.formatDateTime(date, includeTime);
  }
}

describe('BaseKMAClient', () => {
  let client: TestKMAClient;

  beforeEach(() => {
    client = new TestKMAClient({ authKey: 'test-key' });
  });

  describe('initialization', () => {
    test('should create client with default config', () => {
      expect(client).toBeDefined();
    });

    test('should create client with custom config', () => {
      const customClient = new TestKMAClient({
        authKey: 'custom-key',
        baseURL: 'https://custom.api',
        timeout: 60000,
      });
      expect(customClient).toBeDefined();
    });
  });

  describe('formatDateTime', () => {
    test('should format date with time', () => {
      const date = new Date('2025-01-15T14:30:00');
      const result = client.testFormatDateTime(date, true);
      expect(result).toBe('202501151430');
    });

    test('should format date without time', () => {
      const date = new Date('2025-01-15T14:30:00');
      const result = client.testFormatDateTime(date, false);
      expect(result).toBe('20250115');
    });

    test('should pad single digit month/day/hour/minute', () => {
      const date = new Date('2025-01-05T09:05:00');
      const result = client.testFormatDateTime(date, true);
      expect(result).toBe('202501050905');
    });
  });

  describe('makeRequest', () => {
    test('should handle successful API response', async () => {
      // Mock axios
      const mockGet = mock(() =>
        Promise.resolve({
          data: {
            response: {
              header: {
                resultCode: '00',
                resultMsg: 'NORMAL_SERVICE',
              },
              body: {
                dataType: 'JSON',
                items: {
                  item: [{ id: 1, name: 'test' }],
                },
              },
            },
          },
        })
      );

      client['client'].get = mockGet as (typeof client)['client']['get'];

      const result = await client.testRequest('test.php', { param: 'value' });

      expect(result).toEqual([{ id: 1, name: 'test' }]);
      expect(mockGet).toHaveBeenCalledTimes(1);
    });

    test('should handle empty response', async () => {
      const mockGet = mock(() =>
        Promise.resolve({
          data: {
            response: {
              header: {
                resultCode: '00',
                resultMsg: 'NORMAL_SERVICE',
              },
              body: {
                dataType: 'JSON',
              },
            },
          },
        })
      );

      client['client'].get = mockGet as (typeof client)['client']['get'];

      const result = await client.testRequest('test.php', {});

      expect(result).toEqual([]);
    });

    test('should throw KMAAPIError on API error', async () => {
      const mockGet = mock(() =>
        Promise.resolve({
          data: {
            response: {
              header: {
                resultCode: '99',
                resultMsg: 'API ERROR',
              },
              body: {},
            },
          },
        })
      );

      client['client'].get = mockGet as (typeof client)['client']['get'];

      try {
        await client.testRequest('test.php', {});
        expect(true).toBe(false); // Should not reach here
      } catch (error) {
        expect(error).toBeInstanceOf(KMAAPIError);
        expect((error as KMAAPIError).message).toBe('API ERROR');
        expect((error as KMAAPIError).resultCode).toBe('99');
      }
    });

    test('should throw KMAAPIError on HTTP error', async () => {
      const mockGet = mock(() =>
        Promise.reject({
          isAxiosError: true,
          response: {
            status: 401,
          },
          message: 'Unauthorized',
        })
      );

      client['client'].get = mockGet as (typeof client)['client']['get'];

      try {
        await client.testRequest('test.php', {});
        expect(true).toBe(false);
      } catch (error) {
        expect(error).toBeInstanceOf(KMAAPIError);
        expect((error as KMAAPIError).statusCode).toBe(401);
      }
    });
  });

  describe('KMAAPIError', () => {
    test('should create error with message only', () => {
      const error = new KMAAPIError('Test error');
      expect(error.message).toBe('Test error');
      expect(error.name).toBe('KMAAPIError');
      expect(error.statusCode).toBeUndefined();
      expect(error.resultCode).toBeUndefined();
    });

    test('should create error with status code', () => {
      const error = new KMAAPIError('HTTP error', 404);
      expect(error.message).toBe('HTTP error');
      expect(error.statusCode).toBe(404);
    });

    test('should create error with result code', () => {
      const error = new KMAAPIError('API error', undefined, '99');
      expect(error.message).toBe('API error');
      expect(error.resultCode).toBe('99');
    });
  });
});
