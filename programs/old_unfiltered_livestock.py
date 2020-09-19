import requests
import json
import time
from discord_webhook import DiscordWebhook
r = requests.get("https://www.deadstock.ca/collections/new-arrivals/products.json")
global_list = json.loads(r.text)['products']
livestock = True  #livestock bot working
#add proxies


def siteupdate():
    global global_list
    n = requests.get("https://www.deadstock.ca/collections/new-arrivals/products.json")
    temp_list = json.loads(n.text)['products']
    if temp_list == global_list:
        print("No Change")
        # Condition Checks if lists are identical, if yes, loop repeats
    else:
        # If lists arent identical, find the difference and print (Upload to disc) each one
        for item in temp_list:
            if item not in global_list:
                print("New Item: ", item['title'])
                shoe_url = 'https://www.deadstock.ca/collections/new-arrivals/products/' + item['handle']
                webhook = DiscordWebhook(
                    url='https://discordapp.com/api/webhooks/746183940640997426/B6XGuK8UybKsUf1J58XW2IsykZzkoDc_s6SBGldM8E-dCq_dCNZq2p6zToLlbgvcqSyq',
                    content=shoe_url)
                webhook.execute()
                # add print link here, send it to webhook
                print("New Item!!")
            else:
                print('Item Removed!')
        global_list = temp_list
        print("Change!")


if __name__ == "__main__":
    while livestock:
        siteupdate()
        time.sleep(2.5)


