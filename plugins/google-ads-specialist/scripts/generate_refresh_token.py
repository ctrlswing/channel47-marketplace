#!/usr/bin/env python3
"""
Google Ads MCP Server - Refresh Token Generation Script

This script helps you generate an OAuth 2.0 refresh token for the Google Ads API,
which is required for the MCP server to authenticate on your behalf.

Instructions:
1.  **Create OAuth 2.0 Credentials**:
    - Go to the Google Cloud Console: https://console.cloud.google.com/
    - Navigate to "APIs & Services" > "Credentials".
    - Click "Create Credentials" > "OAuth client ID".
    - Select "Desktop app" as the application type.
    - Give it a name (e.g., "Google Ads MCP Client").
    - Click "Create".
    - A dialog will appear with your client ID and client secret. Click "DOWNLOAD JSON"
      and save this file as `client_secrets.json` in the same directory as this script.

2.  **Run this script**:
    - Make sure `client_secrets.json` is in the current directory.
    - Run the script from your terminal: `python generate_refresh_token.py`

3.  **Authorize Access**:
    - The script will print a URL. Copy and paste it into your browser.
    - Log in to the Google account that has access to your Google Ads account.
    - Grant the requested permissions.
    - After authorization, you will be redirected to a localhost URL with an
      authorization code. Copy the full URL from your browser's address bar.

4.  **Provide Authorization Code**:
    - Paste the full localhost URL back into the terminal when prompted.
    - The script will exchange the code for a refresh token.

5.  **Save the Refresh Token**:
    - The script will print your refresh token.
    - Copy this token and add it to your `.env` file or Claude Desktop
      configuration as `GOOGLE_ADS_REFRESH_TOKEN`.

"""

import os
import sys
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

# The scope for the Google Ads API
SCOPES = ["https://www.googleapis.com/auth/adwords"]
SCRIPT_DIR = Path(__file__).resolve().parent
CLIENT_SECRETS_FILE = SCRIPT_DIR / "client_secrets.json"

def main():
    """Main function to generate the refresh token."""
    print("="*60)
    print("Google Ads MCP - Refresh Token Generator")
    print("="*60)
    print()

    # Check for client_secrets.json
    if not CLIENT_SECRETS_FILE.exists():
        print(f"❌ Error: `{CLIENT_SECRETS_FILE}` not found.")
        print("Please download your OAuth 2.0 client ID JSON file from the")
        print("Google Cloud Console and save it in the same directory as this script.")
        sys.exit(1)

    print(f"✅ Found `{CLIENT_SECRETS_FILE}`.")
    print()

    try:
        # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow.
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

        # The user will be directed to this URL to authorize the application.
        # This will open a new browser window.
        print("🔐 Starting OAuth 2.0 flow...")
        print("Your browser should open for you to authorize access.")
        
        credentials = flow.run_local_server(port=0)

        refresh_token = credentials.refresh_token

        print("\n" + "="*60)
        print("🎉 SUCCESS! Refresh token generated.")
        print("="*60)
        print()
        print("Your Refresh Token is:")
        print(f"\n{refresh_token}\n")
        print("ℹ️  Copy this token and add it to your .env file or Claude Desktop config:")
        print("   GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token_here")
        print()

    except Exception as e:
        print(f"\n❌ An error occurred during the OAuth 2.0 flow: {e}")
        print("\n💡 Troubleshooting:")
        print("  - Ensure your OAuth client ID is for a 'Desktop app'.")
        print("  - Verify the `client_secrets.json` file is correct and not corrupted.")
        print("  - Make sure you are logged into the correct Google account with Ads access.")
        sys.exit(1)

if __name__ == "__main__":
    main()
