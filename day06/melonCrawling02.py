from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://www.melon.com/chart/week/index.htm')
driver.implicitly_wait(2)  # 2초간 프로세스를 중지(일시정지)

tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

chartList = []
for chart in trs:
    ranking = chart.find_element(By.CLASS_NAME, 'rank').text
    title = chart.find_element(
        By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME, 'a').text
    singer = chart.find_element(
        By.CLASS_NAME, 'rank02').find_element(By.TAG_NAME, 'a').text
    album = chart.find_element(
        By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME, 'a').text
    like = chart.find_element(By.CLASS_NAME, 'like').find_element(
        By.CLASS_NAME, 'cnt').text

    # like = re.sub(',', '', like)  # 좋아요 쉼표 제거
    print(ranking, title, singer, album, like, sep=' | ')
    chartList.append([ranking, title, singer, album, like])

print('==============================')
chart_df = pd.DataFrame(chartList,
                        columns=('ranking', 'title', 'singer', 'album', 'like'))
print(chart_df)

chart_df.to_csv('day06/melonchart2.csv', mode='w',
                encoding='utf-8-sig', index=False)
