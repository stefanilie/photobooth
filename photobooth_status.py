import os
import sys
import json 
import requests
import pdb
from config import URL, CHANNEL_ID

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, CHANNEL_ID, "markdown")
    get_url(url)

path, dirs, files = next(os.walk(os.getcwd())) 
f=open('photos.txt', 'rw+')
pdb.set_trace()
data = f.read()
file_count = len(files)-25
#f.seek(0)
new=int(data)+1
f.write(str(new))
if file_count == 175 or file_count == 105:
  send_message("`Poze facute:` "+str(file_count))
  send_message("SCHIMBA ROLA!")
if file_count % 25 == 0:
  send_message("`Poze facute:` "+str(file_count))
