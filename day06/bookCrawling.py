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

url = 'https://book.interpark.com/bookPark/html/book.html'
driver.get(url)
driver.implicitly_wait(1)

driver.find_element(
    By.XPATH, '//*[@id="header"]/div[3]/div/div[2]/ul/li[1]/a').click()
time.sleep(1)

bestSeller = driver.find_element(
    By.CSS_SELECTOR, 'div.rankBestContents > div > div.rankBestContentList > ol')
bestSellerList = bestSeller.find_elements(By.TAG_NAME, 'li')

datas = []
for book in bestSellerList:
    try:
        title = book.find_element(By.CLASS_NAME, 'itemName').find_element(
            By.TAG_NAME, 'strong').text
        price = book.find_element(By.CLASS_NAME, 'price').find_element(
            By.TAG_NAME, 'em').text
        score = book.find_element(By.CLASS_NAME, 'rateNumber').text

        print(title, price, score, sep=' | ')
        datas.append([title, price, score])
    except:
        continue

# print(datas)

book_df = pd.DataFrame(datas, columns=('title', 'price', 'score'))
book_df.to_csv('day06/bestseller.csv', mode='w',
               encoding='utf-8-sig', index=True)
