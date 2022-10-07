print('Hello')

print('==============================')
a = 0
print(a)
print(type(a))

b = 'Hello World'
print(b)
print(type(b))

print('==============================')
c = "'안녕하세요'"
print(c)

d = "\'안녕하세요\'"
print(d)

print(b+d)
print(2*3)

# 문자 반복
print('2'*3)
print(c*3)

print('==============================')
# b[1] = 'C' # 오류 발생(문자열은 정적이므로)
print(b)
print(b[0])

# -는 문자열 끝에서부터 시작
print(b[-1])
print(b[-2])

print('==============================')
e = '반갑습니다'
print(e)
print(e[0:2])
print(e[1:3])
print(e[:])

# 2씩 증가
print(e[0:5:2])

# 위치값 반환
print(e.find('반'))
print(e.find('니'))
print(e.find('안'))  # 없으면 -1 리턴

print(e.index('반'))
print(e.index('니'))
# print(e.index('안')) # 없으면 오류 발생

print('==============================')
aa = 'Now is aa bb cc'
print(aa.split())

print('==============================')
bb = ','
print(bb.join('ABCD'))
print(bb)
print(b.upper())
print(b.lower())
print(b)

print('==============================')
cc = '                 py                 '
print(cc.lstrip())
print(cc.rstrip())
print(cc.strip())

print('==============================')
# list : [], 수정 가능
l = list()
print(l, type(l))

l1 = [1, 2, 3]
print(l1, type(l1))

listTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(listTest, type(listTest))
print(listTest[0])

# 길이 구하기
print(len(listTest))

# 마지막 값 출력하기
print(listTest[-1])
print(listTest[len(listTest)-1])

# 리스트 내용 바꾸기
listTest[0] = 99
print(listTest[0])

listTest[1] = [1, 2, 3]
print(listTest)
print(len(listTest))

listTest[2] = '문자'
print(listTest)

# 맨 마지막에 추가
listTest.append(999)
print(listTest)

listTest.remove(5)
print(listTest)

print('==============================')
a1 = [1, 2, 3]
b1 = ['life', 'is', 'too', 'short']
c1 = [1, 2, 'life', 'is']
d1 = [1, 2, [3, 4], ['life', 'is']]

print(d1[0])
print(d1[3])
print(d1[3][1])
print(d1[0:3])

# 특정 위치에 추가(append는 맨 마지막에 추가)
d1.insert(2, 'aa')
print(d1)

# 맨 마지막을 제거
d1.pop()
print(d1)

# 찾고자 하는 문자수 반환
a2 = [2, 1, 0, 2, 3, 2, 4, 2]
print(a2.count(2))

print('==============================')
# tuple : (), 수정 불가
t = tuple()
print(t, type(t))

t1 = (1, 2, 3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1 + t1)
# t[0] = 5 # 오류 발생

t4 = (1, 2, (3, 4), ('life', 'is'))
print(t4)

print('==============================')
# dictionary : {}, java의 map과 유사
d = dict()
print(d, type(d))

d1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(d1, type(d1))

print(d1['a'])
# print(d1['d']) # 오류 발생(d라는 key값이 없으므로)

d1['c'] = 33
print(d1)

print("keys() : ", d1.keys())
print("values() : ", d1.values())
print("items() : ", d1.items())

print("type keys() : ", type(d1.keys()))
print("type values() : ", type(d1.values()))
print("type items() : ", type(d1.items()))

# list형으로 변환
print("type list", type(list(d1.keys())))

print('==============================')
dict = {
    'name': 'Hong',
    'phone': '01011112222',
    'birth': '0814'
}
print(dict)

# 추가하기
dict[1] = 'a'
dict['pet'] = 'dog'
print(dict)
print(dict['pet'])

print(dict.keys())
print(list(dict.keys()))

# 삭제하기
del dict[1]
print(dict)

# 전체 삭제하기
dict.clear()
print(dict)

print('==============================')
# set : {}, 중복 불가
s1 = {1, 2, 3, 4, 4, 4, 4}
print(s1, type(s1))

s2 = set([1, 2, 3, 4, 5])
print(s2, type(s2))

# 교집합
print(s1 & s2)

# 합집합
print(s1 | s2)

# 차집합
print(s1 - s2)
print(s2 - s1)

print(s2.difference(s1))
