import math

# Задача №1
R = float(input("Введите радиус круга в сантиметрах: "))
length_of_circle = 2 * math.pi * R
area_of_circle = math.pi * R ** 2
length_of_circle_rounded = round(length_of_circle, 2)
area_of_circle_rounded = round(area_of_circle, 2)
print(f"Длина окружности: {length_of_circle_rounded} см")
print(f"Площадь круга: {area_of_circle_rounded} см^2")


# Задача №2
x = 10
y = 55
print(f"До замены: x = {x}, y = {y}")
x, y = y, x
print(f"После замены: x = {x}, y = {y}")


# Задача №3
g = 9.81
L = float(input("Введите длину маятника в метрах: "))
T = 2 * math.pi * math.sqrt(L / g)
print(f"Период колебания маятника: {T:.2f} секунд")