from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# 경로 : F12 → 원하는 곳 우클릭 → Copy → Copy selector
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)

print('==============================')
dollarValue = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value')
print('dollarValue :', dollarValue.string)

print('==============================')
txt1 = soup.select_one('div.head_info')
print(txt1)
print('-'*50)
print(txt1.select('span')[0].string)
print(txt1.select('span')[1].string)
print(txt1.select('span')[2].string)
print(txt1.select('span')[3].string)
print(txt1.select('span')[4].string)

print('==============================')
txt2 = txt.select('span')  # list형
print(txt2)
print('-'*50)
for i in txt2:
    print(i.string)

print('==============================')
# 가격
price = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value').string
print(price)

print('==============================')
# 상승/하락
updown = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.blind').string
print(updown)
