from flask import Flask, request
import os
from pprint import pprint as pp
import requests
import random

app = Flask(__name__)

token = os.getenv('TELEGRAM_TOKEN') #os야 우리 environment 변수 설정좀 bashrc에서 가져오는것!
base_url = "https://api.hphk.io/telegram" #https://api.telegram.org => telegram에서 웹훅막아놔서 자체만든 api 주소 가져옴
my_url = "https://webhook-sitback.c9users.io" #"https://webhook-sitback.c9users.io/getWebhookData"에서 정보 안뺏기려고 텔레그램이랑 나 둘다 아는 getWebhookData는 비번으로해

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')




# 웹훅을 통해 정보가 들어올 route
@app.route("/{}".format(token), methods=['POST'])
def telegram():
    doc = request.get_json() #parsing 어구분석
    pp(doc)
    # 어떤 메세지가 들어오던 '닥쳐'라고 하는 챗봇
    
    chat_id = doc["message"]["chat"]["id"]
    msg = doc.get("message").get("text") #메세지 복제 // get("text") 접근하면 존재하지않으면 걍 넘어감 있으면 가져오고
     
    if msg == "로또":
        reply = str(random.sample(range(1, 45), 6))
        url = "{}/bot{}/sendMessage?chat_id={}&text={}".format(base_url, token, chat_id, reply)
        requests.get(url)
    
  # elif msg == "코스피" :

  # elif msg == "비트코인" :
    
    else:
        url = "{}/bot{}/sendMessage?chat_id={}&text={}".format(base_url, token, chat_id, msg)
        requests.get(url)
    



    
    
    chat_id = doc['message']['from']['id']
    img = False
    
    if doc.get('message').get('photo') is not None:
        img = True
    
    if img:
        file_id = doc.get('message').get('photo')[-1].get('file_id')
        file = requests.get("{}/bot{}/getFile?file_id={}".format(base_url, token, file_id))
        file_url = "{}/file/bot{}/{}".format(base_url, token, file.json().get('result').get('file_path'))
        
        # 네이버로 요청
        res = requests.get(file_url, stream=True)
        clova_res = requests.post('https://openapi.naver.com/v1/vision/celebrity',
            headers={
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            },
            files={
                'image':res.raw.read()
            })
        if clova_res.json().get('info').get('faceCount'):
            print(clova_res.json().get('faces'))
            msg = "{}".format(clova_res.json().get('faces')[0].get('celebrity').get('value'))
        else:
            msg = "인식된 사람이 없습니다."
    else:
    	# text 처리
    	text = doc['message']['text']
    
    requests.get('{}/bot{}/sendMessage?chat_id={}&text={}'.format(base_url, token, chat_id, msg))
    



    
    
    return '', 200 #텔레그램에 받았다고 200보내야해python
    
# 웹훅 설정 (set webhook) == 텔레그램에게 알리미를 해달라고 하는 것
@app.route('/setwebhook')
def setwebhook():
    url = "{}/bot{}/setWebhook?url={}/{}".format(base_url, token, my_url, token)
    res = requests.get(url)
    return '{}'.format(res), 200
# 텔레그램이 우리에게 알림을 줄 때 사용할 route
#   만약 특정 유저가 우리 봇으로 메세지를 보내게 되면,
#        텔레그램이 우리에게 알림을 보내온다.(json)