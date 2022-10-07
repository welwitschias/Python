import codecs
import re

# 같은 폴더내라서 파일명만 작성(아닐경우 경로까지 작성), 읽기모드(r)
f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
print(script101[:100])

print('==============================')
# r''(이스케이프 문자(\) 생략 가능)
lines = re.findall(r'Monica:.+', script101)
print(lines[:3])
print(type(lines))

print('==============================')
all = re.findall(r'All:.+', script101)
print(all)

print('==============================')
# all에서 마지막만 출력
print(all[-1])

# all(list형) 길이(개수) 구하기
print(len(all))

print('==============================')
# 첫글자는 대문자 + 소문자 + ':' 으로 시작하는 문자열 찾기
char = re.compile(r'[A-Z][a-z]+:')
names = re.findall(char, script101)

# 중복 허용
print(names)
print(len(names))

print('==============================')
# 중복 제거
print(set(names))
print(len(set(names)))

setType = set(names)
print(type(setType))

print('==============================')
# 이름이 7글자 이상인 사람
for i in setType:
    if len(i) > 7:
        print(i)

# type 변환
character = list(setType)
print(type(character))
print(character)

print('==============================')
# ':' 제거
character_list = []
for i in character:
    character_list += [i[:-1]]
print(character_list)

character_list2 = []
for i in character:
    character_list2 = re.sub(':', '', i)
    print(character_list2, end=' ')
print()

character_list3 = []
for i in character:
    character_list3.append(re.sub(':', '', i))
print(character_list3)

print('==============================')
text = '제 이메일 주소는 great@naver.com'
text += '오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(text)

# 메일주소만 추출하기(패턴 : 영문자 @ 영문자 .)
mail = re.compile(r'[a-z]+@[a-z.]+')
address = re.findall(mail, text)
print(address)

print('==============================')
# 첫글자를 모두 a로 바꾸기(패턴 : a 영문자)
words = ['apple', 'cat', 'brave', 'drama', 'aside', 'blow', 'coat', 'above']

# 1
words_list = []
for i in words:
    words_list += re.findall(r'a[a-z]+', i)
print(words_list)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 2 : search는 찾고자 하는 단어가 중간에 있어도 찾음
for i in words:
    m1 = re.search(r'a[a-z]+', i)
    if m1:
        print(m1.group())

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 3 : match는 찾고자 하는 단어가 처음에 있어야 찾음
for i in words:
    # m2 = re.match(r'a[a-z]+', i)
    m2 = re.match(r'a\D+', i)  # \d(숫자), \D(숫자가 아님)
    if m2:
        print(m2.group())

print('==============================')
exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년입니다.'
print(re.findall(r'\d.+년', exam1))  # 91년 ~ 2022년 사이 추출
print(re.findall(r'\d.+?년', exam1))  # 91년, 97년, 2022년만 추출
print(re.findall(r'\d+.년', exam1))  # 91년, 97년, 2022년만 추출
print(re.findall(r'\d+년', exam1))  # 91년, 97년, 2022년만 추출
