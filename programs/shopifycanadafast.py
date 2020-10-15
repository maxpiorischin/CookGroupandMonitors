import requests
import json
import time
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
# todo add proxies, add more variables
print("Starting to monitor!")
delay = int(input('Input Delay (seconds):'))
if livestockrunning:
    live = requests.get(livestocklinkjson)
    livestock_list = json.loads(live.text)['products']

if nrmlrunning:
    nr = requests.get(nrmllinkjson)
    nrml_list = json.loads(nr.text)['products']

if bbbrandedrunning:
    bb = requests.get(bblinkjson)
    bb_list = json.loads(bb.text)['products']


# kith = .... todo add more sites with site functions

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
                url='https://discordapp.com/api/webhooks/752042313727082579/wWTjZUsYuWSCR-js-6gA9mSp2EKj0sBtXPBVdRCRkJL8y9thnVkMYH85WJjtHGGZE0ud',
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
                url='https://discordapp.com/api/webhooks/752042422950953033/4RpX9y-t6OLhRPSaoXVKbVz_AznsmgLN9sRNJC-m-nH9ca1Me7PQAM3SuBYPRdzisgVV',
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
                url="https://discordapp.com/api/webhooks/751999828657176667/M-AM-KfjIbiSiFeoQnD-giFbqw_IydkDUhvEJJUHvB1qTTxCJuHQS9kcE_F6JHhB9vR7",
                content=shoe_url, user="BBBrandedfast")
            webhook.execute()
    bb_list = temp_list


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
        print('w')
