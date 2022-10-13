from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path = 'C:\\python\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)  # 창 꺼짐 방지
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://www.naver.com')
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
# driver.find_element_by_id('search_btn').click()  # 3버전(이전 버전) 명령어

# 창 꺼짐 방지(강제적)
# while(True):
#     pass
