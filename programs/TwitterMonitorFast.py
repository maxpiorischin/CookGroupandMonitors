import tweepy
from discord_webhook import DiscordWebhook

bot = input('input bot twitter username:')
#Big Win

consumer_key = '1SFD2HvUdlgdSDwvqjKNvGBKc'
consumer_secret = 'TSxU9m4EBqS96EPckEYfDWIEkdVHjOYfL2aUO43YD5VZE0cMV9'
access_token = '994587180130447360-8dPaxUKVAcqnbEK2HqY3B7vVYfvdc35'
access_token_secret = 'eCrLFIfYqlCFzUch872BpBxJDiZmLpZWuLYZOl8FePQxe'
webhooklink = 'https://discordapp.com/api/webhooks/749497271560831047/Dlo3B_Jci7AFbO4L5lX8tAiG0BN_w2a4J5NFxKNNMVCUmduyXtHS4bnd1x1oLkpK3qBK'

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

    'tvyeet': '994587180130447360',

    'splashforcebot': '910500300594786305',

}
print('starting to monitor!')
print(bot)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name.lower() == bot and not hasattr(status, 'retweeted_status'):
            disc_post = "**{}** tweeted:  {}".format(status.user.name, status.text)
            webhook = DiscordWebhook(
                url=webhooklink,
                content=disc_post)
            webhook.execute()
            print("**{} tweeted:** {}".format(status.user.screen_name, status.text))


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(
    follow=[botdict[bot]], is_async=True)
