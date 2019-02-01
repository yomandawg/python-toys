# kospi라고 입력할 경우
# https://finance.naver.com/sise (scrap경로)
# 페이지의 kospi 값을 출력해주는 스크립트

import webbrowser
import requests
from bs4 import BeautifulSoup as BTS

res = requests.get("https://finance.naver.com/sise")
doc = BTS(res.text, 'html.parser')
kospi = doc.select_one('#KOSPI_now') # id표시 #
print("Current KOSPI index: " + kospi.text)