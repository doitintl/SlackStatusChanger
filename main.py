import sys
import os
from slack_sdk import WebClient

def set_status(client, user_id, status_text, status_emoji, status_expiration):
    response = client.users_profile_set(
        user=user_id,
        profile={
            "status_text": status_text,
            "status_emoji": status_emoji,
            "status_expiration": status_expiration
        }
    )

    if not response['ok']:
        print(f"Error for {user_id}: {response['error']}")
    else:
        print(f"Status set for {user_id}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <user-id-1> <user-id-2> ...")
        sys.exit(1)

    token = os.getenv('SLACK_USER_TOKEN')
    if not token:
        print("Error: SLACK_USER_TOKEN environment variable not set")
        sys.exit(1)

    client = WebClient(token=token)

    status_text = "Out of Office"
    status_emoji = ":house:"
    status_expiration = 0

    for user_id in sys.argv[1:]:
        set_status(client, user_id, status_text, status_emoji, status_expiration)

if __name__ == "__main__":
    main()
