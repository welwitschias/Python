from bs4 import BeautifulSoup
import requests
import re

res1 = requests.get('https://news.daum.net/economic/')
soup1 = BeautifulSoup(res1.content, 'html.parser')

# 방법 1
links1 = soup1.select('a[href]')
# print(links)

for i in links1:
    # . : 임의의 문자 1개, \w : 숫자와 문자, + : 1회 이상
    if re.search('https://v.\w+', i['href']):
        print(i.get_text().strip())

print('==============================')
# 방법 2
links2 = soup1.find_all(href=re.compile(r'^https://v.\w+'))
# print(links2)

for i in links2:
    print(i.get_text().strip())

print('==============================')
res2 = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin')
soup2 = BeautifulSoup(res2.content, 'html.parser')

lotto_num = soup2.select(
    '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p .ball_645')
# lotto_num = soup2.find_all('span', class_="ball_645")
# print(lotto_num)

for i in lotto_num:
    print(i.get_text(), end='\t')
    # print(i.string)
