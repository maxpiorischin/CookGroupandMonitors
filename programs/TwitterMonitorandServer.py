import tweepy
from discord_webhook import DiscordWebhook
import time
import webbrowser
import re
import Webhooks

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
consumer_key = Webhooks.consumer_key
consumer_secret = Webhooks.consumer_secret
access_token = Webhooks.access_token
access_token_secret = Webhooks.access_token_secret
webhooklink = Webhooks.webhookltwitter
webhookkiryl = Webhooks.webhooktwitterkiryl

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('starting to monitor!')
mybot = input('Input Bot to monitor')

def openlink(text):
    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    for url in urls:
        webbrowser.get(chrome_path).open(url, new=1, autoraise=True)

if __name__ == '__main__':
    new_tweets = api.user_timeline(count=3, tweet_mode="extended", screen_name = '@'+ mybot, exclude_replies=True)
    latest_tweet = new_tweets[0].full_text
    while True:
        new_tweets = api.user_timeline(count = 1, tweet_mode = "extended", screen_name = '@'+ mybot,  exclude_replies = True)
        for i in new_tweets:
            x = i.full_text
            if x != latest_tweet:
                openlink(x)
                disc_post = "**{}** tweeted:  {}".format(i.user.name, x)
                webhook = DiscordWebhook(
                    url=webhooklink,
                    content=disc_post)
                webhook.execute()
                print(i.user.name, x)
                latest_tweet = x
        time.sleep(1)
