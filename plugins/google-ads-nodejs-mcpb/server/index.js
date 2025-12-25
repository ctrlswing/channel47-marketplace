#!/usr/bin/env node
/**
 * Google Ads MCP Server (Node.js)
 *
 * A comprehensive MCP server for Google Ads analytics and reporting.
 * Provides read-only access to Google Ads data via GAQL queries.
 *
 * Features:
 * - Execute GAQL queries for any Google Ads resource
 * - List all accessible accounts under MCC
 * - OAuth 2.0 authentication with refresh token
 * - Read-only safety enforcement (mutations blocked)
 * - Response truncation for large datasets
 *
 * @author Channel47
 * @license MIT
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { OAuth2Client } from 'google-auth-library';
import { GoogleAdsApi } from 'google-ads-api';

// ============================================================================
// CONSTANTS
// ============================================================================

const CHARACTER_LIMIT = 25000;
const TOOL_TIMEOUT_MS = 120000; // 2 minutes
const SERVER_NAME = 'google-ads-nodejs';
const SERVER_VERSION = '1.0.0';

// Mutation keywords to block for read-only safety
const MUTATION_KEYWORDS = ['create', 'update', 'remove', 'mutate'];

// ============================================================================
// LOGGING UTILITIES
// ============================================================================

/**
 * Log a debug message to stderr (visible in MCP host logs)
 * @param {string} message - Message to log
 * @param {Object} [data] - Optional data to include
 */
function logDebug(message, data = null) {
  const timestamp = new Date().toISOString();
  const logEntry = { timestamp, level: 'debug', message, ...(data && { data }) };
  console.error(JSON.stringify(logEntry));
}

/**
 * Log an error message to stderr
 * @param {string} message - Error message
 * @param {Error} [error] - Optional error object
 */
function logError(message, error = null) {
  const timestamp = new Date().toISOString();
  const logEntry = {
    timestamp,
    level: 'error',
    message,
    ...(error && { error: error.message, stack: error.stack }),
  };
  console.error(JSON.stringify(logEntry));
}

/**
 * Log server startup information
 */
function logStartup() {
  logDebug(`${SERVER_NAME} v${SERVER_VERSION} starting`, {
    nodeVersion: process.version,
    platform: process.platform,
  });
}

// ============================================================================
// CONFIGURATION & VALIDATION
// ============================================================================

/**
 * Required environment variables for OAuth 2.0 authentication
 */
const REQUIRED_ENV_VARS = [
  'GOOGLE_ADS_DEVELOPER_TOKEN',
  'GOOGLE_ADS_LOGIN_CUSTOMER_ID',
  'GOOGLE_ADS_CLIENT_ID',
  'GOOGLE_ADS_CLIENT_SECRET',
  'GOOGLE_ADS_REFRESH_TOKEN',
];

/**
 * Validate all required environment variables are present
 * @returns {{ valid: boolean, missing: string[] }}
 */
function validateEnvironment() {
  const missing = REQUIRED_ENV_VARS.filter((varName) => !process.env[varName]);
  return {
    valid: missing.length === 0,
    missing,
  };
}

/**
 * Get configuration from environment variables
 * @returns {Object} Configuration object
 */
function getConfig() {
  return {
    developerToken: process.env.GOOGLE_ADS_DEVELOPER_TOKEN,
    loginCustomerId: formatCustomerId(process.env.GOOGLE_ADS_LOGIN_CUSTOMER_ID || ''),
    clientId: process.env.GOOGLE_ADS_CLIENT_ID,
    clientSecret: process.env.GOOGLE_ADS_CLIENT_SECRET,
    refreshToken: process.env.GOOGLE_ADS_REFRESH_TOKEN,
  };
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Format customer ID by removing dashes
 * @param {string} customerId - Customer ID (may contain dashes)
 * @returns {string} Formatted customer ID without dashes
 */
function formatCustomerId(customerId) {
  return customerId.replace(/-/g, '');
}

/**
 * Validate customer ID format
 * @param {string} customerId - Customer ID to validate
 * @returns {{ valid: boolean, formatted: string, error?: string }}
 */
function validateCustomerId(customerId) {
  if (!customerId) {
    return { valid: false, formatted: '', error: 'Customer ID is required' };
  }

  const formatted = formatCustomerId(customerId);

  if (!/^\d{10}$/.test(formatted)) {
    return {
      valid: false,
      formatted,
      error: `Invalid customer ID format: "${customerId}". Expected 10 digits (e.g., 1234567890 or 123-456-7890)`,
    };
  }

  return { valid: true, formatted };
}

/**
 * Check if a query contains mutation operations
 * @param {string} query - GAQL query to check
 * @returns {boolean} True if query contains mutation keywords
 */
function containsMutationKeywords(query) {
  const lowerQuery = query.toLowerCase();
  return MUTATION_KEYWORDS.some((keyword) => lowerQuery.includes(keyword));
}

/**
 * Truncate response if it exceeds character limit
 * @param {string} data - Response string to potentially truncate
 * @param {string} [message] - Additional context for truncation notice
 * @returns {string} Original or truncated response
 */
function truncateResponse(data, message = '') {
  if (data.length <= CHARACTER_LIMIT) {
    return data;
  }

  const truncationNotice = [
    '',
    '',
    '--- RESPONSE TRUNCATED ---',
    `Original size: ${data.length.toLocaleString()} characters`,
    `Truncated to: ${CHARACTER_LIMIT.toLocaleString()} characters`,
    message,
  ].filter(Boolean).join('\n');

  return data.slice(0, CHARACTER_LIMIT - truncationNotice.length) + truncationNotice;
}

/**
 * Convert micros to standard currency format
 * @param {number} micros - Value in micros (1/1,000,000)
 * @returns {number} Value in standard format
 */
function formatMicros(micros) {
  return Math.round((micros / 1_000_000) * 100) / 100;
}

/**
 * Safely serialize a value for JSON output
 * @param {*} value - Value to serialize
 * @returns {*} Serialized value
 */
function serializeValue(value) {
  if (value === null || value === undefined) {
    return null;
  }

  if (typeof value === 'bigint') {
    return value.toString();
  }

  if (typeof value === 'object') {
    if (Array.isArray(value)) {
      return value.map(serializeValue);
    }

    // Handle enum-like objects with name/value properties
    if (value.name !== undefined) {
      return value.name;
    }

    // Recursively serialize object properties
    const serialized = {};
    for (const [key, val] of Object.entries(value)) {
      // Skip internal properties
      if (key.startsWith('_')) continue;
      serialized[key] = serializeValue(val);
    }
    return serialized;
  }

  return value;
}

/**
 * Serialize a GAQL result row to a plain object
 * @param {Object} row - GAQL result row
 * @returns {Object} Serialized row
 */
function serializeGaqlRow(row) {
  try {
    return serializeValue(row);
  } catch (error) {
    logError('Error serializing GAQL row', error);
    return { _error: 'Serialization failed', _raw: String(row) };
  }
}

// ============================================================================
// GOOGLE ADS API CLIENT
// ============================================================================

/** @type {GoogleAdsApi|null} */
let googleAdsClient = null;

/**
 * Initialize and return Google Ads API client
 * @returns {GoogleAdsApi} Google Ads API client
 * @throws {Error} If required credentials are missing
 */
function getGoogleAdsClient() {
  if (googleAdsClient) {
    return googleAdsClient;
  }

  const envCheck = validateEnvironment();
  if (!envCheck.valid) {
    throw new Error(
      `Missing required environment variables for OAuth 2.0:\n` +
      envCheck.missing.map((v) => `  - ${v}`).join('\n') +
      `\n\nPlease configure these in your MCP host settings.`
    );
  }

  const config = getConfig();

  googleAdsClient = new GoogleAdsApi({
    client_id: config.clientId,
    client_secret: config.clientSecret,
    developer_token: config.developerToken,
  });

  logDebug('Google Ads API client initialized');
  return googleAdsClient;
}

/**
 * Get a customer instance for queries
 * @param {string} customerId - Customer ID to query
 * @returns {Object} Customer instance
 */
function getCustomer(customerId) {
  const client = getGoogleAdsClient();
  const config = getConfig();

  return client.Customer({
    customer_id: formatCustomerId(customerId),
    login_customer_id: config.loginCustomerId,
    refresh_token: config.refreshToken,
  });
}

/**
 * Execute a GAQL query with timeout
 * @param {string} customerId - Customer ID to query
 * @param {string} query - GAQL query string
 * @param {Object} [options] - Query options
 * @returns {Promise<Array>} Query results
 */
async function executeGaqlQuery(customerId, query, options = {}) {
  const { timeoutMs = TOOL_TIMEOUT_MS } = options;

  const customer = getCustomer(customerId);

  // Create abort controller for timeout
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    logDebug('Executing GAQL query', { customerId, queryLength: query.length });

    const results = await customer.query(query);

    clearTimeout(timeoutId);
    logDebug('GAQL query completed', { resultCount: results.length });

    return results;
  } catch (error) {
    clearTimeout(timeoutId);

    if (error.name === 'AbortError') {
      throw new Error(`Query timed out after ${timeoutMs / 1000} seconds`);
    }

    // Enhance error message with query context
    throw new Error(`GAQL query failed: ${error.message}\nQuery: ${query}`);
  }
}

// ============================================================================
// TOOL IMPLEMENTATIONS
// ============================================================================

/**
 * Tool: run_google_ads_gaql
 * Execute a GAQL query for data retrieval (read-only)
 */
async function runGoogleAdsGaql(params) {
  const { customer_id, query, use_streaming = false } = params;

  // Validate customer ID
  const customerValidation = validateCustomerId(customer_id);
  if (!customerValidation.valid) {
    return {
      success: false,
      error: customerValidation.error,
    };
  }

  // Validate query is not empty
  if (!query || typeof query !== 'string' || query.trim().length === 0) {
    return {
      success: false,
      error: 'Query is required and must be a non-empty string',
    };
  }

  // Safety check: block mutation operations
  if (containsMutationKeywords(query)) {
    return {
      success: false,
      error: 'This tool is read-only and does not support mutation operations (CREATE, UPDATE, REMOVE, MUTATE)',
    };
  }

  try {
    const results = await executeGaqlQuery(
      customerValidation.formatted,
      query.trim()
    );

    // Serialize results
    const serializedResults = results.map(serializeGaqlRow);

    const response = {
      success: true,
      customer_id: customerValidation.formatted,
      query: query.trim(),
      results: serializedResults,
      result_count: serializedResults.length,
      streaming_used: use_streaming,
    };

    return response;
  } catch (error) {
    logError('GAQL query error', error);
    return {
      success: false,
      error: error.message,
      customer_id: customerValidation.formatted,
      query: query.trim(),
    };
  }
}

/**
 * Tool: google_ads_list_accounts
 * List all accessible Google Ads accounts under MCC
 */
async function googleAdsListAccounts(params) {
  const { response_format = 'markdown' } = params;

  const config = getConfig();
  const mccId = config.loginCustomerId;

  if (!mccId) {
    return {
      success: false,
      error: 'MCC account ID not configured. Set GOOGLE_ADS_LOGIN_CUSTOMER_ID environment variable.',
    };
  }

  const accountsQuery = `
    SELECT
      customer_client.id,
      customer_client.descriptive_name,
      customer_client.currency_code,
      customer_client.time_zone,
      customer_client.status,
      customer_client.manager,
      customer_client.test_account
    FROM customer_client
    WHERE customer_client.status = 'ENABLED'
      AND customer_client.manager = FALSE
    ORDER BY customer_client.id
  `.trim();

  try {
    const results = await executeGaqlQuery(mccId, accountsQuery);

    // Transform results to account objects
    const accounts = results.map((row) => ({
      id: String(row.customer_client?.id || ''),
      name: row.customer_client?.descriptive_name || 'N/A',
      currency: row.customer_client?.currency_code || 'N/A',
      timezone: row.customer_client?.time_zone || 'N/A',
      status: row.customer_client?.status?.name || String(row.customer_client?.status || 'UNKNOWN'),
      is_manager: Boolean(row.customer_client?.manager),
      is_test_account: Boolean(row.customer_client?.test_account),
    }));

    if (response_format === 'json') {
      return {
        success: true,
        mcc_account_id: mccId,
        total_accounts: accounts.length,
        accounts,
      };
    }

    // Markdown format
    if (accounts.length === 0) {
      return {
        success: true,
        content: `# Google Ads Accounts\n\nNo accessible accounts found under MCC ${mccId}.`,
      };
    }

    const mdLines = [
      '# Google Ads Accounts',
      '',
      `**MCC Account:** ${mccId}`,
      `**Total Accounts:** ${accounts.length}`,
      '',
      '| Account ID | Name | Currency | Status | Timezone |',
      '|------------|------|----------|--------|----------|',
    ];

    for (const account of accounts) {
      mdLines.push(
        `| ${account.id} | ${account.name} | ${account.currency} | ${account.status} | ${account.timezone} |`
      );
    }

    return {
      success: true,
      content: mdLines.join('\n'),
    };
  } catch (error) {
    logError('List accounts error', error);
    return {
      success: false,
      error: error.message,
    };
  }
}

// ============================================================================
// TOOL DEFINITIONS
// ============================================================================

const TOOLS = [
  {
    name: 'run_google_ads_gaql',
    description: `Execute a Google Ads Query Language (GAQL) query for data retrieval.

This tool allows you to query any Google Ads resource including:
- Campaigns, Ad Groups, Ads
- Keywords, Search Terms
- Metrics and Performance data
- Account structure and settings

IMPORTANT: This tool is read-only. Mutation operations (CREATE, UPDATE, REMOVE) are blocked for safety.

Common GAQL Resources:
- campaign: Campaign-level data
- ad_group: Ad group data
- keyword_view: Keyword performance
- search_term_view: Search query reports
- customer: Account information

Example queries:
1. Campaign performance:
   SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros
   FROM campaign
   WHERE segments.date DURING LAST_30_DAYS

2. Top keywords:
   SELECT ad_group_criterion.keyword.text, metrics.clicks, metrics.conversions
   FROM keyword_view
   WHERE segments.date DURING LAST_7_DAYS
   ORDER BY metrics.clicks DESC
   LIMIT 50`,
    inputSchema: {
      type: 'object',
      properties: {
        customer_id: {
          type: 'string',
          description: 'Google Ads customer ID (format: 1234567890 or 123-456-7890)',
        },
        query: {
          type: 'string',
          description: 'The Google Ads Query Language (GAQL) query to execute',
        },
        use_streaming: {
          type: 'boolean',
          description: 'Use streaming mode for large result sets (default: false)',
          default: false,
        },
      },
      required: ['customer_id', 'query'],
    },
  },
  {
    name: 'google_ads_list_accounts',
    description: `List all Google Ads accounts accessible under the configured MCC (Manager) account.

Returns account details including:
- Account ID
- Account name
- Currency code
- Timezone
- Status (ENABLED/PAUSED)
- Manager and test account flags

Use this tool to discover which accounts you can query with run_google_ads_gaql.`,
    inputSchema: {
      type: 'object',
      properties: {
        response_format: {
          type: 'string',
          enum: ['markdown', 'json'],
          description: 'Output format: "markdown" for human-readable or "json" for structured data',
          default: 'markdown',
        },
      },
      required: [],
    },
  },
];

// ============================================================================
// MCP SERVER SETUP
// ============================================================================

/**
 * Create and configure the MCP server
 * @returns {Server} Configured MCP server instance
 */
function createServer() {
  const server = new Server(
    {
      name: SERVER_NAME,
      version: SERVER_VERSION,
    },
    {
      capabilities: {
        tools: {},
      },
    }
  );

  // Handle tool listing
  server.setRequestHandler(ListToolsRequestSchema, async () => {
    return { tools: TOOLS };
  });

  // Handle tool execution
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    logDebug('Tool call received', { tool: name });

    try {
      let result;

      switch (name) {
        case 'run_google_ads_gaql':
          result = await runGoogleAdsGaql(args || {});
          break;

        case 'google_ads_list_accounts':
          result = await googleAdsListAccounts(args || {});
          break;

        default:
          throw new Error(`Unknown tool: ${name}`);
      }

      // Format response
      const content = result.content || JSON.stringify(result, null, 2);
      const truncatedContent = truncateResponse(content);

      return {
        content: [
          {
            type: 'text',
            text: truncatedContent,
          },
        ],
        isError: result.success === false,
      };
    } catch (error) {
      logError(`Tool execution failed: ${name}`, error);

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              success: false,
              error: error.message,
              tool: name,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  });

  return server;
}

// ============================================================================
// MAIN ENTRY POINT
// ============================================================================

async function main() {
  logStartup();

  // Validate environment on startup (warn but don't fail)
  const envCheck = validateEnvironment();
  if (!envCheck.valid) {
    logError('Missing environment variables', { missing: envCheck.missing });
    console.error(
      `Warning: Missing required environment variables: ${envCheck.missing.join(', ')}\n` +
      'Tool calls will fail until these are configured.'
    );
  }

  const server = createServer();
  const transport = new StdioServerTransport();

  await server.connect(transport);

  logDebug('MCP server connected and ready');
}

// Handle uncaught errors
process.on('uncaughtException', (error) => {
  logError('Uncaught exception', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason) => {
  logError('Unhandled rejection', reason instanceof Error ? reason : new Error(String(reason)));
  process.exit(1);
});

// Start the server
main().catch((error) => {
  logError('Failed to start server', error);
  process.exit(1);
});
