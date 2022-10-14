import usecsv
import re
import csv

ap = usecsv.opencsv('day03/apt_201910.csv')
apt = usecsv.switchcsv(ap)

# 3줄만 출력하기
print(apt[:3])

# 총 갯수 구하기
print(len(apt))

# 시군구, 단지명, 가격만 6줄 출력하기
for i in apt[:6]:
    print(i[0], i[4], i[8])

# 강원도, 120㎡이상, 3억 이하인 단지 검색 후 → 시군구, 단지명, 가격 출력하기
new_list = [['시군구', '단지명', '가격']]
for i in apt:
    try:
        if re.match('강원', i[0]) and i[5] >= 120 and i[8] <= 30000:
            new_list.append([i[0], i[4], i[8]])
    except:
        pass

print(new_list)

# 파일로 내보내기
# with open('day03/apt11.csv', 'w', newline='') as f:
#     a = csv.writer(f, delimiter=',')
#     a.writerows(new_list)

#
list = [['컴퓨터', '노트북', '태블릿'], [100, 80, 60]]
