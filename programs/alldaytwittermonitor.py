import tweepy
from discord_webhook import DiscordWebhook
import Webhooks
import webbrowser
import re

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
consumer_key = Webhooks.consumer_key
consumer_secret = Webhooks.consumer_secret
access_token = Webhooks.access_token
access_token_secret = Webhooks.access_token_secret
webhooklink = Webhooks.webhookltwitter

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

    'yeezy2502': '735996213179371520'
}
list_of_keywords = ['restock', 'password']

def openlink(text):
    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    for url in urls:
        webbrowser.get(chrome_path).open(url, new=1, autoraise=True)

print('starting to monitor!')
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name.lower() in botdict and not hasattr(status, 'retweeted_status'):
            openlink(status.text)
            disc_post = "**{}** tweeted:  {}".format(status.user.name, status.text)
            webhook = DiscordWebhook(
                url=webhooklink,
                content=disc_post)
            webhook.execute()
            print("**{} tweeted:** {}".format(status.user.screen_name, status.text))
            print(disc_post)
            for keyword in list_of_keywords:
                if keyword in status.text.lower():
                    role_mention = '<@&752003786721067138> {} RESTOCKING'.format(status.user.screen_name)
                    webhook = DiscordWebhook(
                        url=webhooklink,
                        content=role_mention)
                    webhook.execute()
                    print('BOT RESTOCK!')
if __name__ == '__main__':
    botidlist = []
    for item in botdict:
        botidlist.append(botdict[item])
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(
        follow=botidlist, is_async=True)