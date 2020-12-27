import requests
import json
import time
from discord_webhook import DiscordWebhook
from multiprocessing import Process


# ----------------------------------------------------------------------------------------
def siteupdate(main_list, main_id_list, jsonlink, link, sitename, webhook, proxies):
    global livestock_list, nrml_list, bb_list, kith_list, livestock_id_list, nrml_id_list, bb_id_list, kith_id_list
    n = requests.get(jsonlink, proxies=proxies)
    temp_list = json.loads(n.text)['products']
    temp_id_list = []
    for tempid in temp_list:
        temp_id_list.append(tempid['id'])
        if temp_id_list == main_id_list:
            # print("No Livestock Change")
            return main_list  # Return same list, to recompare after
    for item in temp_list:
        if item['id'] not in main_id_list:  # Finds new item not in old list
            print(("New Item {}: {}").format(sitename, item['title']))
            shoe_url = link + item['handle']
            webhook = DiscordWebhook(
                url=webhook,
                content=shoe_url, user=sitename)
            webhook.execute()
    print('Not same list')
    if sitename == 'Livestock':
        livestock_list = temp_list
        livestock_id_list = temp_id_list
    if sitename == 'nrml':
        nrml_list = temp_list
        nrml_id_list = temp_id_list
    if sitename == 'bbbranded':
        livestock_list = temp_list
        nrml_id_list = temp_id_list
    if sitename == 'Kith':
        livestock_list = temp_list
        nrml_id_list = temp_id_list


# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    livestockrunning = True
    nrmlrunning = True
    bbbrandedrunning = True
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
    allwebhook = 'https://discordapp.com/api/webhooks/751671463660093520/MiMV4BA4qldw2omwVI-37AI_G3eWDIaaRlZKMCX192zpqxudfVLdR2NbZn9-28HrjyiC'
    livestock_list = []
    livestock_id_list = []
    nrml_list = []
    nrml_id_list = []
    bb_list = []
    bb_id_list = []
    kith_list = []
    kith_id_list = []
    isproxies = input('Use Proxies? (Y or N)').lower()
    delaytime = int(input('Monitor Delay:'))
    isYeezy = input('Yeezys?(Y or N)').lower()
    if isYeezy == 'y':
        livestocklink = livestockyeezylink
        livestocklinkjson = livestockyeezylinkjson
    proxies = {}
    if isproxies != 'n':
        proxies = {'https': 'https://maximpiorischin8390:421debdacc9a9dfea41Aa@ca.slashproxies.io:20000',
                'http': 'https://maximpiorischin8390:421debdacc9a9dfea41Aa@ca.slashproxies.io:20000'}
    # todo add proxies, add more variables
    print("Starting to monitor!")
    if livestockrunning:
        live = requests.get(livestocklinkjson)
        livestock_list = json.loads(live.text)['products']
        for liveid in livestock_list:
            livestock_id_list.append(liveid['id'])

    if nrmlrunning:
        nr = requests.get(nrmllinkjson)
        nrml_list = json.loads(nr.text)['products']
        for nrmlid in nrml_list:
            nrml_id_list.append(nrmlid['id'])

    if bbbrandedrunning:
        bb = requests.get(bblinkjson)
        bb_list = json.loads(bb.text)['products']
        for bbid in bb_list:
            bb_id_list.append(bbid['id'])

    if kithrunning:
        kth = requests.get(kithlinkjson)
        kith_list = json.loads(kth.text)['products']
        for kthid in kith_list:
            kith_id_list.append(kthid['id'])

    while True:
        processes = []
        time.sleep(delaytime)
        if livestockrunning:
            proc = Process(target=siteupdate,
                           args=[livestock_list, livestock_id_list, livestocklinkjson, livestocklink, 'Livestock',
                                 allwebhook, proxies])
            processes.append(proc)
            proc.start()
        if nrmlrunning:
            proc = Process(target=siteupdate,
                           args=[nrml_list, nrml_id_list, nrmllinkjson, nrmllink, 'nrml', allwebhook, proxies])
            processes.append(proc)
            proc.start()
        if bbbrandedrunning:
            proc = Process(target=siteupdate,
                           args=[bb_list, bb_id_list, bblinkjson, bblink, 'bbbranded', allwebhook, proxies])
            processes.append(proc)
            proc.start()

        if kithrunning:
            proc = Process(target=siteupdate,
                           args=[kith_list, kith_id_list, kithlinkjson, kithlink, 'Kith',
                                 allwebhook, proxies])
            processes.append(proc)
            proc.start()
        for p in processes:
            p.join()
        print('w')
