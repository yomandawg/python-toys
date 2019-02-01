from flask import Flask, render_template, request
# jinja template 사용하기 위해 render_template 가져옴
import requests
# requests: 우리 대신 요청을 보내는 것
from bs4 import BeautifulSoup as BTS
# bs4: beuatiful soup - html text등 일반적인 글자들을 검색하기 좋게(parsing) 예쁘게 처리함

app = Flask(__name__, template_folder="views")
# Flask()의 instance 만들기, __name__ 써야 지정 명령어 사용 가능
# template_folder="views", views folder 경로설정 없이는 사용 못함
# 없으면 => jinja2.exceptions.TemplateNotFound: index.html

@app.route('/')
def index():
    return render_template('index.html') 
    # c9은 jinja라는 template 사용
    # return "<h1>OP.GG</h1>" # Browser이 html 인식함 / 해도 되지만 temlplate 사용 못함
    
@app.route('/search')
def search():
    # python은 정보 받아서 request라는 객체에 저장해둠
    # full_path: /search?userName=%EC%A1%B0%EC%A7%80+%EB%B2%84%ED%81%B4%EB%A6%AC
    # 전송된 모든 정보 볼 수 있다(encoded)

    # remote_addr: 요청한 사람의 IP볼 수 있다

    # url: 전체 url이 다나온다.. 모든정보

    # headers: 모든 헤더 출력
    
    # request.args['userName']
    # request.args.get('userName')
    # args: 파라미터 값 보기 in dictionary
    
    userInput = request.args.get('userName')
    
    # op.gg에 있는 데이터를 검색해서 - op.gg에 요청을 보내서, op.gg로부터 받은 html파일 중,
    # 승, 패 정보만 가져온다
    
    url = "http://www.op.gg/summoner/userName="
    
    response = requests.get(url + userInput)
    # 요청을 보내서 받아온 응답이 response에 들어있을 것
    # response [200]: 요청 보내서 받아옴
    
    # print(response)
    # print(response.text)
    # #response.text: 받아온 모든 데이터 출력
    
    doc = BTS(response.text, features="html5lib")
    # beautifulsoup parsing
    
    wins = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    loses = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")
    # select_one: 하나의 element를 가져오기
    # 페이지소스에서 따온 데이터 string
    # wins.text: element에서 text만 추출
    
    return render_template('search.html', userInput=userInput, wins=wins.text[:-1], loses=loses.text[:-1])
    # index에서 데이터를 받아서 search로 넘겨주기