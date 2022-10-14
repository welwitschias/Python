from bs4 import BeautifulSoup
import re
import requests
import urllib.request as req

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""

soup = BeautifulSoup(html, 'html.parser')

# https로 시작하는 것 출력
lis1 = soup.find_all(href=re.compile(r'https://'))  # https:// 갖고 있는 것 모두 출력
lis2 = soup.find_all(href=re.compile(r'^https://'))  # https:// 로 시작하는 것 출력
print(lis1)
print(lis2)

for i in lis2:
    print(i.attrs['href'])  # href 속성값만 출력

print('==============================')
r = requests.get("http://api.aoikujira.com/time/get.php")

# text 형식으로 데이터 추출
txt = r.text
print(txt)

# binary 형식으로 데이터 추출
bin = r.content
print(bin)

print('==============================')
# 방법1
url1 = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
res1 = req.urlopen(url1)
movieurl1 = BeautifulSoup(res1, 'html.parser')

rank1 = movieurl1.select('#old_content > table > tbody > tr .tit3 a')

num = 0
for i in rank1:
    num += 1
    print(num, ":", i.string)

print('==============================')
# 방법2-1
url2 = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
res2 = url2.text
movieurl2 = BeautifulSoup(res2, 'html.parser')

rank2 = movieurl2.find_all('div', class_="tit3")
print(type(rank2))

# 제목만 표시
for i in rank2:
    print(i.get_text().strip())
print('-'*50)

# 제목과 순위까지 표시
for i in range(len(rank2)):
    print((i+1), '위 :', rank2[i].get_text().strip())

print('==============================')
# 방법2-2
rank3 = movieurl2.select('div.tit3')
print(type(rank3))

# 제목만 표시
for i in rank3:
    print(i.get_text().strip())
print('-'*50)

# 제목과 순위까지 표시
for i in range(len(rank3)):
    print((i+1), '위 :', rank2[i].get_text().strip())
