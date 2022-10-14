from bs4 import BeautifulSoup
import requests
import pandas as pd

# User-Agent : HTTP 요청을 보내는 디바이스/브라우저 등 사용자 소프트웨어의 식별 정보
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

url = 'https://www.melon.com/chart/week/index.htm'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')

tbody = soup.select_one('#frm > div > table > tbody')

chartList = []
for chart in tbody.select('tr'):
    tds = chart.select('td')
    if len(tds) > 0:
        ranking = tds[1].select_one('span.rank').text
        title = tds[5].select_one('div.ellipsis.rank01 > span > a').text
        singer = tds[5].select_one('div.ellipsis.rank02 > a').text
        album = tds[6].select_one('div.ellipsis.rank03 > a').text

        print(ranking, title, singer, album, sep=' | ')
        chartList.append([ranking, title, singer, album])

print('==============================')
chart_df = pd.DataFrame(chartList,
                        columns=('ranking', 'title', 'singer', 'album'))
print(chart_df)

chart_df.to_csv('day06/melonchart1.csv', mode='w',
                encoding='utf-8-sig', index=False)
