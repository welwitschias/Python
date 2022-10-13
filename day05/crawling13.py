from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tbody = soup.select_one('tbody')

weatherList = []
for weather in tbody.select('tr'):
    tds = weather.select('td')
    if len(tds) > 0:
        location = tds[0].text
        temperature = tds[5].text
        humidity = tds[10].text
        weatherList.append([location, temperature, humidity])

# print(weatherList)

print('==============================')
# pandas로 변환 후 csv 내보내기
weather_df = pd.DataFrame(weatherList,
                          columns=('location', 'temperature', 'humidity'))
# print(weather_df)

weather_df.to_csv('day05/weather1.csv', mode='w',
                  encoding='euc-kr', index=True)

print('==============================')
# csv로 내보낸 후 pandas로 불러오기
with open('day05/weather2.csv', 'w', encoding='euc-kr') as file:
    file.write('location, temperature, humidity \n')
    for item in weatherList:
        row = ','.join(item)
        file.write(row+'\n')

df = pd.read_csv('day05/weather2.csv',
                 index_col='location', encoding='euc-kr')
print(df)
