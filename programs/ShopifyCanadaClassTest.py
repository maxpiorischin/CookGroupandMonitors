import requests
import json
import time
from discord_webhook import DiscordWebhook
from multiprocessing import Process, Queue


# ----------------------------------------------------------------------------------------
class ShopifySite:
    def __init__(self, main_list, main_id_list, jsonlink, link, sitename, webhook, proxies):
        self.main_list = main_list
        self.main_id_list = main_id_list
        self.jsonlink = jsonlink
        self.link = link
        self.sitename = sitename
        self.webhook = webhook
        self.queue = Queue()
        self.proxies = proxies

    def siteupdate(self):
        n = requests.get(self.jsonlink, proxies=proxies)
        temp_list = json.loads(n.text)['products']
        temp_id_list = []
        for tempid in temp_list:
            temp_id_list.append(tempid['id'])
            if temp_id_list == self.main_id_list:
                # print("No Livestock Change")
                return self.main_list  # Return same list, to recompare after
        for item in temp_list:
            if item['id'] not in self.main_id_list:  # Finds new item not in old list
                print("New Item {}: {}").format(self.sitename, item['title'])
                shoe_url = self.link + item['handle']
                webhook = DiscordWebhook(
                    url=self.webhook,
                    content=shoe_url, user=self.sitename)
                webhook.execute()
        main_list = temp_list
        self.queue.put(main_list)


# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    livestockrunning = True
    nrmlrunning = True
    bbbrandedrunning = True
    # ------------------
    livestocklink = "https://www.deadstock.ca/collections/new-arrivals/products/"
    nrmllink = "https://nrml.ca/"
    bblink = 'https://www.bbbranded.com/collections/all/products/'
    livestocklinkjson = "https://www.deadstock.ca/collections/new-arrivals/products.json"
    nrmllinkjson = "https://nrml.ca/products.json"
    bblinkjson = 'https://www.bbbranded.com/collections/all/products.json'
    livestockwebhook = 'https://discordapp.com/api/webhooks/752042313727082579/wWTjZUsYuWSCR-js-6gA9mSp2EKj0sBtXPBVdRCRkJL8y9thnVkMYH85WJjtHGGZE0ud'
    nrmlwebhook = 'https://discordapp.com/api/webhooks/752042422950953033/4RpX9y-t6OLhRPSaoXVKbVz_AznsmgLN9sRNJC-m-nH9ca1Me7PQAM3SuBYPRdzisgVV'
    bbbrandedwebhook = "https://discordapp.com/api/webhooks/751999828657176667/M-AM-KfjIbiSiFeoQnD-giFbqw_IydkDUhvEJJUHvB1qTTxCJuHQS9kcE_F6JHhB9vR7"
    livestock_list = []
    livestock_id_list = []
    nrml_list = []
    nrml_id_list = []
    bb_list = []
    bb_id_list = []
    isproxies = input('Use Proxies? (Y or N)').lower()
    delaytime = int(input('Monitor Delay:'))
    proxies = {}
    if isproxies != 'n':
        proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@shpfy26.slashproxies.io:40000',
                'http': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@shpfy26.slashproxies.io:40000'}
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
    livestock = ShopifySite(livestock_list, livestock_id_list, livestocklinkjson, livestocklink, 'Livestock',
                                 livestockwebhook, proxies)
    nrml = ShopifySite(nrml_list, nrml_id_list, nrmllinkjson, nrmllink, 'nrml', nrmlwebhook, proxies)
    bbbranded = ShopifySite(bb_list, bb_id_list, bblinkjson, bblink, 'bbbranded', bbbrandedwebhook, proxies)
    while True:
        q = Queue()
        rets = []
        processes = []
        time.sleep(delaytime)
        if livestockrunning:
            proc = Process(target=livestock.siteupdate())
            proc.start()
        if nrmlrunning:
            proc = Process(target=nrml.siteupdate(),
                           args=[nrml_list, nrml_id_list, nrmllinkjson, nrmllink, 'nrml', nrmlwebhook, proxies])
            proc.start()
        if bbbrandedrunning:
            proc = Process(target=bbbranded.siteupdate(),
                           args=[bb_list, bb_id_list, bblinkjson, bblink, 'bbbranded', bbbrandedwebhook, proxies])
            proc.start()
        for p in processes:
            ret = q.get()
            livestock_list = ret[0]
            nrml_list = ret[1]
            bb_list = ret[2]
            rets.append(ret)
        for p in processes:
            p.join()
        print('w')
