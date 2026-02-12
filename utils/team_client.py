#!/usr/bin/env python3
import os
import sys
import json
import requests

def send_teams_message(message: str) -> None:
    """
    Sends a message to a Microsoft Teams channel via Incoming Webhook.

    Expects the webhook URL in the environment variable TEAMS_WEBHOOK_URL.
    """
    url = os.getenv("TEAMS_WEBHOOK_URL")
    if not url:
        print("ERROR: TEAMS_WEBHOOK_URL is missing. Set it via env (e.g., GitHub Actions secret).", file=sys.stderr)
        sys.exit(1)

    payload = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "summary": "Notification",
        "text": message
    }

    try:
        resp = requests.post(
            url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=15
        )
        # Raise on HTTP errors
        resp.raise_for_status()
        print(f"Sent to Teams: {resp.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ERROR sending to Teams: {e}", file=sys.stderr)
        # Optionally print response text if present (without exposing secrets)
        if 'resp' in locals() and resp is not None:
            print(f"Response: {resp.text}", file=sys.stderr)
        sys.exit(2)

def main():
    # Allow message from CLI; default if none provided
    message = "Hello from Microsoft Teams webhook!"
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    send_teams_message(message)

if __name__ == "__main__":
    main()
