import pymysql

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True)

# 부산의 날씨
select_data_busan = "SELECT * FROM forecast WHERE city='부산' ORDER BY tmef DESC"
cur = conn.cursor()
cur.execute(select_data_busan)
result = cur.fetchall()

datas = []
for i in result:
    datas.append([i[2], i[4], i[5]])
print(datas)

# 부산의 최저기온, 최고기온
select_data_temp = "SELECT max(tmax), min(tmn) FROM forecast WHERE city='부산'"
cur.execute(select_data_temp)
result_temp = cur.fetchone()
print('최고기온 :', result_temp[0])
print('최저기온 :', result_temp[1])
