import sys
import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class SlackBot(object):
    def __init__(self, bottoken=None, channelid=None):
        self.client = WebClient(token=bottoken)
        self.channel_id = channelid  # replace with the channel ID you want to send the message to

    def send_message(self, message):
        try:
            response = self.client.chat_postMessage(
                channel=self.channel_id,
                text=message
            )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            #assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
            logger.error({'action': 'send', 'status': 'false', 'error':e.response["error"]})

if __name__ == '__main__':
    #Slack OAuth Tokens
    token=''
    #Slack Channel ID for Message
    channel_id=''
    slackbot = SlackBot(token, channel_id)
    slackbot.send_message('こんにちは')