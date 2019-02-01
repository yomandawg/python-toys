"""
https://edu.ssafy.com에 로그인 하여,
출첵을 하는 스크립트
"""

# edu.ssafy.com 로그인 패턴 분석
# 1. form (name="loginForm")
#   - POST 방식으로 이루어짐
#   - "action" = ???
# 2. input
#   - ID가 들어가는 input : userId
#   - PW가 들어가는 input : userPwd
# 3. LOGIN 버튼
#   - fnLogin() 실행하는 JS 이벤트가 작동됨
#   - 하하 개발자님 죄송죄송 : ajax ->
#   - URL_LOGIN

import requests
#import os
from bs4 import BeautifulSoup as BTS

url = "https://edu.ssafy.com/comm/login/SecurityLoginCheck.do"
index_url = "https://edu.ssafy.com/edu/main/index.do"

checkin_url = "https://edu.ssafy.com/edu/mycampus/attendance/attendanceCheckIn.do"


data = {
    # 'userId': os.getenv('MYID'),
    # 'userPwd': os.getenv('MYPWD')
    'userId': 'myId',
    'userPwd': 'myPwd'
}

with requests.Session() as session:
    res = session.post(url, data=data) # cookie 관리
    print(res.status_code) # 200 나오면 login 된거

    checkin_res = session.get(checkin_url)
    print(checkin_res.status_code) # 입실하기

    index_res = session.get(index_url)
    doc = BTS(index_res.text, 'html.parser')
    day = doc.select_one("#wrap > div.container.main-container > div.content > section.main-page.sec1 > div > div.col-md.n1 > div > div.today > p.day")
    #copy selector
    print(day.text) # 날짜 출력