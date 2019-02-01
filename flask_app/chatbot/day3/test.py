import requests

import bs4
response = requests.get("https://www.bithumb.com/").text
doc = bs4.BeautifulSoup(response, 'html.parser')
result = doc.select('#tableAsset > tbody')
bit = doc.select_one('#assetRealBTC').text
print(bit)
    #return render_template('kospi.html', coin = result)
