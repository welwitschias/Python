import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://www.youtube.com/c/paikscuisine/videos')
time.sleep(2)  # 2초간 프로세스를 중지(일시정지)

all_videos = driver.find_elements(By.ID, 'dismissible')

datas = []
for video in all_videos:
    title = video.find_element(By.ID, 'video-title').text
    playtime = video.find_element(
        By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer').text
    views = video.find_element(
        By.CSS_SELECTOR, 'span.ytd-grid-video-renderer').text

    print('제목 :', title)
    print('재생시간 :', playtime)
    print(views)
    print()

    datas.append([title, playtime, views])
