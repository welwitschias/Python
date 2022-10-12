from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# li > b > a 일 경우
# 후손 li a → li 하위 a 접근
# 자식 li > b → li 바로 아래 b에 접근
a_list = soup.select('#mw-content-text > div.mw-parser-output > ul > li a')

for i in a_list:
    name = i.string
    print('-', name)
