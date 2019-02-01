import webbrowser

# 자주 검색하는 키워드 리스트
url = "https://search.daum.net/search?q="
keyword = ["ssafy", "kospi", "bitcoin"]

for word in keyword:
    webbrowser.open(url+word)

print("hello, Ray")