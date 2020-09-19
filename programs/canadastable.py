import requests
import json
import time
from discord_webhook import DiscordWebhook

livestockrunning = True
nrmlrunning = True
bbbrandedrunning = True
# ------------------
shopifyallwebhook = 'https://discordapp.com/api/webhooks/751671463660093520/MiMV4BA4qldw2omwVI-37AI_G3eWDIaaRlZKMCX192zpqxudfVLdR2NbZn9-28HrjyiC'
livestock_webhook_list = [
    "https://discordapp.com/api/webhooks/746485840498130944/FTQrIYfouLCswGs45JEvfdAlENksuHyY3AYFGgWj5yY546KXCdCL40wcsE4Jkne2Ykn8",
    shopifyallwebhook]
nrml_webhook_list = [
    'https://discordapp.com/api/webhooks/747662610333433928/O4Md3uhXoYLTpm7PnogaDbLQKTv4y4f9XE9MDrInZSCSthQceLITrWau8EeEvaXYdzWF',
    shopifyallwebhook]
bbbranded_webhook_list = [
    "https://discordapp.com/api/webhooks/749008549685887026/8E-JyhhBQ9uF96tEYSA0_NGF8jZOf89ZwVDFczhgU6Xs8qJBh_w_QPB94EbT8_d4iYiA",
    shopifyallwebhook]
# ------------------------------------------------------------------------------
livestocklink = "https://www.deadstock.ca/collections/new-arrivals/products/"
nrmllink = "https://nrml.ca/"
bblink = 'https://www.bbbranded.com/collections/all/products/'
livestocklinkjson = "https://www.deadstock.ca/collections/new-arrivals/products.json"
nrmllinkjson = "https://nrml.ca/products.json"
bblinkjson = 'https://www.bbbranded.com/collections/all/products.json'
# todo add proxies, add more variables
print("Starting to monitor!")
if livestockrunning:
    live = requests.get(livestocklinkjson)
    livestock_list = json.loads(live.text)['products']
    livestock_id_list = []
    for liveid in livestock_list:
        livestock_id_list.append(liveid['id'])

if nrmlrunning:
    nr = requests.get(nrmllinkjson)
    nrml_list = json.loads(nr.text)['products']
    nrml_id_list = []
    for nrmlid in nrml_list:
        nrml_id_list.append(nrmlid['id'])

if bbbrandedrunning:
    bb = requests.get(bblinkjson)
    bb_list = json.loads(bb.text)['products']
    bb_id_list = []
    for bbid in bb_list:
        bb_id_list.append(bbid['id'])


# kith = .... todo add more sites with site functions

# ----------------------------------------------------------------------------------------
def siteupdatelivestock():
    global livestock_list, livestock_id_list
    n = requests.get(livestocklinkjson)
    if n.status_code != 200:
        time.sleep(60)
        print('error livestock')
    else:
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
        if temp_id_list == livestock_id_list:
            #print("No Livestock Change")
            pass
            # Condition Checks if lists are identical, if yes, loop repeats
        else:
            # If lists arent identical, find the difference and print (Upload to disc) each one
            for item in temp_list:
                if item["id"] not in livestock_id_list:
                    print("New Item Livestock: ", item['title'])
                    shoe_url = livestocklink + item['handle']
                    webhook = DiscordWebhook(
                        url=livestock_webhook_list,
                        content=shoe_url, user="LivestockBot")
                    webhook.execute()
            livestock_list = temp_list
            livestock_id_list = temp_id_list
            print("Change!")


def siteupdatenrml():
    global nrml_list, nrml_id_list
    n = requests.get(nrmllinkjson)
    if n.status_code != 200:
        time.sleep(60)
        print('error nrml')
    else:
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
        if temp_id_list == nrml_id_list:
            #print("No nrml Change")
            pass
            # Condition Checks if lists are identical, if yes, loop repeats
        else:
            # If lists arent identical, find the difference and print (Upload to disc) each one
            for item in temp_list:
                if item["id"] not in nrml_id_list:
                    print("New Item nrml: ", item['title'])
                    shoe_url = nrmllink + item['handle']
                    webhook = DiscordWebhook(
                        url=nrml_webhook_list,
                        content=shoe_url, user="NrmlBot")
                    webhook.execute()
            nrml_list = temp_list
            nrml_id_list = temp_id_list
            print("Change!")

def siteupdatebbbranded():
    global bb_list, bb_id_list
    n = requests.get(bblinkjson)
    if n.status_code != 200:
        time.sleep(60)
        print('error bb')
    else:
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
        if temp_id_list == bb_id_list:
            #print("No bbbranded Change")
            pass
            # Condition Checks if lists are identical, if yes, loop repeats
        else:
            # If lists arent identical, find the difference and print (Upload to disc) each one
            for item in temp_list:
                if item["id"] not in bb_id_list:
                    print("New Item bbbranded: ", item['title'])
                    shoe_url = bblink + item['handle']
                    webhook = DiscordWebhook(
                        url=bbbranded_webhook_list,
                        content=shoe_url, user="BBBrandedBot")
                    webhook.execute()
            bb_list = temp_list
            bb_id_list = temp_id_list
            print("Change!")


# --------------------------------------------------------------------------------------------------
# todo multi precessing

if __name__ == "__main__":
    while True:
        time.sleep(7)
        if livestockrunning:
            siteupdatelivestock()
        if nrmlrunning:
            siteupdatenrml()
        if bbbrandedrunning:
            siteupdatebbbranded()
