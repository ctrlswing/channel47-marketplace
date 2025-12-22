#!/usr/bin/env python3
"""
Google Ads MCP Server Authentication Test Script

This script tests your Google Ads API authentication setup to ensure
everything is configured correctly before using the MCP server.

Usage:
    python test_google_ads_auth.py

Requirements:
    - .env file with credentials OR environment variables set
    - google-ads, google-auth packages installed
"""

import os
import sys
from pathlib import Path
from typing import Optional

# Try to load from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded environment variables from .env file")
except ImportError:
    print("ℹ️  python-dotenv not installed, using system environment variables")

def check_env_vars():
    """Check if all required environment variables are set."""
    required_vars = [
        "GOOGLE_ADS_DEVELOPER_TOKEN",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
        "GOOGLE_ADS_CLIENT_ID",
        "GOOGLE_ADS_CLIENT_SECRET",
        "GOOGLE_ADS_REFRESH_TOKEN"
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        else:
            # Show partial value for security
            display_value = f"{value[:4]}..." if len(value) > 8 else "***"
            print(f"  ✅ {var}: {display_value}")
    
    if missing_vars:
        print("\n❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease set these in your .env file or as environment variables.")
        print("Run `scripts/generate_refresh_token.py` to get your REFRESH_TOKEN.")
        return False
    
    return True

def _resolve_api_version() -> Optional[str]:
    """
    Return a supported Google Ads API version for tests.
    Falls back when GOOGLE_ADS_API_VERSION points to an unavailable release.
    """
    requested = os.getenv("GOOGLE_ADS_API_VERSION", "").strip()
    if not requested:
        return None

    try:
        from google.ads.googleads import client as googleads_client_module

        valid_versions = getattr(googleads_client_module, "_VALID_API_VERSIONS", None)
        if valid_versions and requested not in valid_versions:
            default_version = getattr(googleads_client_module, "_DEFAULT_VERSION", "unspecified")
            print(
                f"⚠️  GOOGLE_ADS_API_VERSION '{requested}' is unavailable; "
                f"falling back to client default '{default_version}'."
            )
            return None
    except Exception:
        # If version metadata cannot be inspected, proceed with the requested value
        return requested

    return requested


def test_authentication():
    """Test authentication with Google Ads API."""
    try:
        from google.oauth2.credentials import Credentials
        from google.ads.googleads.client import GoogleAdsClient
        
        print("\n🔐 Testing authentication...")
        
        # Create credentials from OAuth 2.0 refresh token
        credentials = Credentials(
            None,
            refresh_token=os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
            token_uri="https://accounts.google.com/o/oauth2/token",
            client_id=os.getenv("GOOGLE_ADS_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
            scopes=['https://www.googleapis.com/auth/adwords']
        )
        print("  ✅ OAuth 2.0 credentials created")
        
        # Initialize Google Ads client
        client = GoogleAdsClient(
            credentials=credentials,
            developer_token=os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
            login_customer_id=os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
            version=_resolve_api_version()
        )
        print("  ✅ Google Ads client initialized")
        
        # Try a simple query to verify access
        mcc_id = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID").replace("-", "")
        ga_service = client.get_service("GoogleAdsService")
        
        query = """
            SELECT
                customer.id,
                customer.descriptive_name
            FROM customer
            LIMIT 1
        """
        
        print("  🔍 Testing API access with simple query...")
        response = ga_service.search(customer_id=mcc_id, query=query)
        
        # Get first result
        for row in response:
            print(f"  ✅ Successfully accessed account: {row.customer.descriptive_name}")
            break
        
        print("\n" + "="*60)
        print("🎉 SUCCESS! Authentication is working correctly!")
        print("="*60)
        print("\nYou can now:")
        print("1. Add this server to your Claude Desktop configuration")
        print("2. Restart Claude Desktop")
        print("3. Start using natural language to query your Google Ads data")
        print("\nNext steps:")
        print("- Try: 'List my Google Ads accounts'")
        print("- Try: 'Show me campaign performance for the last 30 days'")
        
        return True
        
    except ImportError as e:
        print(f"\n❌ Missing required packages: {e}")
        print("\nInstall them with:")
        print("  pip install google-ads google-auth")
        return False
        
    except Exception as e:
        error_msg = str(e)
        print(f"\n❌ Authentication failed: {error_msg}")
        
        # Provide specific guidance based on error
        if "invalid_grant" in error_msg:
            print("\n💡 Troubleshooting:")
            print("  - Your refresh token may have expired or been revoked.")
            print("  - Run `scripts/generate_refresh_token.py` to get a new one.")
            print("  - Ensure your OAuth consent screen is set to 'External' and 'Published'.")
            
        elif "invalid_client" in error_msg:
            print("\n💡 Troubleshooting:")
            print("  - Verify `GOOGLE_ADS_CLIENT_ID` and `GOOGLE_ADS_CLIENT_SECRET` are correct.")
            
        elif "DEVELOPER_TOKEN" in error_msg:
            print("\n💡 Troubleshooting:")
            print("  - Verify your developer token is correct.")
            print("  - Check token has Basic or Standard access (not test-only)")
            print("  - Ensure token is approved and active")
            
        elif "UNAUTHENTICATED" in error_msg or "Invalid credentials" in error_msg:
            print("\n💡 Troubleshooting:")
            print("  - Verify your OAuth 2.0 credentials are correct.")
            print("  - Run `scripts/generate_refresh_token.py` again.")
            
        elif "PERMISSION_DENIED" in error_msg:
            print("\n💡 Troubleshooting:")
            print("  - Verify MCC account ID is correct (10 digits, no dashes)")
            print("  - Ensure service account has been granted access")
            print("  - Check that you have permission to access this account")
            
        else:
            print("\n💡 Check the full error message above for details")
            print("   See README_GOOGLE_ADS_MCP.md for more troubleshooting help")
        
        return False

def main():
    """Run all authentication tests."""
    print("="*60)
    print("Google Ads MCP Server - Authentication Test")
    print("="*60)
    print()
    
    print("📋 Step 1: Checking environment variables...")
    if not check_env_vars():
        sys.exit(1)
    
    print("\n🔐 Step 2: Testing authentication...")
    if not test_authentication():
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
