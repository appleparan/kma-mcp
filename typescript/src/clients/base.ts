/**
 * Base KMA API Client
 */
import axios, { AxiosInstance, AxiosError } from 'axios';

export interface KMAClientConfig {
  authKey: string;
  baseURL?: string;
  cgiBaseURL?: string;
  timeout?: number;
}

export interface KMAResponse<T = unknown> {
  response: {
    header: {
      resultCode: string;
      resultMsg: string;
    };
    body: {
      dataType: string;
      items?: {
        item: T[];
      };
      pageNo?: number;
      numOfRows?: number;
      totalCount?: number;
    };
  };
}

export class KMAAPIError extends Error {
  constructor(
    message: string,
    public statusCode?: number,
    public resultCode?: string
  ) {
    super(message);
    this.name = 'KMAAPIError';
  }
}

export abstract class BaseKMAClient {
  protected client: AxiosInstance;
  protected cgiClient: AxiosInstance;
  protected authKey: string;

  constructor(config: KMAClientConfig) {
    this.authKey = config.authKey;
    this.client = axios.create({
      baseURL: config.baseURL || 'https://apihub.kma.go.kr/api/typ01/url',
      timeout: config.timeout || 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    });
    this.cgiClient = axios.create({
      baseURL: config.cgiBaseURL || 'https://apihub.kma.go.kr/api/typ01/cgi-bin/url',
      timeout: config.timeout || 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  protected async makeRequest<T = unknown>(
    endpoint: string,
    params: Record<string, unknown>,
    useCgi = false
  ): Promise<T[]> {
    try {
      const client = useCgi ? this.cgiClient : this.client;
      const response = await client.get<KMAResponse<T>>(endpoint, {
        params: {
          ...params,
          authKey: this.authKey,
          help: params.help !== undefined ? params.help : '0',
        },
      });

      const { header, body } = response.data.response;

      if (header.resultCode !== '00') {
        throw new KMAAPIError(header.resultMsg, undefined, header.resultCode);
      }

      return body.items?.item || [];
    } catch (error) {
      if (error instanceof KMAAPIError) {
        throw error;
      }

      if (axios.isAxiosError(error)) {
        const axiosError = error as AxiosError;
        throw new KMAAPIError(
          `HTTP ${axiosError.response?.status}: ${axiosError.message}`,
          axiosError.response?.status
        );
      }

      throw new KMAAPIError(`Unexpected error: ${error}`);
    }
  }

  /**
   * Format datetime to KMA API format (YYYYMMDDHHmm or YYYYMMDD)
   */
  protected formatDateTime(date: Date, includeTime = true): string {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    if (!includeTime) {
      return `${year}${month}${day}`;
    }

    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');

    return `${year}${month}${day}${hours}${minutes}`;
  }
}
