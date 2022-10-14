from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = 'http://tour.interpark.com/?mbn=tour&mln=tour'
driver.get(url)
driver.implicitly_wait(1)

# 장소 입력하기
driver.find_element(By.ID, 'SearchGNBText').send_keys('제주도')  # 방법 1
# search = input('검색어를 입력해주세요.')
# driver.find_element(By.ID, 'SearchGNBText').send_keys(search)  # 방법 2(input 사용)

# 찾기 클릭하기
driver.find_element(By.CLASS_NAME, 'search-btn').click()  # 방법 1(속도 느림)
# driver.execute_script('searchBarModule.ClickForSearch()')  # 방법 2(자바스크립트 함수로 실행, 속도 빠름)
time.sleep(1)

# 국내숙박 클릭하기
driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/ul/li[2]').click()
time.sleep(1)

pageNum = driver.find_elements(By.CSS_SELECTOR, 'div.pageNumBox > ul > li')

datas = []
for item in range(1, len(pageNum)+1):
    hotelList = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')

    for hotel in hotelList:
        try:
            name = hotel.find_element(By.CLASS_NAME, 'infoTitle').text
            price = hotel.find_element(By.CLASS_NAME, 'final').find_element(
                By.TAG_NAME, 'strong').text
            score = hotel.find_element(
                By.CSS_SELECTOR, 'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]

            print(name, price, score, sep=' | ')
            datas.append([name, price, score])
        except:
            print(item)
            continue

    if item == len(pageNum):
        break

    pageNum[item].click()
    time.sleep(1)

# print(datas)

hotel_df = pd.DataFrame(datas, columns=('name', 'price', 'score'))
hotel_df.to_csv('day06/hotel.csv', mode='w', encoding='utf-8-sig', index=True)
