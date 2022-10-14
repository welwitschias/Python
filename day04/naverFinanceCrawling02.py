from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

table = soup.select_one(
    '#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
chart = table.select('tr')

datas = []
for i in chart:
    name = i.select_one('th > a').get_text()
    price = i.select_one('td').get_text()
    updown = i.select_one('td > img')['alt']
    variance = i.select_one('span').get_text().strip()
    datas.append([name, price, updown, variance])

print(datas)

print('==============================')
# 엑셀로 결과 내보내기
write_workbook = Workbook()
write_worksheet = write_workbook.create_sheet('결과')

for i in datas:
    write_worksheet.append(i)

write_workbook.save(r'day04/finance.xlsx')
