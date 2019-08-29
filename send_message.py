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

send_message(sys.argv[1])
