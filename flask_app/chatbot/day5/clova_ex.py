from flask import Flask, request

import requests
import os
from pprint import pprint as pp

app = Flask(__name__)

my_url = "https://saramin-biniprc.c9users.io"
token = os.getenv('TELEGRAM_TOKEN')
naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')
api_url = "https://api.hphk.io/telegram"

@app.route("/{}".format(token), methods=['POST'])
def telegram():
    doc = request.get_json()
    pp(doc)
    chat_id = doc['message']['from']['id']
    img = False
    
    if doc.get('message').get('photo') is not None:
        img = True
    
    if img:
        file_id = doc.get('message').get('photo')[-1].get('file_id')
        file = requests.get("{}/bot{}/getFile?file_id={}".format(api_url, token, file_id))
        file_url = "{}/file/bot{}/{}".format(api_url, token, file.json().get('result').get('file_path'))
        
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
            text = "{}".format(clova_res.json().get('faces')[0].get('celebrity').get('value'))
        else:
            text = "인식된 사람이 없습니다."
    else:
    	# text 처리
    	text = doc['message']['text']
        
    requests.get('{}/bot{}/sendMessage?chat_id={}&text={}'.format(api_url, token, chat_id, text))
    return '', 200
    
@app.route('/set_webhook')
def set_webhook():
    res = requests.get('https://api.hphk.io/telegram/bot{}/setWebhook?url={}/{}'.format(token, my_url, token))
    print(res)
    return '{}'.format(res), 200

@app.route('/delete_webhook')
def delete_webhook():
    res = requests.get('https://api.hphk.io/telegram/bot{1}/deleteWebhook?url={2}/{3}'.format(token, my_url, token))
    print(res.text)
    return '{}'.format(res), 200