import pandas as pd
import numpy as np

# print(np.__version__)
arr = np.array([1, 2, 3, 4, 5, 6])
arr1 = arr.reshape(3, 2)
print(arr1)

arr2 = np.zeros((2, 3))
print(arr2)

arr3 = arr + 10
print(arr3)

arr4 = arr * 5
print(arr4)

print('==============================')
data1 = [10, 20, 30, 40, 50]
print(data1)
data2 = ['10!', '20!', '30!', '40!', '50!']
print(data2)

sr1 = pd.Series(data1)
print(sr1)
sr2 = pd.Series(data2)
print(sr2)

print('==============================')
data_dic = {
    'year': [2018, 2019, 2020],
    'sales': [350, 600, 700]
}
print(data_dic)

df1 = pd.DataFrame(data_dic)
print(df1)

print('==============================')
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [88.1, 90.4, 96.7]],
                   index=['중간고사', '기말고사'], columns=['국어', '영어', '수학'])
print(df2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df2.head())  # head default : 처음부터 5개
print(df2.head(1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df2.tail())  # tail default : 끝부터 5개
print(df2.tail(1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df2['국어'])
print(df2.영어)  # 비추천

print('==============================')
# 엑셀파일로 내보내기(내보낼 때 utf-8 사용 시 한글 깨짐)
# df2.to_csv('c:/python/score.csv', header='False', encoding='euc-kr')

# 엑셀파일 불러오기(내보낼 때의 encoding type이랑 동일해야 함)
df3 = pd.read_csv('c:/python/score.csv', encoding='utf-8')
print(df3)
