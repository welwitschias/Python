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
