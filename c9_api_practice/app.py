from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

url = "https://openapi.naver.com/v1/papago/n2mt" # PAPAGO API URL

naver_id = os.getenv('NAVER_ID') # 개발자센터에서 발급받은 Client ID 값
naver_secret = os.getenv('NAVER_SECRET') # 개발자센터에서 발급받은 Client Secret 값

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# data = {
#     'source': 'en',
#     'target': 'ko',
#     'text': 'case of Mondays'
# }

# res = requests.post(url, headers, data)


@app.route("/") # 주문받을/요청받을 서비스... / : home에 대해 정의
def index(): # 해당하는 주문/요청에 대한 결과
    return render_template('index.html')

@app.route("/show") # index에 날려준 단어를 받아 그대로 출력한다.
def show():
    keyword = request.args.get('keyword')
    
    data = {
    'source': 'en',
    'target': 'ko',
    'text': keyword
    }
    
    res = requests.post(url, headers=headers, data=data)
    
    # print(res.text)
    
    res_dict = res.json() # json parse해서 넘겨줌
    
    end_res = res_dict.get('message').get('result').get('translatedText')
    
    return render_template('show.html', keyword=end_res)