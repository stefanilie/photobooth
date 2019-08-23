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
f=open('photos.txt', 'r')

data = f.read()
f.close()
f=open('photos.txt', 'w')
# file_count = len(files)-25
#f.seek(0)
new=int(data)+1
f.write(str(new))
f.close()
if int(data) == 175 or int(data) == 105:
  send_message("`Poze facute:` "+str(data))
  send_message("SCHIMBA ROLA!")
if int(data) % 25 == 0:
  send_message("`Poze facute:` "+str(data))
  os.system('rm -rf *.jpg')
