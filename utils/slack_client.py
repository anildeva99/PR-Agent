import os
import json
import requests
 # test ne chane

# test 555
def send_slack_message(message: str):

    url = os.getenv("SLACK_WEBHOOK_URL")
 
    if not url:
        print("SLACK_WEBHOOK_URL is missing")
        return
 
    payload = {"text": message}

    try:
        r = requests.post(
            url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        print("Slack status:", r.status_code)
        print("Slack response:", r.text)
 
    except Exception as e:
        print("Slack error:", e)