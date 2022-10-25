from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import re
import matplotlib as mpl
import matplotlib.pyplot as plt

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = 'https://book.interpark.com/bookPark/html/book.html'
driver.get(url)
time.sleep(1)

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

book_df = pd.DataFrame(datas, columns=('title', 'price', 'score'))
book_df.to_csv('result.csv', mode='w',
               encoding='utf-8-sig', index=True)

bestseller_dict = {
    '12,000원 이상': 0,
    '13,000원 이상': 0,
    '14,000원 이상': 0,
    '15,000원 이상': 0,
    '16,000원 이상': 0
}

for item in datas:
    price = item[1]
    priceNew = float(re.sub(',', '', price))

    if priceNew >= 16000:
        bestseller_dict['16,000원 이상'] += 1
    elif priceNew >= 15000:
        bestseller_dict['15,000원 이상'] += 1
    elif priceNew >= 14000:
        bestseller_dict['14,000원 이상'] += 1
    elif priceNew >= 13000:
        bestseller_dict['13,000원 이상'] += 1
    elif priceNew >= 12000:
        bestseller_dict['12,000원 이상'] += 1

print(bestseller_dict)


font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(bestseller_dict.values(), labels=bestseller_dict.keys(), autopct='%.1f%%')
plt.show()