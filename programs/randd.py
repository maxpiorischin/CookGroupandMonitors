import webbrowser
import re

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('https://google.com', new=1, autoraise=True)



def openlink(text):
    url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    firsturl = url[0]
    webbrowser.get(chrome_path).open(firsturl, new=1, autoraise=True)

txt = "bla hello jsijs ad https://www.google.com EEE ddd o"
openlink(txt)