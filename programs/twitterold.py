import tweepy
from discord_webhook import DiscordWebhook
import webbrowser
import re
import Webhooks
#Big Win

consumer_key = Webhooks.consumer_key
consumer_secret = Webhooks.consumer_secret
access_token = Webhooks.access_token
access_token_secret = Webhooks.access_token_secret
webhooklink = Webhooks.webhooktwitterkiryl
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
botdict = {
    'kodaiaio': '1044054193365934081',
    'cybersole': '718857559403270144',
    'wrathbots': '968299339117363200',
    'soleaio': '1001153235179180032',
    'balkobot': '997644265156116480',
    'f3ather': '990276109383225344',
    'adeptbots': '1001896176428441601',
    'destroyerbots': '887790349699227650',
    'prismaio': '1053046389704409089',
    'eveaio': '914897340280053763',
    'theganeshbot': '1258037709660184577',
    'ghostaio': '940121522269691904',
    'hayhabots': '1177590876111085573',
    'kilosoftware': '1219097705986826240',
    'themobilebot': '114508616663470081',
    'mekrobotics': '1133623549791354880',
    'polarisaio': '859003898438328322',
    'veloxpreme': '959483571797921795',
    'restockworld': '1075875489603076096',
    'thenorthcop': '4499047233',
    'osirisrafflebot': '1190094485687947264',
    'pulsaraio': '1181031632804941824',
    're_aio': '1147686467973443584',
    'hawkmesh': '1105057852287340544',

    'tvyeet': '994587180130447360',

    'splashforcebot': '910500300594786305',

    'gizmosolution': '1144858502873014272',

    'zeny_aio': '1218965377482481664',

    'essenceaio': '730120059067219968',

    'estocksoftware': '1156428558845321216',

    'elonmusk': '44196397'

}
print('starting to monitor!')

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name.lower() == bot:
            url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+',status.text)
            webbrowser.open(url[0], new = 1, autoraise=True)
            disc_post = "**{}** tweeted:  {} URLS: {}".format(status.user.name, status.text, url)
            webhook = DiscordWebhook(
                url=webhooklink,
                content=disc_post)
            webhook.execute()
            print("**{} tweeted:** {}".format(status.user.screen_name, status.text))
            print(disc_post)


if __name__ == '__main__':
    bot = input('input bot twitter username:')
    print(bot)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(
        follow=[botdict[bot]], is_async=True)