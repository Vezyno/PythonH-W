def print_char():
  print('*')
# sim = input()
# print_char()
print_char(3)
# print_char()


x = 3 #Global
print('start value: ', x)
def pr():
  # global x
  x = 3
  x = pow(x, 10)
  print('changed value: ', x)
pr()
print(x)


def sum_d(n): #Определение функции с параметром
  sum = 0
  while n != 0:
    sum += n % 10
    n = n // 10
  return sum #Возврат значения функции
#Запуск программы
sum_d(int(input()))


import math
# Функция для вычисления площади треугольника по формуле Герона
def triangle_area(x, y, z):
    p = (x + y + z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))
# Проверка существования треугольника
def is_valid_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x
# Функция для ввода сторон треугольника через пробел и проверки их корректности
def get_triangle_sides():
    while True:
        try:
            # Ввод трёх сторон через пробел
            sides = list(map(float, input('Введите стороны треугольника через пробел (a b c): ').split()))
            if len(sides) != 3:
                print('Ошибка: нужно ввести три стороны.')
                continue
            a, b, c = sides
            if is_valid_triangle(a, b, c):
                return a, b, c
            else:
                print('Ошибка: стороны не образуют треугольник. Попробуйте снова.')
        except ValueError:
            print('Ошибка: введите корректные числа.')
# Список для хранения площадей треугольников
areas = []
# Ввод сторон трёх треугольников
for i in range(1, 4):
    print(f'Введите стороны {i}-го треугольника: ')
    a, b, c = get_triangle_sides()
    areas.append(triangle_area(a, b, c))
# Вывод площадей треугольников
for i in range(3):
    print(f'Площадь {i + 1}-го треугольника: {areas[i]}')
# Проверка, равны ли площади всех трёх треугольников
if areas[0] == areas[1] == areas[2]:
    print('Треугольники равновеликие')
else:
    print('Треугольники не равновеликие')


first_frac = input().split()
second_frac = input().split()
def divide(frac_1, frac_2):
  print(f'First frac is {frac_1[0]}/{frac_1[-1]}')
  print(f'Second frac is {frac_2[0]}/{frac_2[-1]}')
  result = [0, 0]
  result[0], result[-1] = float(frac_1[0]) * float(frac_2[-1]), float(frac_2[0]) * float(frac_1[-1])
  # chs, zhm = result
  print(f'Non reduced result is {result[0]}/{result[-1]}')
  def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n
  nod = gcd(result[0], result[-1])
  if result[-1]/nod != 1:
    print(f'Reduced result is {result[0]/nod}/{result[-1]/nod}')
  else:
    print(f'Reduced result is {result[0]/nod}')
divide(first_frac, second_frac)
print('----------------------')
print(gcd(20, 575))