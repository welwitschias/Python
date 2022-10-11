import pandas as pd

# survey.csv 읽어서 위에서 5개만 출력
df = pd.read_csv('day03/survey.csv', encoding='utf-8')
print(df[:5])
print(df.head())

print('==============================')
print(df.mean())
print('수입의 평균 :', df.income.mean())
print('수입의 평균 반올림 :', round(df.income.mean(), 1))
print('수입의 합계 :', df.income.sum())
print('수입의 중앙값 :', df.income.median())

print('==============================')
print(df.describe())
print('-'*50)
print(df.income.describe())
print('-'*50)
print(df.sex.value_counts())
