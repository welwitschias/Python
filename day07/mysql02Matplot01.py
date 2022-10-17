import pymysql
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True)

# 폰트 설정
font_path = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 꺾은선 그래프 그리기
select_data_seoul = "SELECT * FROM forecast WHERE city='서울' ORDER BY tmef"
cur = conn.cursor()
cur.execute(select_data_seoul)
result = cur.fetchall()

highTemp = []
lowTemp = []
weatherState = []
xdata = []

for i in result:
    highTemp.append(float(i[5]))
    lowTemp.append(float(i[4]))
    weatherState.append(i[3])
    xdata.append(i[2].split('-')[2])

plt.figure(figsize=(10, 6))  # 크기
plt.plot(xdata, lowTemp, label='최저기온')
plt.plot(xdata, highTemp, label='최고기온')
plt.title(result[0][2].split('-')[1]+'월')
plt.legend()
plt.show()

# 막대 그래프 그리기
select_data_wf = "SELECT wf, count(*) FROM forecast WHERE city='서울' GROUP BY wf"
cur.execute(select_data_wf)
result_wf = cur.fetchall()

wfData = []
wfDataCount = []

for i in result_wf:
    wfData.append(i[0])
    wfDataCount.append(i[1])

plt.bar(wfData, wfDataCount)
plt.show()

# 원형 그래프 그리기
plt.pie(wfDataCount, labels=wfData, autopct='%.1f%%')
plt.show()
