# File: src/google_ads_mcp.py
# What: Google Ads MCP server utilities and tools for analytics/reporting.
# Why: Maintain MCP functionality while addressing review findings (ROAS sorting,
#      anomaly detection resource mapping, Shopping product campaign filtering).

"""
Google Ads MCP Server

A comprehensive MCP server for Google Ads management with MCC-level access,
focusing on Search and Shopping campaign performance analysis and optimization.

This server provides tools for:
- Campaign, keyword, and product performance analysis
- Search term analysis for negative keyword opportunities
- Budget pacing and spend monitoring
- Anomaly detection for performance changes
- Cross-account analysis and reporting
- Shopping product issue identification

Authentication: OAuth 2.0
Access Level: Read-only operations for safe exploration

Recent Fixes:
- Fixed "_pb" serialization errors by replacing MessageToJson(row._pb) with robust serialize_gaql_row() function
- Removed unsupported page_size parameter from GAQL queries (Google Ads API doesn't support it)
- Improved error reporting with clearer messages and query information
"""

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Dict, Any, Callable, Tuple
from enum import Enum
import json
import os
import warnings
from google.oauth2.credentials import Credentials
from google.ads.googleads import client as googleads_client_module
from google.ads.googleads.client import GoogleAdsClient
from google.protobuf.json_format import MessageToJson

# Module-level constants
CHARACTER_LIMIT = 25000
def _resolve_google_ads_version() -> Optional[str]:
    """
    Return a supported Google Ads API version or None to use the client's default.
    Falls back automatically if the requested version isn't bundled with the SDK.
    """
    requested = os.getenv("GOOGLE_ADS_API_VERSION", "").strip()
    if not requested:
        return None

    valid_versions = getattr(googleads_client_module, "_VALID_API_VERSIONS", None)
    if valid_versions and requested not in valid_versions:
        default_version = getattr(googleads_client_module, "_DEFAULT_VERSION", "unspecified")
        warnings.warn(
            f"GOOGLE_ADS_API_VERSION '{requested}' is not available; "
            f"falling back to client default '{default_version}'.",
            RuntimeWarning,
        )
        return None

    return requested


GOOGLE_ADS_API_VERSION = _resolve_google_ads_version()

# Initialize FastMCP server
mcp = FastMCP("google_ads_mcp")

# ============================================================================
# SHARED UTILITIES
# ============================================================================

def get_google_ads_client(customer_id: Optional[str] = None) -> GoogleAdsClient:
    """
    Initialize Google Ads API client with OAuth 2.0 credentials.
    
    Args:
        customer_id: Optional customer ID to set as login_customer_id
        
    Returns:
        GoogleAdsClient instance configured with OAuth 2.0
    """
    # Get configuration from environment variables
    developer_token = os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN")
    login_customer_id = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID", customer_id)
    client_id = os.getenv("GOOGLE_ADS_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_ADS_CLIENT_SECRET")
    refresh_token = os.getenv("GOOGLE_ADS_REFRESH_TOKEN")
    
    if not all([developer_token, login_customer_id, client_id, client_secret, refresh_token]):
        raise ValueError(
            "Missing required environment variables for OAuth 2.0. Please set:\n"
            "- GOOGLE_ADS_DEVELOPER_TOKEN\n"
            "- GOOGLE_ADS_LOGIN_CUSTOMER_ID (MCC account ID)\n"
            "- GOOGLE_ADS_CLIENT_ID\n"
            "- GOOGLE_ADS_CLIENT_SECRET\n"
            "- GOOGLE_ADS_REFRESH_TOKEN"
        )
    
    # Create credentials from OAuth 2.0 refresh token
    credentials = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri="https://accounts.google.com/o/oauth2/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=['https://www.googleapis.com/auth/adwords']
    )
    
    # Initialize Google Ads client
    client = GoogleAdsClient(
        credentials=credentials,
        developer_token=developer_token,
        login_customer_id=login_customer_id,
        version=GOOGLE_ADS_API_VERSION
    )
    
    return client


def execute_gaql_query(
    client: GoogleAdsClient,
    customer_id: str,
    query: str,
    use_streaming: bool = True,
    page_size: Optional[int] = None
) -> List[Any]:
    """
    Execute a GAQL query and return results.

    Args:
        client: GoogleAdsClient instance
        customer_id: Customer ID to query (format: 1234567890, no dashes)
        query: GAQL query string
        use_streaming: Whether to use SearchStream (default) or Search
        page_size: Deprecated - not supported by Google Ads API. The API handles pagination internally.

    Returns:
        List of GoogleAdsRow objects
    """
    ga_service = client.get_service("GoogleAdsService")

    try:
        if use_streaming:
            response = ga_service.search_stream(customer_id=customer_id, query=query)
            results = []
            for batch in response:
                results.extend(batch.results)
            return results
        else:
            # Use non-streaming search
            # Note: Google Ads API does not support page_size parameter in the search method
            # Pagination is handled internally by the API
            response = ga_service.search(customer_id=customer_id, query=query)
            return list(response)
    except Exception as e:
        raise Exception(f"Error executing GAQL query: {str(e)}\nQuery: {query}")


def format_micros(micros: int) -> float:
    """Convert micros (1/1,000,000) to standard currency format."""
    return round(micros / 1_000_000, 2)


def format_gaql_value(value: Any) -> str:
    """
    Format a value for safe inclusion in GAQL queries.

    Handles proper escaping for strings, boolean conversion, and type validation.

    Args:
        value: The value to format

    Returns:
        str: Properly formatted GAQL value
    """
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    elif isinstance(value, str):
        # Escape single quotes by doubling them
        escaped_value = value.replace("'", "''")
        return f"'{escaped_value}'"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        # For other types, convert to string and escape
        str_value = str(value)
        escaped_value = str_value.replace("'", "''")
        return f"'{escaped_value}'"


def calculate_roas(conversions_value: float, cost: float) -> Optional[float]:
    """Calculate ROAS (Return on Ad Spend)."""
    if cost == 0:
        return None
    return round(conversions_value / cost, 2)


def calculate_cvr(conversions: float, clicks: int) -> Optional[float]:
    """Calculate conversion rate."""
    if clicks == 0:
        return None
    return round((conversions / clicks) * 100, 2)


def get_proto_attr(entity: Any, attr: str) -> Any:
    """Return proto field, handling trailing underscore that Python reserves."""
    if entity is None:
        return None

    sentinel = object()
    value = getattr(entity, attr, sentinel)
    if value is sentinel:
        value = getattr(entity, f"{attr}_", sentinel)
    return None if value is sentinel else value


def truncate_response(data: str, message: str = "") -> str:
    """
    Truncate response if it exceeds CHARACTER_LIMIT.
    
    Args:
        data: The response string to potentially truncate
        message: Additional context message about truncation
        
    Returns:
        Original or truncated response with truncation notice
    """
    if len(data) <= CHARACTER_LIMIT:
        return data
    
    truncation_notice = (
        f"\n\n⚠️ RESPONSE TRUNCATED\n"
        f"Original size: {len(data):,} characters\n"
        f"Truncated to: {CHARACTER_LIMIT:,} characters\n"
        f"{message}"
    )
    
    # Truncate and add notice
    return data[:CHARACTER_LIMIT - len(truncation_notice)] + truncation_notice


def format_customer_id(customer_id: str) -> str:
    """Format customer ID by removing dashes."""
    return customer_id.replace("-", "")


def get_enum_name(
    value: Any,
    enum_converter: Optional[Callable[[Any], Enum]] = None,
    default: str = "UNSPECIFIED"
) -> str:
    """
    Safely resolve the name of a Google Ads enum, handling int fallbacks.

    Args:
        value: Enum value returned by Google Ads API (may be proto enum or int)
        enum_converter: Callable that can convert raw value into enum instance
        default: Fallback string when value is None

    Returns:
        Enum name string or fallback representation.
    """
    if value is None:
        return default

    # Some proto enums expose `name`, others only provide `value`
    # or require using the enum descriptor's Name() helper.
    name = getattr(value, "name", None)
    if name:
        return name

    raw_value = getattr(value, "value", value)

    if enum_converter:
        try:
            name_helper = getattr(enum_converter, "Name", None)
            if callable(name_helper):
                return name_helper(raw_value)
        except Exception:
            pass

        try:
            converted = enum_converter(raw_value)
            converted_name = getattr(converted, "name", None)
            if converted_name:
                return converted_name
        except Exception:
            pass

    return str(raw_value)


def resolve_enum_converter(
    client: GoogleAdsClient,
    candidates: List[Tuple[str, str]]
) -> Optional[Callable[[Any], Enum]]:
    """Return the first available enum converter from the provided candidates."""
    enums_container = getattr(client, "enums", None)
    if not enums_container:
        return None

    for enum_name, member_name in candidates:
        enum_class = getattr(enums_container, enum_name, None)
        if not enum_class:
            continue

        converter = getattr(enum_class, member_name, None)
        if converter:
            return converter

    return None


# ============================================================================
# INPUT MODELS
# ============================================================================

class DateRange(str, Enum):
    """Predefined date ranges for Google Ads queries."""
    TODAY = "TODAY"
    YESTERDAY = "YESTERDAY"
    LAST_7_DAYS = "LAST_7_DAYS"
    LAST_14_DAYS = "LAST_14_DAYS"
    LAST_30_DAYS = "LAST_30_DAYS"
    LAST_BUSINESS_WEEK = "LAST_BUSINESS_WEEK"
    THIS_MONTH = "THIS_MONTH"
    LAST_MONTH = "LAST_MONTH"
    THIS_WEEK_SUN_TODAY = "THIS_WEEK_SUN_TODAY"
    THIS_WEEK_MON_TODAY = "THIS_WEEK_MON_TODAY"


class ResponseFormat(str, Enum):
    """Output format for tool responses."""
    MARKDOWN = "markdown"
    JSON = "json"


class RunGoogleAdsGaqlInput(BaseModel):
    """Input for running a raw GAQL query."""
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    customer_id: str = Field(
        ...,
        description="Google Ads customer ID (format: 1234567890 or 123-456-7890)",
        min_length=10,
        max_length=12
    )
    query: str = Field(
        ...,
        description="The Google Ads Query Language (GAQL) query to execute."
    )
    page_size: int = Field(
        default=100,
        description="DEPRECATED: Not supported by Google Ads API. This parameter is ignored as the API handles pagination internally. Kept for backward compatibility.",
        ge=1,
        le=10000
    )
    use_streaming: bool = Field(
        default=False,
        description="Use streaming mode to fetch ALL results (ignores page_size). Enable only for large exports."
    )


class ListAccountsInput(BaseModel):
    """Input for listing Google Ads accounts under MCC."""
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' for human-readable or 'json' for machine-readable"
    )


# ============================================================================
# TOOL IMPLEMENTATIONS
# ============================================================================

@mcp.tool(
    name="run_google_ads_gaql",
    annotations={
        "title": "Run Google Ads GAQL Query",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def run_google_ads_gaql(params: RunGoogleAdsGaqlInput) -> str:
    """
    Run any Google Ads Query Language (GAQL) query for data retrieval (read-only).
    This tool is for advanced users who are familiar with GAQL.
    For simpler use cases, consider using 'list_google_ads_resources'.
    """
    try:
        # Basic check to prevent mutations
        query_lower = params.query.lower()
        if any(op in query_lower for op in ["create", "update", "remove", "mutate"]):
            raise ValueError("This tool is read-only and does not support mutation operations.")

        client = get_google_ads_client()
        customer_id = format_customer_id(params.customer_id)

        # Note: page_size is not supported by Google Ads API search method
        # The page_size parameter is ignored as the API handles pagination internally
        results = execute_gaql_query(
            client,
            customer_id,
            params.query,
            use_streaming=params.use_streaming,
            page_size=None  # Always None as the API doesn't support page_size parameter
        )

        # Serialize results using the robust helper function
        serialized_results = [serialize_gaql_row(row) for row in results]

        return json.dumps({
            "customer_id": customer_id,
            "query": params.query,
            "results": serialized_results,
            "result_count": len(serialized_results),
            "streaming_used": params.use_streaming
        }, indent=2)

    except Exception as e:
        return f"Error executing GAQL query: {str(e)}\nQuery: {params.query}"


@mcp.tool(
    name="google_ads_list_accounts",
    annotations={
        "title": "List Google Ads Accounts",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def google_ads_list_accounts(params: ListAccountsInput) -> str:
    """
    List all Google Ads accounts accessible under the MCC account.

    Returns a list of customer accounts with basic information including
    account ID, name, currency, timezone, and status.

    Args:
        params (ListAccountsInput): Query parameters including output format

    Returns:
        str: Account list in JSON or Markdown format
    """
    try:
        client = get_google_ads_client()

        # Get MCC account ID from environment
        mcc_id = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID")
        if not mcc_id:
            raise ValueError("MCC account ID not configured. Set GOOGLE_ADS_LOGIN_CUSTOMER_ID environment variable.")

        # Query for all accessible customer accounts
        accounts_query = """
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
        """

        results = execute_gaql_query(client, format_customer_id(mcc_id), accounts_query)

        # Convert results to JSON format first
        accounts = []
        for row in results:
            account = {
                "id": str(row.customer_client.id),
                "name": row.customer_client.descriptive_name,
                "currency": row.customer_client.currency_code,
                "timezone": row.customer_client.time_zone,
                "status": row.customer_client.status.name if hasattr(row.customer_client.status, 'name') else str(row.customer_client.status),
                "is_manager": row.customer_client.manager,
                "is_test_account": row.customer_client.test_account
            }
            accounts.append(account)

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({
                "mcc_account_id": mcc_id,
                "total_accounts": len(accounts),
                "accounts": accounts
            }, indent=2)
        else:
            # Markdown format
            if not accounts:
                return f"# Google Ads Accounts\n\nNo accessible accounts found under MCC {mcc_id}."

            md_output = f"# Google Ads Accounts\n\n"
            md_output += f"**MCC Account:** {mcc_id}\n"
            md_output += f"**Total Accounts:** {len(accounts)}\n\n"

            md_output += "| Account ID | Name | Currency | Status | Timezone |\n"
            md_output += "|------------|------|----------|--------|----------|\n"

            for account in accounts:
                name = account.get("name", "N/A") or "N/A"
                md_output += f"| {account['id']} | {name} | {account['currency']} | {account['status']} | {account['timezone']} |\n"

            return md_output

    except Exception as e:
        return f"Error listing accounts: {str(e)}"


def serialize_gaql_row(row) -> dict:
    """
    Convert a GAQL result row to a dictionary, handling dynamic field access.

    Args:
        row: GoogleAdsRow object from GAQL query

    Returns:
        dict: Serialized row data
    """
    try:
        # Try using MessageToJson on the row directly first
        return json.loads(MessageToJson(row))
    except Exception:
        # Fallback: manually extract fields if MessageToJson fails
        result = {}
        # The row object has attributes corresponding to the selected resource types
        # For example, if querying campaigns, row.campaign will exist
        for attr_name in dir(row):
            if not attr_name.startswith('_') and hasattr(row, attr_name):
                attr_value = getattr(row, attr_name)
                if attr_value is not None:
                    # Try to serialize nested objects
                    try:
                        if hasattr(attr_value, '__dict__'):
                            # For nested objects, recursively serialize
                            nested_dict = {}
                            for nested_attr in dir(attr_value):
                                if not nested_attr.startswith('_') and hasattr(attr_value, nested_attr):
                                    nested_value = getattr(attr_value, nested_attr)
                                    if nested_value is not None:
                                        nested_dict[nested_attr] = str(nested_value)
                            if nested_dict:
                                result[attr_name] = nested_dict
                        else:
                            result[attr_name] = str(attr_value)
                    except Exception:
                        # If serialization fails, convert to string
                        result[attr_name] = str(attr_value)
        return result








# ============================================================================
# SERVER INITIALIZATION
# ============================================================================

if __name__ == "__main__":
    # Run the MCP server using stdio transport
    mcp.run()
