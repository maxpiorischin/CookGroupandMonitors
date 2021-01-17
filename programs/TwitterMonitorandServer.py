import tweepy
from discord_webhook import DiscordWebhook
import time
import webbrowser
import re

consumer_key = '1SFD2HvUdlgdSDwvqjKNvGBKc'
consumer_secret = 'TSxU9m4EBqS96EPckEYfDWIEkdVHjOYfL2aUO43YD5VZE0cMV9'
access_token = '994587180130447360-j2UaEvSpXvgnH6V9GJzgKqU80Tr0iWd'
access_token_secret = 'Pow5JrgUFXwW7KKzpluSqEDV0nnwzvDgfFtdSSGuyTa6A'
webhooklink = 'https://discordapp.com/api/webhooks/749497271560831047/Dlo3B_Jci7AFbO4L5lX8tAiG0BN_w2a4J5NFxKNNMVCUmduyXtHS4bnd1x1oLkpK3qBK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('starting to monitor!')
mybot = input('Input Bot to monitor')
if __name__ == '__main__':
    new_tweets = api.user_timeline(count=1, tweet_mode="extended", screen_name = '@'+ mybot, exclude_replies=True)
    print(new_tweets)
    latest_tweet = new_tweets[0].full_text
    while True:
        new_tweets = api.user_timeline(count = 1, tweet_mode = "extended", screen_name = '@'+ mybot,  exclude_replies = True)
        for i in new_tweets:
            x = i.full_text
            if x != latest_tweet:
                disc_post = "**{}** tweeted:  {}".format(i.user.name, x)
                webhook = DiscordWebhook(
                    url=webhooklink,
                    content=disc_post)
                webhook.execute()
                print(i.user.name, x)
                latest_tweet = x
        time.sleep(1)
