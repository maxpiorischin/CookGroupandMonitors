import requests
import time
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

havenrunning = True
# ------------------
havenlink = 'https://shop.havenshop.com/collections/new-arrivals'
allwebhook = 'https://discordapp.com/api/webhooks/757788317243932754/_MQtbVKwX7NltbVj5wXdgcujUV20S7KPqFQ27wC8-sdTeKhaCQaZSO_g5xWNhJKam8aA'
proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/',
           'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
print("Starting to monitor!")
if havenrunning:
    hav = requests.get(havenlink, proxies)
    havensoup = BeautifulSoup(hav.content, 'html.parser')
    haven_list = havensoup.find_all(class_='product-card-name')
# ----------------------------------------------------------------------------------------
def siteupdatehaven():
    global haven_list
    n = requests.get(havenlink, proxies)
    tempsoup = BeautifulSoup(n.content, 'html.parser')
    temp_list = tempsoup.find_all(class_='product-card-name')
    for item in temp_list:
        if item not in haven_list:
            print("New Item Haven: ", item.text)
            url = item.text.replace(' ', '-')
            urlend = '/products/' + url
            shoe_url = havenlink + urlend
            webhook = DiscordWebhook(
                url=allwebhook,
                content=shoe_url, user="haven")
            webhook.execute()
    haven_list = temp_list

while True:
    time.sleep(5)
    if havenrunning:
        siteupdatehaven()
    print('w')