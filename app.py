import sys
import logging
from slack_sdk import WebClient
import json
import os
import datetime

# Enable detailed logging with logging.DEBUG
logging.basicConfig(level=logging.WARN)

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_ID = 'C03M034MFAS'

if SLACK_BOT_TOKEN is None:
    print('Please define the env variable SLACK_BOT_TOKEN')
    sys.exit(1)


def main():

    client = WebClient(SLACK_BOT_TOKEN)

    latest = datetime.datetime.utcnow() - datetime.timedelta(minutes=45)
    response = client.conversations_history(channel=CHANNEL_ID, oldest=latest.timestamp())

    msgs = response['messages']

    print("All recent messages:")
    for msg in msgs:
        print(msg)

    notification_msgs = [msg for msg in msgs if msg['subtype'] == 'bot_message' and 'attachments' in msg and 'went from' in msg['attachments'][0]['title']]

    print("Relevant recent messages:")
    for msg in notification_msgs:
        print(msg)

    success = len(notification_msgs) > 0
    if success:
        print(f"{len(notification_msgs)} recent notifications detected, check successful")
        sys.exit(0)
    else:
        print("There were no recent notifications, check unsuccessful")
        sys.exit(1)


if __name__ == '__main__':
    main()
