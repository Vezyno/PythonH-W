import random

# Задача №1
array = [[1, 2, 3],
         [10, 9, 6],
         [7, 8, 9]]
max_column3 = []
max_row2 = []
for y in range(len(array)):
    if y == 1:
        max_row2 = array[y]
    for x in range(len(array[y])):
        if x == 2:
            max_column3.append(array[y][x])
print("Максимальное значение в третьем столбце:", max(max_column3))
print("Максимальное значение во второй строке:", max(max_row2))


# Задача №2
m, n = 3, 4  
original_array = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(-10, 10))  
    original_array.append(row)
new_array = []
for row in original_array:
    new_row = []
    for element in row:
        if element > 0:
            new_row.append(1)  
        else:
            new_row.append(0)  
    new_array.append(new_row)
print("Исходный массив:")
for row in original_array:
    print(row)
print("\nНовый массив:")
for row in new_array:
    print(row)


# Задача №3
n = 3  
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
magic_sum = sum(matrix[0])
is_magic = True
# Проверяем суммы строк
for i in range(n):
    if sum(matrix[i]) != magic_sum:
        is_magic = False
        break
# Проверяем суммы столбцов
if is_magic:
    for j in range(n):
        column_sum = 0
        for i in range(n):
            column_sum += matrix[i][j]
        if column_sum != magic_sum:
            is_magic = False
            break
if is_magic:
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")


# Задача №4
n = 3 
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
is_symmetric = True
# Проверяем симметричность матрицы
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break
if is_symmetric:
    print("Матрица является симметричной.")
else:
    print("Матрица не является симметричной.")


# Задача №5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
max_row_index = 0
min_row_index = 0
max_row = sum(matrix[0])
min_row = sum(matrix[0])
for i in range(len(matrix)):
    current_sum = sum(matrix[i])  
    if current_sum > max_row:
        max_row = current_sum
        max_row_index = i
    if current_sum < min_row:
        min_row = current_sum
        min_row_index = i
print("Строка с наибольшей суммой:")
print(matrix[max_row_index], "Сумма:", max_row)
print("Строка с наименьшей суммой:")
print(matrix[min_row_index], "Сумма:", min_row)


# Задача №6
matrix = [
    [3.5, 2, 5.6],
    [7.2, 1.4, 8.9],
    [0.5, 4.3, 6.8],
    [9.1, 3.3, 2.2]
]
n = len(matrix)
m = len(matrix[0])
new_matrix = [[0] * m for _ in range(n)]
for i in range(n):
    min_index = 0
    for j in range(1, m):
        if matrix[i][j] == matrix[i][min_index]:
            min_index = j
    
    if matrix[i][min_index] % 2 == 0:
        new_matrix[i][min_index] = 0  
    else:
        new_matrix[i][min_index] = 1 

    # Копируем остальные элементы из исходной матрицы
    for j in range(m):
        if j != min_index:
            new_matrix[i][j] = matrix[i][j]
for row in new_matrix:
    print(row)