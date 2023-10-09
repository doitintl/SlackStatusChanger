from slack_sdk import WebClient

# Initialize a Web API client
client = WebClient(token='your-user-token-here')

# Set the user's status
response = client.users_profile_set(
    user='user-id-here',  # User ID of the employee
    profile={
        "status_text": "Out of Office",
        "status_emoji": ":house:",
        "status_expiration": 0  # Status does not expire
    }
)

# Check for errors
if not response['ok']:
    print(f"Error: {response['error']}")
