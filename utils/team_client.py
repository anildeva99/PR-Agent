import os
import json
import requests

def send_teams_message(message: str):

    url = os.getenv("TEAMS_WEBHOOK_URL")

    if not url:
        print("TEAMS_WEBHOOK_URL is missing")
        return

    # Teams requires "text" inside a card-like object
    payload = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "summary": "Notification",
        "text": message
    }

    try:
        r = requests.post(
            url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        print("Teams status:", r.status_code)
        print("Teams response:", r.text)

    except Exception as e:
        print("Teams error:", e)