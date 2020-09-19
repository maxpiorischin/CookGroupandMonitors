import requests
from urllib import request
import json
import time
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup

flrunning = True
# ------------------
footlockerlink = 'https://www.google.ca'
proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/',
           'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
print("Starting to monitor!")
fl = request.urlopen(footlockerlink)
print('hm')
print(fl.read())


