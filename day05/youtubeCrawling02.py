from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://www.youtube.com/c/paikscuisine/videos')
time.sleep(2)

# 소스코드 불러오기
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')

datas = []
for video in all_videos:
    title = video.find(id='video-title').text
    playtime = video.find(
        'span', class_="style-scope ytd-thumbnail-overlay-time-status-renderer").text.strip()
    views = video.find('span', {'class': 'ytd-grid-video-renderer'}).text
    
    # 조회수에서 숫자만 추출하기 방법 1
    numcut = re.compile('\d*\.?\d+')
    viewsNumcut = numcut.findall(views)

    for viewsNum in viewsNumcut:
        viewsNum = float(viewsNum)

    print('제목 :', title)
    print('재생시간 :', playtime)
    print(views)
    print()

    datas.append([title, playtime, viewsNum])

# print('==============================')
youtube_df = pd.DataFrame(datas,
                          columns=('title', 'playtime', 'views'))
print(youtube_df)

# utf-8-sig : 한글 안깨짐
youtube_df.to_csv('day05/youtube1.csv', mode='w',
                  encoding='utf-8-sig', index=False)

print('==============================')
youtube_dict = {
    '100만 이상': 0,
    '50만 이상': 0,
    '10만 이상': 0
}

for i in datas:
    count = i[-1]
    if count >= 100:
        youtube_dict['100만 이상'] += 1
    elif count >= 50:
        youtube_dict['50만 이상'] += 1
    elif count >= 10:
        youtube_dict['10만 이상'] += 1

print(youtube_dict)
