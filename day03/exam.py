# animals list에서 새가 저장되어 있는 위치(index)만 저장하는 리스트
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']

# 방법1
bird_pos1 = []
for i in range(len(animals)):
    if animals[i] == '새':
        bird_pos1.append(i)
print('새의 위치1 :', bird_pos1)

print('==============================')
# 방법 2
bird_pos2 = []
for i, animal in enumerate(animals):
    if animal == '새':
        bird_pos2.append(i)
print('새의 위치2 :', bird_pos2)

print('==============================')
# myList에서 짝수만 출력
myList = [3, 5, 4, 9, 2, 8, 2, 1]

# 방법 1
new_list1 = []
for i in myList:
    if i % 2 == 0:
        new_list1.append(i)
print(new_list1)

print('==============================')
# 방법 2
# 리스트 함축 : for와 if를 결합 → [i for i in 리스트명 if 조건식]
new_list2 = [i for i in myList if (i % 2) == 0]
print(new_list2)

print('==============================')
# 19세 이상인 사람만 추출하여 adult list에 저장
people = [31, 53, 19, 15, 18, 21, 13]
adult = [i for i in people if i >= 19]
print(adult)

print('==============================')
# 항목이 2개인 것만 추출하여 twolist에 추가
lists = [[1, 2], [3, 4, 5], [6, 7]]
twolist = [i for i in lists if len(i) == 2]
print(twolist)
