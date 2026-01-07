#!/usr/bin/env python3
"""
Validates Google Ads API queries and mutations.
Ensures skill file was referenced before executing query/mutate operations.
Exempts list_accounts from this requirement.
"""
import json
import sys

def load_hook_input():
    """Load hook input from stdin."""
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

def check_skill_referenced(transcript_path):
    """Check if skill file was referenced in conversation."""
    try:
        with open(transcript_path, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                    content = json.dumps(event).lower()
                    # Check for various skill references
                    if any(ref in content for ref in [
                        'skill',
                        '.skill.md',
                        'google ads skill',
                        'campaign-performance',
                        'search-terms-report',
                        'wasted-spend',
                        'quality-score',
                        'budget-pacing',
                        'add-negative-keywords',
                        'adjust-bids',
                        'account-health-audit',
                        'gaql-errors',
                        'atomic-campaign-performance',
                        'atomic-search-terms-report',
                        'atomic-wasted-spend-analysis',
                        'atomic-quality-score-audit',
                        'atomic-budget-pacing',
                        'atomic-add-negative-keywords',
                        'atomic-adjust-bids',
                        'playbook-account-health-audit',
                        'troubleshooting-gaql-errors'
                    ]):
                        return True
                except json.JSONDecodeError:
                    continue
        return False
    except (FileNotFoundError, IOError):
        # If we can't read transcript, fail open (allow)
        return True

def main():
    hook_input = load_hook_input()

    tool_name = hook_input.get("tool_name", "")
    transcript_path = hook_input.get("transcript_path", "")
    tool_input = hook_input.get("tool_input", {})

    # Only validate Google Ads MCP operations
    if not tool_name.startswith("mcp__google_ads__"):
        sys.exit(0)

    # Exempt list_accounts - safe enumeration
    if "list_accounts" in tool_name.lower():
        sys.exit(0)

    # Only validate query and mutate operations
    if tool_name not in ["mcp__google_ads__query", "mcp__google_ads__mutate"]:
        sys.exit(0)

    # Check if skill was referenced
    if not check_skill_referenced(transcript_path):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason":
                    "Google Ads query/mutate operations require consulting the skill file first. "
                    "This prevents hallucinated or incorrect API queries. "
                    "Please reference the relevant Google Ads skill file to understand the proper "
                    "API structure and parameters before executing this operation."
            }
        }
        print(json.dumps(output))
        sys.exit(0)

    # Skill was referenced, allow execution
    sys.exit(0)

if __name__ == "__main__":
    main()
