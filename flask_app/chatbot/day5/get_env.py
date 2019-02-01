import os
import requests
from pprint import pprint as pp

token = os.getenv('TELEGRAM_TOKEN')
#method = "getUpdates"
name = os.getenv('NAME')
#method = "getUpdates"
#chat_id = ""

msg = input()

# url = f"https://api.telegram.org/bot{token}/{method}"
# #"https://api.telegram.org/bot{token}/getUpdates"

#token = 636693654:AAFdBC0YcOhS-4FqD87Q9cE4tvvDS4YM0E0
#method = sendMessage
#chat_id = 706212804

# ?chat_id={chat_id}&text={name}"

# string 수술(interpolation)
# 1. f-string
#print(f"Hello, {name}")

# 2. format()
#print("Hello, {}{}{}{}".format("Ashley", token, method, chat_id)) #.format()메쏘드 지정
#print("Hello, {}".format(name))

# res = requests.get(url)
# doc = res.json()
# #json.loads() => python dictionary
# #pp(doc['result'][0]['message']['chat']['id'])

# chat_id = doc['result'][0]['message']['chat']['id']

# method = "sendMessage"
# url = f"https://api.telegram.org/bot{token}/{method}"
# #url = "https://api.telegram.org/bot{token}/sendMessage"
# print(f"{url}?chat_id={chat_id}&text={name}")
# requests.get(f"{url}?chat_id={chat_id}&text={name}")

#"https://api.telegram.org/bot{token}/sendMessage?chat_id="


#AGENDA : 텔레그램 메세지를 보낼거임(sendmessage)
##I. chat_id 받아오는 기능(function => getId())
#1.환경변수를 불러와서
#    - token 환경변수를 불러온다.
#2.url을 만들고
#   - base url을 만들어서
#   - base url + token + method
#3.getUpdates 호출
#4.chat_id받고
#--------------------------------
## II. message를 보내는 기능(funciton)
#5.url 다시만들고
#6.메세지를 보냄

def getId(token):
    url = f"http://api.telegram.org/bot{token}/getUpdates"
    res = requests.get(url)
    doc = res.json()
    #json.loads() => python dictionary
    chat_id = doc['result'][0]['message']['chat']['id']
    # 779667174
    return chat_id

def sendMessage(chat_id, token, message):
    base_url = "https://api.telegram.org"
    url = f"{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    return f"{message}를 {chat_id}님에게 보냈습니다."

print(getId(token))

sendMessage(779667174, token, msg)