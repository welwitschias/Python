import numpy as np

a = np.array([[2, 3], [5, 2]])
print(a)
print(a.shape)

d = np.array([2, 3, 4, 5, 6])
print(d)
print(d.shape)

e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)
print(e.shape)
print(e.dtype)

print('==============================')
print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(np.arange(2, 10))  # 2이상 10미만의 원소로 구성된 1차원 배열

print('==============================')
a = np.ones((2, 3))
b = np.transpose(a)  # 행과 열이 바뀜
print(b)

print('==============================')
arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 13, 14], [26, 27, 28]])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

print('==============================')
d = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]])
print(d)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
d_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]]
print(d_list)
print(type(d_list))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# d_list[:2] = 0  # 오류 발생(범위지정해서 바꾸지 못함)
d_list[2] = 0
print(d_list)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
d[:2] = 0  # 오류 발생 안함(numpy는 범위지정해서 바꿀 수 있음)
print(d)

print(np.arange(10))
