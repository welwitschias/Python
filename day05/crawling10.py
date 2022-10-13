from bs4 import BeautifulSoup
import requests

codes = ['252670', '251340']

datas = []
for i in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+i
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # string 대신 get_text() 써도 됨
    title = soup.select_one(
        '#middle > div.h_company > div.wrap_company > h2 > a').string
    price = soup.select_one(
        '#chart_area > div.rate_info > div > p.no_today > em .blind').string
    datas.append([title, price])

print(datas)

print('==============================')
# 반복문 안쓴 노가다 버전(지양)
res1 = requests.get('https://finance.naver.com/item/main.naver?code=252670')
soup1 = BeautifulSoup(res1.content, 'html.parser')

title1 = soup1.select_one(
    '#middle > div.h_company > div.wrap_company > h2 > a').string
price1 = soup1.select_one(
    '#chart_area > div.rate_info > div > p.no_today > em .blind').string


res2 = requests.get('https://finance.naver.com/item/main.naver?code=251340')
soup2 = BeautifulSoup(res2.content, 'html.parser')

title2 = soup2.select_one(
    '#middle > div.h_company > div.wrap_company > h2 > a').string
price2 = soup2.select_one(
    '#chart_area > div.rate_info > div > p.no_today > em .blind').string

list = []
list.append([[title1, price1], [title2, price2]])
print(list)
