# Задача №1
n = int(input("Введите натуральное число (не больше 100): "))
sum = 0
for i in range(1, n+1):
    sum += (i**3)
print(f"Сумма кубов натуральных чисел от 1 до {n} равна: {sum}")


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
array = [21,875,986,96552,2,545]
for item in array:
    print(item)