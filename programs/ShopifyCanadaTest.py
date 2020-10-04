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
livestockwebhook = 'https://discordapp.com/api/webhooks/752042313727082579/wWTjZUsYuWSCR-js-6gA9mSp2EKj0sBtXPBVdRCRkJL8y9thnVkMYH85WJjtHGGZE0ud'
nrmlwebhook = 'https://discordapp.com/api/webhooks/752042422950953033/4RpX9y-t6OLhRPSaoXVKbVz_AznsmgLN9sRNJC-m-nH9ca1Me7PQAM3SuBYPRdzisgVV'
bbbrandedwebhook = "https://discordapp.com/api/webhooks/751999828657176667/M-AM-KfjIbiSiFeoQnD-giFbqw_IydkDUhvEJJUHvB1qTTxCJuHQS9kcE_F6JHhB9vR7"
livestock_list = []
nrml_list = []
bb_list = []
isproxies = input('Use Proxies? (Y or N)').lower()
delaytime = int(input('Monitor Delay:'))
proxies = {}
if isproxies != 'n':
    proxies = {'https': 'https://maxsnkrs252165:08621ab5cb7ffe02111Aa@cwda.slashproxies.io:20000/',
               'http': 'http://maxsnkrs252165:08621ab5cb7ffe02111Aa@ca.slashproxies.io:20000/'}
# todo add proxies, add more variables
print("Starting to monitor!")
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
def siteupdate(main_list, jsonlink, link, sitename, webhook):
    n = requests.get(jsonlink, proxies=proxies)
    temp_list = json.loads(n.text)['products']
    for item in temp_list:
        if item not in main_list:
            main_list = temp_list
            print("New Item {}: {}").format(sitename, item['title'])
            shoe_url = link + item['handle']
            webhook = DiscordWebhook(
                url=webhook,
                content=shoe_url, user=sitename)
            webhook.execute()
    main_list = temp_list
    return main_list


# --------------------------------------------------------------------------------------------------
# todo multi precessing
if __name__ == "__main__":
    while True:
        time.sleep(delaytime)
        if livestockrunning:
            livestock_list = siteupdate(livestock_list, livestocklinkjson, livestocklink, 'Livestock', livestockwebhook)
        if nrmlrunning:
            nrml_list = siteupdate(nrml_list, nrmllinkjson, nrmllink, 'nrml', nrmlwebhook)
        if bbbrandedrunning:
            bb_list = siteupdate(bb_list, bblinkjson, bblink, 'bbbranded', bbbrandedwebhook)
        print('w')
