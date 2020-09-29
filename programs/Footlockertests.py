import requests
from urllib import request
import json
import time
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup

flrunning = True
# ------------------
footlockerlink = 'https://www.footlocker.ca/en/category/new-arrivals'
proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/',
           'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
print("Starting to monitor!")
fl = requests.get(footlockerlink, headers={'Referer': 'https://www.google.com/', "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' })
tempsoup = BeautifulSoup(fl.content, 'html.parser')
temp_list = tempsoup.find_all(class_='product-container col')
for item in temp_list:
    print (item.a['href'])
print('hm')
print(fl.status_code)


