n = 3
m = 4
arr = [0]*n
for i in range(n):
    arr[i] = [0]*m
print(r'array is ', arr)


n = int(input())
arr = list()
#input array
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
#output array
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()


arr = [[1, 2, 3, 4], [5, 4, 3, 1], [2, 4, 8, 5], [3, 5, 8, 1]]
#Вывод при помощи цикла for и метода join
print('Arrray is ')
for i in arr:
  print(' '.join(list(map(str, i))))
#Пример 1. Подсчет суммы всех элементов
s = 0
for i in range(len(arr)):
  for j in range(len(arr[i])):
    s += arr[i][j]
print('Ex. 1, sum is ', s)
#Пример 2. Подсчет суммы всех элементов
s = 0
for row in arr:
  for element in row:
    s += element
print('Ex. 2, sum is ', s)


from random import *
#Пример формирования рандомной матрицы
# n = 5
# arr = list()
# for i in range(n):
#   row = list()
#   for j in range(n):
#     row.append(float(round(randint(0, 100) + random(), 2)))
#   arr.append(row)
n = 3
arr = [[1, 3, 0], [3, 2, 6], [0, 6, 5]]
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
couple_count = (len(arr) ** 2 - len(arr)) / 2
count_validate = 0
for i in range(len(arr)):
  for j in range(i + 1, len(arr[i])):
    if arr[i][j] == arr[j][i]:
      count_validate += 1
print(couple_count)
print(count_validate)

if couple_count == count_validate:
  print('Symmentic')
else:
  print('Asymmetric')