# 함수
def seperate():
    a = int(input('수 입력 : '))
    if (a % 2 == 0):
        print('짝수')
    else:
        print('홀수')


def addResult(a, b):
    return a + b


# seperate()
print(addResult(3, 5))

ret = addResult(10, 20)
print(ret)

print('==============================')
# 1~10까지의 합 출력하기


def sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


print(sum(10))

print('==============================')
# 연습문제
nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]


def max_count(list):
    counts = {}
    for i in list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


counts = max_count(nums)
print(counts)
print(counts.values())

print('==============================')
# values의 최대값 구하기 1
print(max(counts.values()))

# values의 최대값 구하기 2
first = []
maxValue = max(counts.values())
for (name, count) in counts.items():
    print(name, " : ", count)
    if (count == maxValue):
        first.append(count)
print('first :', first)
