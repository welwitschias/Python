from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# 경로 : F12 → 원하는 곳 우클릭 → Copy → Copy selector
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)
