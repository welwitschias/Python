import pymysql
import requests
from bs4 import BeautifulSoup

# connect() : db 연결
# cursor() : db 전달을 위한 객체 생성
# execute() : 질의문 전달
# commit() : 실행
# fetchone(), fetchall() : select한 결과를 가져옴

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True)

insert_weather = "INSERT INTO forecast(city, tmef, wf, tmn, tmax) VALUES (%s, %s, %s, %s, %s)"

# 중복 데이터 삽입 방지
select_data = "SELECT tmef FROM forecast ORDER BY tmef DESC limit 1"
cur = conn.cursor()
cur.execute(select_data)
last_date = cur.fetchone()  # db에 있는 최신 날짜
# print(type(last_date))
# print(last_date)

req = requests.get(
    'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text
soup = BeautifulSoup(html, 'lxml')

weather = {}
for i in soup.find_all('location'):
    weather[i.find('city').text] = []

    for j in i.find_all('data'):
        tmp = []
        if(last_date is None) or (str(last_date[0]) < j.find('tmef').text):
            tmp.append(j.find('tmef').text)
            tmp.append(j.find('wf').text)
            tmp.append(j.find('tmn').text)
            tmp.append(j.find('tmx').text)
            weather[i.find('city').string].append(tmp)

for i in weather:
    for j in weather[i]:
        cur = conn.cursor()
        cur.execute(insert_weather, (i, j[0], j[1], j[2], j[3]))
        conn.commit()
