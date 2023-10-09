# SlackStatusChanger
Simple python app to change slack users status in case they are unavailable and can't change it themselves


# Slack Status Updater

This script allows you to set a specific status for multiple users on Slack using the Slack API.

## Requirements

- Python 3.x
- `slack_sdk` library

## Installation

1. Install the `slack_sdk` library using pip:

```bash
pip install slack-sdk
```

2. Create a Slack app and obtain a User OAuth Token with `users.profile:write` scope. Set this token as an environment variable named `SLACK_USER_TOKEN`:

```bash
export SLACK_USER_TOKEN='your-user-token-here'
```

## Usage

Run the script from the command line, passing the User IDs as arguments:

```bash
python script.py <user-id-1> <user-id-2> ...
```

The script will set the specified status for each User ID provided.

## Code Structure

- `set_status` function: This function takes a `WebClient` instance, a user ID, and status details, and sets the status for the specified user.
- `main` function: This function checks command line arguments, initializes a `WebClient` instance, and iterates through the User IDs, calling `set_status` for each one.

Ensure you have the necessary permissions to modify user statuses in your Slack workspace.
