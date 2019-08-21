import os
import sys
import json 
import requests

from config import URL, CHANNEL_ID

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, CHANNEL_ID, "markdown")
    get_url(url)


path, dirs, files = next(os.walk(os.getcwd()))
file_count = len(files)-25
#if file_count % 50 == 0:
#    send_message("`Poze facute:` "+str(file_count))
send_message("`Poze facute:` "+str(file_count))
