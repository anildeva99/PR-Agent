#!/usr/bin/env python3
import os
import sys
import json
import requests

def send_teams_message(message: str):
    url = os.getenv("TEAMS_WEBHOOK_URL")

    if not url:
        print("ERROR: TEAMS_WEBHOOK_URL is missing.")
        sys.exit(1)

    payload = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "summary": "Notification",
        "text": message,
    }

    try:
        r = requests.post(
            url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=15
        )
        r.raise_for_status()
        print("Message sent to Teams:", r.status_code)

    except Exception as e:
        print("ERROR sending to Teams:", e)
        sys.exit(2)

if __name__ == "__main__":
    msg = "Hello from GitHub Actions!"
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    send_teams_message(msg)
