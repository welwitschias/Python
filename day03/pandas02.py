import pandas as pd

data = {
    'name': ['Mark', 'Jane', 'Chris', 'Paul'],
    'age': [32, 24, 19, 26],
    'score': [91.2, 88.5, 55.6, 88.9]
}
print(data)
print(type(data))

print('==============================')
df = pd.DataFrame(data)
print(df)
print(type(df))

print('==============================')
print(df.sum())
print(df.mean())

print('==============================')
print(df.age)
print(df['age'])

print('==============================')
data_dic = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [350, 400, 1050, 2000, 1000]
}
df2 = pd.DataFrame(data_dic)
print(df2)

print('==============================')
df3 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   index=['중간고사', '기말고사'],
                   columns=['1반', '2반', '3반'])
print(df3)

print('==============================')
df4 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   columns=['1반', '2반', '3반'])
df4.index = ['중간고사4', '기말고사4']
print(df4)

print('==============================')
df5 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]])
df5.index = ['중간고사5', '기말고사5']
df5.columns = ['1반', '2반', '3반']
print(df5)

print('==============================')
print(df3.sum())
print(df3.mean())
print(df3['1반'].sum())
print(df3['1반'].mean())

print('==============================')
df5.to_csv('day03/dataframe.csv', header='False', encoding='utf-8-sig')
df_read = pd.read_csv('day03/dataframe.csv', encoding='utf-8-sig')
print(df_read)
