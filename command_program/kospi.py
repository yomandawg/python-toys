import webbrowser
import requests
from bs4 import BeautifulSoup as BTS

res = requests.get("https://finance.naver.com/sise")
doc = BTS(res.text, 'html.parser')
kospi = doc.select_one('#KOSPI_now') # id표시 #
print("Current KOSPI index: " + kospi.text)
