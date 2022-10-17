import pymysql
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)

# 폰트 설정
font_path = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# [dataframe 이용] 꺾은선 그래프 그리기
select_data_seoul = "SELECT * FROM forecast WHERE city='서울' ORDER BY tmef"
cur = conn.cursor()
cur.execute(select_data_seoul)
result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

plt.figure(figsize=(10, 6))
plt.plot(pd.to_numeric((df['tmn'])), label='최저기온')
plt.plot(pd.to_numeric((df['tmax'])), label='최고기온')
plt.legend()
plt.show()
