import matplotlib.pyplot as plt
import numpy as np
import os

x = np.array([1,2,3,4,5,6])
y = np.array([15,12,18,21,12,15])
plt.plot(x,y, color='cyan', marker='.', markersize=10) # Создать график
plt.scatter(x, y, color='#FFD0EC', edgecolors='#1F2544', linewidth=3, s=40) # Создать график рассеяния
plt.title('Пример столбчатой диаграммы') # Название фигуры
# plt.grid() # Сделать квадратную сетку
# plt.xticks(np.array([0, 100, 5])) # Изобразить кординатную прямую
plt.xlabel('Ось х') # Подпись для оси х
plt.ylabel('Ось y') # Подпись для оси y
plt.xlim(-1, 10) # Установить лимит по х
plt.title('Первый график') # Название

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
plt.bar(x, y, label="бла блоа боа", alpha=0.5) # Сделать диаграмму
plt.legend() # Показать условные обозначения

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=labels, autopct='%1.1f%%',shadow=True) # Создать круговую диаграмму
plt.show() # Показать фигуру


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
dir = os.getcwd() # Получить путь к файлу
print(dir)
def f(a):
   return np.sin(a) + a + a * np.sin(a**2)
x = np.linspace(-10, 10, 1000)
y = [np.sin(a) + a + a * np.sin(a**2) for a in x]
# y = lambda a: np.sin(a) + a + a * np.sin(a**2) for a in x ????
plt.plot(x, f(x), color='red', linewidth=1)
plt.grid()
plt.savefig(dir + '/my_first_dependence.png', dpi=600) # Сохранить полученую фигуру
plt.annotate('Text', (0, 0), (2.5, 10))
plt.show()