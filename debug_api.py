import json 
from curl_cffi import requests as r
from datetime import datetime, timezone
from keychain import save_token, get_token
from pprint import pprint





def get_claude_data(token):
    cookies = {"sessionKey": token}
    kw = dict(cookies=cookies, impersonate="chrome120")

    # Send GET Request to retrieve organizations list from Claude API
    resp = r.get("https://claude.ai/api/organizations", **kw)

    # Check if request was successful
    if resp.status_code != 200:
        print(f"Failed to fetch organizations. Status code {resp.status_code}")
        return None

    # Extract the UUID of the first organization
    org_id = resp.json()[0]['uuid']
    # print(org_id)  # Print the uuid

    # Get subscription capabilities (e.g. ['chat', 'claude_pro'])
    capabilities = resp.json()[0]['capabilities']

    # Work out a human-readable plan name from the capabilities list
    if len(capabilities) > 1:
        plan = capabilities[-1].removeprefix("claude_").replace("_", " ").title()
    else:
        plan = "Free"

    # Get the usage data for the first organization
    resp2 = r.get(f"https://claude.ai/api/organizations/{org_id}/usage", **kw)

    if resp2.status_code != 200:
        print(f"Failed to fetch usage. Status code {resp2.status_code}")
        return None

    # Parse the JSON response
    usage_data = resp2.json()

    # Add the resolved plan name to usage_data
    usage_data['plan'] = plan

    return usage_data


def main():
    token = get_token()

    if token is None:
        token = input("Enter your Claude AI session token:")
        save_token(token=token)
        print("Token saved successfully.")


    data = get_claude_data(token)
    if data is not None:
        print(f"Plan: Claude {data['plan']}")

if __name__ == "__main__":
    main()
