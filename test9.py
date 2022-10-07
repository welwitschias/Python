import csv
import re

f = open('popSeoul.csv', 'r')
reader = csv.reader(f)
# print(reader)  # 객체값이 출력됨

print('==============================')
# output = []
# for i in reader:
#     output.append(i)
# print(output)

print('==============================')
# 숫자구분 쉼표(,) 제거 → float 형태로 변환 / 문자는 그대로
output = []
for i in reader:
    tmp = []
    for j in i:
        try:
            if re.search('\d', j):
                tmp.append(float(re.sub(',', '', j)))
            else:
                tmp.append(j)
        except:
            pass
    output.append(tmp)
print(output)

print('==============================')
# '구', '한국인', '외국인', '외국인 비율'로 나타내기
ko_fo = [['구', '한국인', '외국인', '외국인 비율']]
for i in output:
    try:
        foreignerRatio = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreignerRatio > 5:
            ko_fo.append([i[0], i[1], i[2], foreignerRatio])  # list로 받아주어야 하므로 []추가
    except:
        pass
print(ko_fo)
print(len(ko_fo))
