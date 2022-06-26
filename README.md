# checkson-slack-self-check

This repository creates a Docker image that retrieves the history of a Slack channel.

It validates that Checkson sent notification via the Slack notification channel recently.
The notification are triggered by this Checkson check: https://github.com/checkson-io/checkson-flapping-self-check

The following environment variable must be defined: `SLACK_BOT_TOKEN`. It must contain a 
Slack bot token with the Bot token scope `channels:history` (configurable in OAuth&Permissions
when creating a Slack application)
