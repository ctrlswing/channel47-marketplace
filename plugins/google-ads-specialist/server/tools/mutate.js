#!/usr/bin/env node
import { getCustomerClient } from '../auth.js';

/**
 * Execute mutation operations using GoogleAdsService.Mutate
 * Supports any write operation with dry_run validation
 *
 * @param {Object} params - Mutation parameters
 * @param {string} params.customer_id - Google Ads customer ID (optional, uses env default)
 * @param {Array} params.operations - Array of mutation operation objects
 * @param {boolean} params.partial_failure - Enable partial failure mode (default: true)
 * @param {boolean} params.dry_run - Validate only, don't execute (default: true)
 * @returns {Promise<Object>} Mutation results
 */
export async function mutate(params) {
  const {
    customer_id = process.env.GOOGLE_ADS_CUSTOMER_ID,
    operations,
    partial_failure = true,
    dry_run = true
  } = params;

  // Validate required parameters
  if (!customer_id) {
    return {
      success: false,
      error: 'customer_id is required (either as parameter or GOOGLE_ADS_CUSTOMER_ID env var)'
    };
  }

  if (!operations || !Array.isArray(operations) || operations.length === 0) {
    return {
      success: false,
      error: 'operations array is required and must contain at least one operation'
    };
  }

  try {
    const customer = getCustomerClient(customer_id);

    // Execute mutation with validation options
    const response = await customer.mutateResources(operations, {
      partialFailure: partial_failure,
      validateOnly: dry_run
    });

    return {
      success: true,
      dry_run,
      results: response,
      message: dry_run
        ? 'Validation successful - no changes made'
        : 'Mutations applied successfully',
      operations_count: operations.length
    };
  } catch (error) {
    return {
      success: false,
      dry_run,
      error: error.message,
      error_details: error.errors || null
    };
  }
}
