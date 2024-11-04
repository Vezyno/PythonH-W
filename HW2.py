# Задача №1
num1 = float(input("Введите первое вещественное число: "))
num2 = float(input("Введите второе вещественное число: "))
if num2 == 0:
    print("Ошибка: Деление на ноль невозможно.")
else:
    result = num1 / num2
    print(f"Результат деления {num1} на {num2} равен {result:.2f}")


# Задача №2
total_amount = float(input("Введите сумму покупки (в у.е.): "))
if total_amount > 20:
    discount = total_amount * 0.35  
    final_price = total_amount - discount  
discount = round(discount, 2)
final_price = round(final_price, 2)
print(f"Размер предоставленной скидки: {discount} у.е.")
print(f"Итоговая стоимость покупки: {final_price} у.е.")


# Задача №3
months = {
    1: ("Январь", "Зима"),
    2: ("Февраль", "Зима"),
    3: ("Март", "Весна"),
    4: ("Апрель", "Весна"),
    5: ("Май", "Весна"),
    6: ("Июнь", "Лето"),
    7: ("Июль", "Лето"),
    8: ("Август", "Лето"),
    9: ("Сентябрь", "Осень"),
    10: ("Октябрь", "Осень"),
    11: ("Ноябрь", "Осень"),
    12: ("Декабрь", "Зима")
}
month_number = int(input("Введите номер месяца (от 1 до 12): "))
if month_number < 1 or month_number > 12:
    print("Ошибка: Введите число от 1 до 12.")
else:
    month_name, season = months[month_number]
    print(f"Месяц: {month_name}, Время года: {season}")