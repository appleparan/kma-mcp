#!/usr/bin/env node
/**
 * KMA MCP Server - TypeScript Implementation
 * Model Context Protocol server for Korea Meteorological Administration API
 */
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod';
import { config } from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { ASOSClient } from './clients/asos.js';
import { AWSClient } from './clients/aws.js';

// Load environment variables from .env file
// When running from dist/index.js: typescript/dist/index.js -> go up 2 levels to project root
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const envPath = join(__dirname, '..', '..', '.env');
config({ path: envPath });
console.error(`Loading environment from: ${envPath}`);

// Environment variables
const API_KEY = process.env.KMA_API_KEY;

/**
 * Validate API key by making a simple API call
 * Uses AWS minutely data API as a lightweight validation endpoint
 */
async function validateApiKey(apiKey: string): Promise<boolean> {
  if (!apiKey) {
    console.error('API key is empty');
    return false;
  }

  try {
    const awsClient = new AWSClient({ authKey: apiKey });

    // Get data from 10 minutes ago to ensure data availability
    const testTime = new Date(Date.now() - 10 * 60 * 1000);
    const timeStr = testTime.toISOString().replace(/[-:]/g, '').replace(/T/, '').slice(0, 12); // YYYYMMDDHHmm format

    // Test with a single station (104 = Bukgangneung)
    const result = await awsClient.getMinutelyData(timeStr, 104);

    if (result) {
      console.error('API key validation successful');
      return true;
    } else {
      console.error('API key validation failed: No data returned');
      return false;
    }
  } catch (error) {
    console.error(
      `API key validation error: ${error instanceof Error ? error.message : String(error)}`
    );
    return false;
  }
}

if (!API_KEY) {
  console.error('Error: KMA_API_KEY environment variable is required');
  process.exit(1);
}

// Initialize clients
const asosClient = new ASOSClient({ authKey: API_KEY });

// Create MCP server
const server = new Server(
  {
    name: 'kma-mcp-server',
    version: '0.1.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Define input schemas
const TimeStationSchema = z.object({
  tm: z.string().describe('Time in YYYYMMDDHHmm format (e.g., 202501011200)'),
  stn: z.number().default(108).describe('Station ID (default: 108 for Seoul, 0 for all)'),
});

const PeriodStationSchema = z.object({
  tm1: z.string().describe('Start time in YYYYMMDDHHmm format'),
  tm2: z.string().describe('End time in YYYYMMDDHHmm format'),
  stn: z.number().default(108).describe('Station ID (default: 108 for Seoul, 0 for all)'),
});

const DateStationSchema = z.object({
  tm: z.string().describe('Date in YYYYMMDD format (e.g., 20250101)'),
  stn: z.number().default(108).describe('Station ID (default: 108 for Seoul, 0 for all)'),
});

const ElementSchema = z.object({
  tm1: z.string().describe('Start time in YYYYMMDDHHmm format'),
  tm2: z.string().describe('End time in YYYYMMDDHHmm format'),
  stn: z.number().describe('Station ID'),
  element: z.string().describe('Element code (e.g., "ta" for temperature, "rn" for precipitation)'),
});

// Tool handlers
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'get_current_weather',
        description: 'Get current hourly weather data from ASOS station',
        inputSchema: {
          type: 'object',
          properties: {
            tm: {
              type: 'string',
              description: 'Time in YYYYMMDDHHmm format (e.g., 202501011200)',
            },
            stn: {
              type: 'number',
              description: 'Station ID (default: 108 for Seoul, 0 for all)',
              default: 108,
            },
          },
          required: ['tm'],
        },
      },
      {
        name: 'get_hourly_weather',
        description: 'Get hourly weather data for a time period from ASOS',
        inputSchema: {
          type: 'object',
          properties: {
            tm1: {
              type: 'string',
              description: 'Start time in YYYYMMDDHHmm format',
            },
            tm2: {
              type: 'string',
              description: 'End time in YYYYMMDDHHmm format',
            },
            stn: {
              type: 'number',
              description: 'Station ID (default: 108 for Seoul)',
              default: 108,
            },
          },
          required: ['tm1', 'tm2'],
        },
      },
      {
        name: 'get_daily_weather',
        description: 'Get daily weather data from ASOS station',
        inputSchema: {
          type: 'object',
          properties: {
            tm: {
              type: 'string',
              description: 'Date in YYYYMMDD format (e.g., 20250101)',
            },
            stn: {
              type: 'number',
              description: 'Station ID (default: 108 for Seoul)',
              default: 108,
            },
          },
          required: ['tm'],
        },
      },
      {
        name: 'get_temperature_data',
        description: 'Get temperature data for a time period',
        inputSchema: {
          type: 'object',
          properties: {
            tm1: {
              type: 'string',
              description: 'Start time in YYYYMMDDHHmm format',
            },
            tm2: {
              type: 'string',
              description: 'End time in YYYYMMDDHHmm format',
            },
            stn: {
              type: 'number',
              description: 'Station ID',
            },
          },
          required: ['tm1', 'tm2', 'stn'],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'get_current_weather': {
        const { tm, stn } = TimeStationSchema.parse(args);
        const data = await asosClient.getHourlyData(tm, stn);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      }

      case 'get_hourly_weather': {
        const { tm1, tm2, stn } = PeriodStationSchema.parse(args);
        const data = await asosClient.getHourlyPeriod(tm1, tm2, stn);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      }

      case 'get_daily_weather': {
        const { tm, stn } = DateStationSchema.parse(args);
        const data = await asosClient.getDailyData(tm, stn);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      }

      case 'get_temperature_data': {
        const { tm1, tm2, stn } = ElementSchema.parse(args);
        const data = await asosClient.getElementData(tm1, tm2, stn, 'ta');
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(data, null, 2),
            },
          ],
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${errorMessage}`,
        },
      ],
      isError: true,
    };
  }
});

// Start server
async function main() {
  console.error('Starting KMA MCP server...');

  // Validate API key on startup
  if (!API_KEY) {
    console.error('KMA_API_KEY environment variable not set');
    console.error('Server will start but API calls will fail');
  } else {
    console.error('Validating API key...');
    const isValid = await validateApiKey(API_KEY);
    if (isValid) {
      console.error('API key is valid and working');
    } else {
      console.error('API key validation failed - API calls may not work properly');
      console.error('Please check your API key at https://apihub.kma.go.kr/');
    }
  }

  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Server initialized successfully');
  console.error('KMA MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
