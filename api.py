from curl_cffi import requests as r
from datetime import datetime, timezone

from keychain import save_token, get_token, delete_token

def time_unit(iso_string):
    if iso_string is None:
        return "_"
    # Convert the string into real datetime 
    reset_time = datetime.fromisoformat(iso_string)

    # Get Current time 
    now = datetime.now(timezone.utc)

    # How much time is left ?
    diff = reset_time - now

    # Convert it to total seconds 
    total_seconds = int(diff.total_seconds())

    # Break it down
    days    = total_seconds // 86400
    hours   = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    elif hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"

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

    # Get the usage data for the first organization
    resp2 = r.get(f"https://claude.ai/api/organizations/{org_id}/usage", **kw)
    
    if resp2.status_code != 200:
        print(f"Failed to fetch usage. Status code {resp2.status_code}")
        return None

    # Parse the JSON response
    usage_data = resp2.json()

    return usage_data 


def main():
    token = get_token()

    if token is None:
        token = input("Enter your Claude AI session token:")
        save_token(token=token)
        print("Token saved successfully.")


    data = get_claude_data(token)
    if data is not None:
        
        session_usage = data['five_hour']['utilization']
        weekly_usage = data['seven_day']['utilization']
        reset_date = data['seven_day']['resets_at']

        converted_reset_date = time_unit(reset_date)

        print(f"5hr Season   : {(session_usage):.0f}%")
        print(f"Weekly Usage : {(weekly_usage):.0f}%")
        print(f"Reset Date   : {converted_reset_date}")

if __name__ == "__main__":
    main()
