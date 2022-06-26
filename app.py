import sys
import logging
from slack_sdk import WebClient
import json
import os

logging.basicConfig(level=logging.DEBUG)

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_ID = 'C03K8LKF0CT'

if SLACK_BOT_TOKEN is None:
    print('Please define the env variable SLACK_BOT_TOKEN')
    sys.exit(1)


def main():

    client = WebClient(SLACK_BOT_TOKEN)
    response = client.conversations_history(channel=CHANNEL_ID)

    print(response)

    for msg in response['messages']:
        print(msg)

    success = True
    if success:
        print("Recent notification detected, check successful")
        sys.exit(0)
    else:
        print("There were no recent notifications, check unsuccessful")
        sys.exit(1)


if __name__ == '__main__':
    main()
