# 문자열과 관련된 정규식 라이브러리
import re

text = "<title>지금은 문자열 연습입니다.</title>"

# 0~7사이 추출
print(text[0:7])

# '문' 있으면 위치값 출력
print(text.find('문'))
print(text.index('문'))

# '파' 있으면 위치값 출력, 없으면 -1 출력
print(text.find('파'))

# '파' 있으면 위치값 출력, 없으면 오류 발생
# print(text.index('파'))

print('==============================')
text1 = "     <title>지금은 문자열 연습입니다.</title>     "
text2 = ";"

# text1 공백 제거하고 text 연결
print(text1.strip() + text2)

# text1 왼쪽공백 제거하고 text 연결
print(text1.lstrip() + text2)

# text1 오른쪽공백 제거하고 text 연결
print(text1.rstrip() + text2)

# text1 <title>을 <div>로 바꾸기
print(text1.replace("<title>", "<div>"))

print('==============================')
text3 = ('111<head>안녕하세요</head>22')

text3Search = re.search('<head.*/head>', text3)
print(text3Search)

text3Group = text3Search.group()
print(text3Group)

# [0-9], [a-z]
# ab*c : abc, abbc, abbbc, abbbbc, ...
# *(0 이상), +(1 이상), ?(0 이상 1 이하)

print('==============================')
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')

text4Search = re.search('<title.*/title>', text4)
text4Group = text4Search.group()
print(text4Group)

text4Sub = re.sub('<.+?>', '', text4)
print(text4Sub)
