import requests
import json
import time
from multiprocessing import Process
from discord_webhook import DiscordWebhook

livestockrunning = False
nrmlrunning = False
bbbrandedrunning = True
# ------------------
livestocklink = "https://www.deadstock.ca/collections/new-arrivals/products/"
nrmllink = "https://nrml.ca/"
bblink = 'https://www.bbbranded.com/collections/all/products/'
livestocklinkjson = "https://www.deadstock.ca/collections/new-arrivals/products.json"
nrmllinkjson = "https://nrml.ca/products.json"
bblinkjson = 'https://www.bbbranded.com/collections/all/products.json'
proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/',
           'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
print("Starting to monitor!")
if livestockrunning:
    live = requests.get(livestocklinkjson, proxies=proxies)
    livestock_list = json.loads(live.text)['products']
if nrmlrunning:
    nr = requests.get(nrmllinkjson, proxies=proxies)
    nrml_list = json.loads(nr.text)['products']

if bbbrandedrunning:
    bb = requests.get(bblinkjson, proxies=proxies)
    bb_list = json.loads(bb.text)['products']


# kith = .... todo add more sites with site functions

# ----------------------------------------------------------------------------------------
def siteupdatelivestock():
    global livestock_list
    n = requests.get(livestocklinkjson, proxies=proxies)
    temp_list = json.loads(n.text)['products']
    livestock_list = temp_list
    print('ez')
    for item in temp_list:
        if item not in livestock_list:
            print("New Item Livestock: ", item['title'])
            shoe_url = livestocklink + item['handle']
            webhook = DiscordWebhook(
                url='https://discordapp.com/api/webhooks/746183940640997426/B6XGuK8UybKsUf1J58XW2IsykZzkoDc_s6SBGldM8E-dCq_dCNZq2p6zToLlbgvcqSyq',
                content=shoe_url, user="livestockfast")
            webhook.execute()


def siteupdatenrml():
    global nrml_list
    n = requests.get(nrmllinkjson, proxies=proxies)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in nrml_list:
            nrml_list = temp_list
            print("New Item nrml: ", item['title'])
            shoe_url = nrmllink + item['handle']
            webhook = DiscordWebhook(
                url='https://discordapp.com/api/webhooks/747665527660347412/BPWVicDUDB5ba_Nsz09kEnB9V0MQIBBUObFu1fadrwwtKlzQGZE6uCtN_EmLXVUcVilF',
                content=shoe_url, user="nrmlfast")
            webhook.execute()
    nrml_list = temp_list


def siteupdatebbbranded():
    global bb_list
    n = requests.get(bblinkjson, proxies=proxies)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in bb_list:
            print("New Item bbbranded: ", item['title'])
            shoe_url = bblink + item['handle']
            webhook = DiscordWebhook(
                url="https://discordapp.com/api/webhooks/749008642606366812/gKO18ulA1RXl1Vep444P0YoAgxuJ9CEBQ3Z4IDBT5Cr2nLdAUW2gt88bz827_pBM0G_q",
                content=shoe_url, user="BBBrandedfast")
            webhook.execute()
    bb_list = temp_list


# --------------------------------------------------------------------------------------------------
# todo multi precessing
if __name__ == "__main__":
    while True:
        processes = []
        print("ez")
        if livestockrunning:
            proc = Process(target=siteupdatelivestock)
            processes.append(proc)
            proc.start()
        if nrmlrunning:
            proc = Process(target=siteupdatenrml)
            processes.append(proc)
            proc.start()
        if bbbrandedrunning:
            proc = Process(target=siteupdatebbbranded)
            processes.append(proc)
            proc.start()
        for p in processes:
            p.join()
        print('ok')
