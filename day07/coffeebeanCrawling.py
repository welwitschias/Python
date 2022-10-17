from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def coffeeBeanStore(datas):
    path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    coffeeBeanURL = 'https://www.coffeebeankorea.com/store/store.asp'

    datas = []
    for i in range(1, 370):  # 매장 수만큼 반복
        driver.get(coffeeBeanURL)
        time.sleep(1)

        try:
            driver.execute_script('storePop2(%d)' % i)
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            storeName = soup.select('div.store_txt > h2')[0].string

            print(storeName)
            datas.append(storeName)
        except:
            continue


result = []
coffeeBeanStore(result)
