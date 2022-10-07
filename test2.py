# 조건문
a = 2
if (a == 1):
    print(1)
else:
    print(2)

if (a == 1):
    print(1)
elif (a == 2):
    print(2)
else:
    print(3)

x = 3
y = 2
print(x == y)
print(x != y)

money = 1300
if (money >= 1200 and money < 3500):
    print("버스 탑승 가능")

print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2, 3])
print('i' not in 'python')

if (money < 1000):
    pass
else:
    print('지금!!!')


print('==============================')
# for 반복문
for i in [1, 2, 3]:
    print(i)

for i in (1, 2, 3):
    print(i)

for i in 'Hello':
    print(i, end=' ')
print()

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i + '!')
    # print(i, end='! ')

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d 학생은 합격입니다." % number)
    else:
        print("%d 학생은 불합격입니다." % number)

print('==============================')
# while 반복문
num = 5
while (num > 0):
    print(num)
    num -= 1

num = 10
while (num > 0):
    if (num == 6):
        print('---end---')
        break
    print(num, end=' ')
    num -= 1

print('==============================')
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()

print('==============================')
# 1~100 중에서 7의 배수의 합계 계산하기
sum = 0
for i in range(101):
    if(i != 0 | i % 7 == 0):
        sum += i
        print(i, end=' ')
print('\nsum :', sum)

print('==============================')
for i in range(3):
    for j in range(3):
        print('*', end=' ')
    print()

print('==============================')
i = 0
while i < 5:
    i += 1
    print('*' * i)
