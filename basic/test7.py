# w : write
f1 = open('basic/new.txt', 'w')
print(f1)
f1.close()

f2 = open('basic/test.txt', 'w')
for i in range(1, 6):
    data = '%d번째 줄입니다. \n' % i
    f2.write(data)
f2.close()

# a : append
f3 = open('basic/test.txt', 'a')
for i in range(6, 11):
    data = '%d번째 줄입니다. \n' % i
    f3.write(data)
f3.close()

# r : read
# 1줄 읽기
f4 = open('basic/test.txt', 'r')
line = f4.readline()
print(line)

while True:
    line = f4.readline()
    if not line:
        break
    print(line)
f4.close()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 여러줄 읽기
f5 = open('basic/test.txt', 'r')
lines = f5.readlines()
print(lines)
f5.close()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
f6 = open('basic/test.txt', 'r')
data = f6.read()
print(data)
f6.close()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# with open : close() 포함
with open('basic/test.txt', 'w') as f:
    f.write('aa bb cc')
# data = f.read()  # f.close() 상태여서 오류 발생
