# Задача №1
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
is_symmetric = False
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
        else:
            is_symmetric = True
if is_symmetric:
    print("Матрица симметрична.")
else:
    print("Матрица не симметрична.")


# Задача №2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, -1, 1]
]
max_sum = 0
min_sum = 0
max_row = []
min_row = []
for row in matrix:
    current_sum = sum(row)
    if current_sum > max_sum:
        max_sum = current_sum
        max_row = row
    if current_sum < min_sum:
        min_sum = current_sum
        min_row = row
print("Строка с наибольшей суммой:", max_row)
print("Сумма элементов строки с наибольшей суммой:", max_sum)
print("Строка с наименьшей суммой:", min_row)
print("Сумма элементов строки с наименьшей суммой:", min_sum)


# Задача №3
matrix = [
    [3, 2, 1],
    [8, 5, 6],
    [13, 8, 11]
]
new_matrix = []
for row in matrix:
    min_value = min(row)
    min_index = row.index(min_value)
    new_row = row
    if min_value % 2 == 0:
        new_row[min_index] = 0
    else: 
        new_row[min_index] = 1
    new_matrix.append(new_row)  
for row in new_matrix:
    print(row)