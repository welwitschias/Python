import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('day05/weather2.csv',
                 index_col='location', encoding='utf-8-sig')
# print(df)

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
print(city_df)

# 그래프 그리기
# 한글 지원 폰트 가져오기 + 설정하기
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# kind : 그래프 종류, figsize : 차트 크기, legend : 범례
ax = city_df.plot(kind='bar', title='날씨',
                  figsize=(12, 7), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)
plt.show()
