# Задача №1
n = int(input("Введите натуральное число (не больше 100): "))
sum = 0
for i in range(1, n+1):
    sum += (i**3)
print(f"Сумма кубов натуральных чисел от 1 до {n} равна: {sum}")

print(list(range(1, 11)))
# Задача №2
print("     1   2   3   4   5   6   7   8   9")
for i in range(1, 10):
    print(f"{i}|", end="")  
    for j in range(1, 10):
        if j*i > 9:
            print(f"  {i * j}", end="")
        else:
            print(f"   {i * j}", end="")  
    print() 


# Задача №3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
n = len(matrix)
rotated = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        rotated[j][n - 1 - i] = matrix[i][j]
for row in rotated:
    print(row)