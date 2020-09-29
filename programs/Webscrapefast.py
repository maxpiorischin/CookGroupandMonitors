import requests
import time
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

footlockercarunning = True
havenrunning = True
# ------------------
havenlink = 'https://shop.havenshop.com/collections/new-arrivals'
footlockercalink = 'https://www.footlocker.ca/en/category/new-arrivals'
havenwebhook = 'https://discordapp.com/api/webhooks/757788317243932754/_MQtbVKwX7NltbVj5wXdgcujUV20S7KPqFQ27wC8-sdTeKhaCQaZSO_g5xWNhJKam8aA'
footlockercanadawebhook = 'https://discordapp.com/api/webhooks/760364048004546591/mBKXd0uL66acDZVVzJd4_XIPgi_JOK_c7W_FYwp9DkdXCnfX1QLhRVwV7zorzc3WN8v6'
allwebhook = 'https://discordapp.com/api/webhooks/751671463660093520/MiMV4BA4qldw2omwVI-37AI_G3eWDIaaRlZKMCX192zpqxudfVLdR2NbZn9-28HrjyiC'
print("Starting to monitor!")
if havenrunning:
    hav = requests.get(havenlink)
    havensoup = BeautifulSoup(hav.content, 'html.parser')
    haven_list = havensoup.find_all(class_='product-card-name')
if footlockercarunning:
    flca = requests.get(footlockercalink, headers = {'Referer': 'https://www.google.com/', "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' })
    flcasoup = BeautifulSoup(flca.content, 'html.parser')
    flca_list = flcasoup.find_all(class_='product-container col')
# ----------------------------------------------------------------------------------------
def siteupdatehaven():
    global haven_list
    n = requests.get(havenlink)
    tempsoup = BeautifulSoup(n.content, 'html.parser')
    temp_list = tempsoup.find_all(class_='product-card-name')
    for item in temp_list:
        if item not in haven_list:
            print("New Item Haven: ", item.text)
            url = item.text.replace(' ', '-')
            urlend = '/products/' + url
            shoe_url = havenlink + urlend
            webhook = DiscordWebhook(
                url=havenwebhook,
                content=shoe_url, user="haven")
            webhook.execute()
    haven_list = temp_list

def siteupdateflca():
    global flca_list
    n = requests.get(footlockercalink, headers={'Referer': 'https://www.google.com/', "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' })
    tempsoup = BeautifulSoup(n.content, 'html.parser')
    temp_list = tempsoup.find_all(class_='product-container col')
    for item in temp_list:
        if item not in flca_list:
            print("New Item FootlockerCanada: ", item.a['href'])
            urlend = item.a['href']
            shoe_url = "https://footlocker.ca" + urlend
            webhook = DiscordWebhook(
                url=footlockercanadawebhook,
                content=shoe_url, user="FLCA")
            webhook.execute()
            webhook2 = DiscordWebhook(
                url=allwebhook,
                content=shoe_url, user="FLCA")
            webhook2.execute()
    flca_list = temp_list

if __name__ == "__main__":
    while True:
        time.sleep(5)
        if havenrunning:
            siteupdatehaven()
        if footlockercalink:
            siteupdateflca()
        print('w')
