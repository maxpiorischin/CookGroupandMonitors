import requests
import time
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
from multiprocessing import Process, Queue
import Webhooks

havenrunning = False
footlockercarunning = True
# ------------------
havenlink = 'https://shop.havenshop.com/collections/new-arrivals'
footlockercalink = 'https://www.footlocker.ca/en/category/new-arrivals'
footlockercanadawebhook = Webhooks.webhookfootlocker
allwebhook = Webhooks.allwebhook
proxiesif = input('Proxies?(Y or N').lower()
flca_list = []
haven_list = []
proxies = {}
if proxiesif != 'n':
    proxies = {}
print("Starting to monitor!")
if havenrunning:
    hav = requests.get(havenlink, proxies)
    havensoup = BeautifulSoup(hav.content, 'html.parser')
    haven_list = havensoup.find_all(class_='product-card-name')
if footlockercarunning:
    flca = requests.get(footlockercalink, proxies=proxies, headers={'Referer': 'https://www.google.com/',
                                                                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'})
    flcasoup = BeautifulSoup(flca.content, 'html.parser')
    flca_list = flcasoup.find_all(class_='product-container col')


# ----------------------------------------------------------------------------------------
def siteupdatehaven(link, proxies, webhook):
    global haven_list
    n = requests.get(link, proxies = proxies)
    tempsoup = BeautifulSoup(n.content, 'html.parser')
    temp_list = tempsoup.find_all(class_='product-card-name')
    for item in temp_list:
        if item not in haven_list:
            print("New Item Haven: ", item.text)
            url = item.text.replace(' ', '-')
            urlend = '/products/' + url
            shoe_url = link + urlend
            webhook = DiscordWebhook(
                url=webhook,
                content=shoe_url, user="haven")
            webhook.execute()
    haven_list = temp_list


def siteupdateflca(link, proxies, webhook1, webhook2):
    global flca_list
    n = requests.get(link, proxies=proxies, headers={'Referer': 'https://www.google.com/',
                                                                 "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'})
    tempsoup = BeautifulSoup(n.content, 'html.parser')
    temp_list = tempsoup.find_all(class_='product-container col')
    for item in temp_list:
        if item not in flca_list:
            print("New Item FootlockerCanada: ", item.a['href'])
            urlend = item.a['href']
            shoe_url = "https://footlocker.ca" + urlend
            webhook = DiscordWebhook(
                url=webhook1,
                content=shoe_url, user="FLCA")
            webhook.execute()
            webhook2 = DiscordWebhook(
                url=webhook2,
                content=shoe_url, user="FLCA")
            webhook2.execute()
    flca_list = temp_list


if __name__ == "__main__":
    while True:
        processes = []
        # print('ez')
        if havenrunning:
            proc = Process(target=siteupdatehaven, args= [havenlink, proxies, allwebhook])
            processes.append(proc)
            proc.start()
        if footlockercarunning:
            proc = Process(target=siteupdateflca, args= [footlockercalink, proxies, footlockercanadawebhook, allwebhook])
            processes.append(proc)
            proc.start()

        for p in processes:
            p.join()
