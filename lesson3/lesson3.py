x = 10
sum = 0
count = 0
while x > 0: # This is circle of x - 1 & print(x)
  print(x)
  sum += x #sum = sum + x
  count += 1
  x -= 1 # x = x - 1
  # if x == 5:
  #   break
  # else:
  #   continue
print('Circle is continued')
print(f'Sum is {sum}')
print(f'Count is {count}')


# Вычислим факториал вручную...
number = int(input("Input num: "))
i = 1
factorial = 1
while i <= number:
  factorial *= i #Это то же самое, что и factorial = factorial * i
  i += 1         #Тут также, i = i + 1
print("Factorial of", str(number), "is", str(factorial))


sum = 0
for i in range(0, 21, 2):
  for j in range(20):
    # print(j)
    sum += i*j

print(sum)


n = int(input("Введите целое цисло не меньше 2 \n "))
i = 2
while n%i != 0:
  i += 1
print("Наименьший натуральный делитель:", i)