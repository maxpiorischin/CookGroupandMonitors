import requests
import json
import time
from discord_webhook import DiscordWebhook
import Webhooks

livestockrunning = False
nrmlrunning = False
bbbrandedrunning = False
kithrunning = True
# ------------------
livestocklink = "https://www.deadstock.ca/collections/new-arrivals/products/"
livestockyeezylink = 'https://www.deadstock.ca/collections/yeezy'
nrmllink = "https://nrml.ca/"
bblink = 'https://www.bbbranded.com/collections/all/products/'
kithlink = 'https://kith.com/collections/new-arrivals'
livestocklinkjson = "https://www.deadstock.ca/collections/new-arrivals/products.json"
livestockyeezylinkjson = 'https://www.deadstock.ca/collections/yeezy/products.json'
nrmllinkjson = "https://nrml.ca/products.json"
bblinkjson = 'https://www.bbbranded.com/collections/all/products.json'
kithlinkjson = 'https://kith.com/collections/new-arrivals/products.json'
# todo add proxies, add more variables
print("Starting to monitor!")
delay = int(input('Input Delay (seconds):'))
isYeezy = input('Yeezys?(Y or N)').lower()
if isYeezy == 'y':
    livestocklink = livestockyeezylink
    livestocklinkjson = livestockyeezylinkjson
if livestockrunning:
    live = requests.get(livestocklinkjson)
    livestock_list = json.loads(live.text)['products']

if nrmlrunning:
    nr = requests.get(nrmllinkjson)
    nrml_list = json.loads(nr.text)['products']

if bbbrandedrunning:
    bb = requests.get(bblinkjson)
    bb_list = json.loads(bb.text)['products']

if kithrunning:
    kth = requests.get(kithlinkjson)
    kith_list = json.loads(kth.text)['products']

# ----------------------------------------------------------------------------------------
def siteupdatelivestock():
    global livestock_list
    n = requests.get(livestocklinkjson)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in livestock_list:
            print("New Item Livestock: ", item['title'])
            shoe_url = livestocklink + item['handle']
            webhook = DiscordWebhook(
                url=Webhooks.webhooklivestock,
                content=shoe_url, user="livestockfast")
            webhook.execute()
    livestock_list = temp_list


def siteupdatenrml():
    global nrml_list
    n = requests.get(nrmllinkjson)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in nrml_list:
            nrml_list = temp_list
            print("New Item nrml: ", item['title'])
            shoe_url = nrmllink + item['handle']
            webhook = DiscordWebhook(
                url=Webhooks.webhooknrml,
                content=shoe_url, user="nrmlfast")
            webhook.execute()
    nrml_list = temp_list


def siteupdatebbbranded():
    global bb_list
    n = requests.get(bblinkjson)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in bb_list:
            print("New Item bbbranded: ", item['title'])
            shoe_url = bblink + item['handle']
            webhook = DiscordWebhook(
                url=Webhooks.webhookbb,
                content=shoe_url, user="BBBrandedfast")
            webhook.execute()
    bb_list = temp_list

def siteupdatekith():
    global kith_list
    n = requests.get(kithlinkjson)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in kith_list:
            print("New Item Kith: ", item['title'])
            shoe_url = kithlink + item['handle']
            webhook = DiscordWebhook(
                url=Webhooks.webhookkith,
                content=shoe_url, user="Kithfast")
            webhook.execute()
    kith_list = temp_list

# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        time.sleep(delay)
        if livestockrunning:
            siteupdatelivestock()
        if nrmlrunning:
            siteupdatenrml()
        if bbbrandedrunning:
            siteupdatebbbranded()
        if kithrunning:
            siteupdatekith()
        print('w')
