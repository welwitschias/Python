from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# url에 접속(import urllib.request)한 후 읽기
res = req.urlopen(url)
print(res)

soup = BeautifulSoup(res, 'html.parser')
# print(soup)

print('==============================')
# 기상청 육상 중기예보 title만 출력하기
title1 = soup.channel.title.string
print(title1)

title2 = soup.find('title').string
print(title2)
print('-'*50)

# wf태그 내용 출력하기
wf = soup.find('wf').string
print(wf)
