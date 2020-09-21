import requests
import json
import time
from multiprocessing import Process
from discord_webhook import DiscordWebhook

livestockrunning = True
nrmlrunning = True
bbbrandedrunning = True
# ------------------
allwebhook = 'https://discordapp.com/api/webhooks/751671463660093520/MiMV4BA4qldw2omwVI-37AI_G3eWDIaaRlZKMCX192zpqxudfVLdR2NbZn9-28HrjyiC'
# ------------------------------------------------------------------------------
livestocklink = "https://www.deadstock.ca/collections/new-arrivals/products/"
nrmllink = "https://nrml.ca/"
bblink = 'https://www.bbbranded.com/collections/all/products/'
livestocklinkjson = "https://www.deadstock.ca/collections/new-arrivals/products.json"
nrmllinkjson = "https://nrml.ca/products.json"
bblinkjson = 'https://www.bbbranded.com/collections/all/products.json'
proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/',
           'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
#print("Starting to monitor!")
if livestockrunning:
    live = requests.get(livestocklinkjson, proxies=proxies)
    livestock_list = json.loads(live.text)['products']
    livestock_id_list = []
    for liveid in livestock_list:
        livestock_id_list.append(liveid['id'])

if nrmlrunning:
    nr = requests.get(nrmllinkjson, proxies=proxies)
    nrml_list = json.loads(nr.text)['products']
    nrml_id_list = []
    for nrmlid in nrml_list:
        nrml_id_list.append(nrmlid['id'])

if bbbrandedrunning:
    bb = requests.get(bblinkjson, proxies=proxies)
    bb_list = json.loads(bb.text)['products']
    bb_id_list = []
    for bbid in bb_list:
        bb_id_list.append(bbid['id'])


# kith = .... todo add more sites with site functions

# ----------------------------------------------------------------------------------------
def siteupdatelivestock():
    global livestock_list, livestock_id_list
    n = requests.get(livestocklinkjson, proxies=proxies)
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
                        url=allwebhook,
                        content=shoe_url, user="LivestockBot")
                    webhook.execute()

            livestock_list = temp_list
            livestock_id_list = temp_id_list
            print("Change!")


def siteupdatenrml():
    global nrml_list, nrml_id_list
    n = requests.get(nrmllinkjson, proxies=proxies)
    if n.status_code != 200:
        time.sleep(60)
        print('error nrml')
    else:
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
        if temp_id_list == nrml_id_list:
            # print("No nrml Change")
            pass
            # Condition Checks if lists are identical, if yes, loop repeats
        else:
            # If lists arent identical, find the difference and print (Upload to disc) each one
            for item in temp_list:
                if item["id"] not in nrml_id_list:
                    print("New Item nrml: ", item['title'])
                    shoe_url = nrmllink + item['handle']
                    webhook = DiscordWebhook(
                        url=allwebhook,
                        content=shoe_url, user="NrmlBot")
                    webhook.execute()
            nrml_list = temp_list
            nrml_id_list = temp_id_list
            print("Change!")


def siteupdatebbbranded():
    global bb_list, bb_id_list
    n = requests.get(bblinkjson, proxies=proxies)
    if n.status_code != 200:
        time.sleep(60)
        print('error bb')
    else:
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
        if temp_id_list == bb_id_list:
            # print("No bbbranded Change")
            pass
            # Condition Checks if lists are identical, if yes, loop repeats
        else:
            # If lists arent identical, find the difference and print (Upload to disc) each one
            for item in temp_list:
                if item["id"] not in bb_id_list:
                    print("New Item bbbranded: ", item['title'])
                    shoe_url = bblink + item['handle']
                    webhook = DiscordWebhook(
                        url=allwebhook,
                        content=shoe_url, user="BBBrandedBot")
                    webhook.execute()
            bb_list = temp_list
            bb_id_list = temp_id_list
            print("Change!")


# --------------------------------------------------------------------------------------------------
# todo multi precessing

if __name__ == "__main__":
    while True:
        processes = []
        #print('ez')
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
