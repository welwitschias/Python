from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://www.youtube.com/c/paikscuisine/videos')
time.sleep(2)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')

datas = []
for video in all_videos:
    title = video.find(id='video-title').text
    playtime = video.find(
        'span', class_="style-scope ytd-thumbnail-overlay-time-status-renderer").text.strip()
    views = video.find('span', {'class': 'ytd-grid-video-renderer'}).text

    datas.append([title, playtime, views])

# print('==============================')
youtube_df = pd.DataFrame(datas,
                          columns=('title', 'playtime', 'views'))
print(youtube_df)

print('==============================')
youtube_dict = {
    '100만 이상': 0,
    '50만 이상': 0,
    '10만 이상': 0
}

for item in datas:
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())
    if item >= 100:
        youtube_dict['100만 이상'] += 1
    elif item >= 50:
        youtube_dict['50만 이상'] += 1
    elif item >= 10:
        youtube_dict['10만 이상'] += 1

print(youtube_dict)

# 그래프 그리기
# 한글 지원 폰트 가져오기 + 설정하기
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)  # 111 : 1행 1열 1번째
axes.pie(youtube_dict.values(), labels=youtube_dict.keys(), autopct='%.1f%%')
plt.show()
