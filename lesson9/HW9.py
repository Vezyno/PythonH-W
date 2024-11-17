import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def f(x, alpha, beta):
    return (x**beta + alpha**beta) / x**beta

# Задаем диапазон значений x для основного графика
x_main = np.linspace(-3, -0.1, 400)  # от -3 до -0.1, чтобы избежать деления на ноль
# Задаем диапазон значений x для врезки
x_zoom = np.linspace(-0.1, -10, 100)  # от -0.1 до -10 для врезки

# Параметры для графиков
params = [
    (1, 0.5),
    (1, -0.5),
    (2, 0.5),
    (2, -1)
]

# Построение графиков
plt.figure(figsize=(12, 6))

for alpha, beta in params:
    # Основной график
    plt.plot(x_main, f(x_main, alpha, beta), label=f'α={alpha}, β={beta}')
    
    # Врезка
    plt.plot(x_zoom, f(x_zoom, alpha, beta), linestyle='--', color=plt.gca().lines[-1].get_color())

# Добавление прямой f(x) = 0
plt.axhline(0, color='black', lw=0.5, ls='--', label='f(x) = 0')

# Настройка графика
plt.title('Графики функции для x < 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axvline(0, color='black', lw=0.5, ls='--')  # Вертикальная линия x=0
plt.legend()
plt.grid()
plt.xlim(-10, 0)
plt.ylim(-10, 10)
plt.show()

# Задание 4
def f(x, alpha, beta):
    return (x**beta + alpha**beta) / x**beta

x = np.linspace(0.1, 3, 400)  
params = [
    (1, 0.5),
    (1, -0.5),
    (1, -1.5)
]

common_params = [(1, 0), (1, -1)]
unique_params = [
    [(1, 0.5), (1, 0.8)],
    [(1, -0.5), (1, -0.8)],
    [(1, -1.5), (1, -2.5)]
]

plt.figure(figsize=(15, 5))

for i, (alpha_common, beta_common) in enumerate(common_params):
    plt.subplot(1, 3, i + 1)
    # Общие графики
    plt.plot(x, f(x, alpha_common, beta_common), 'b--', label=f'α={alpha_common}, β={beta_common}')
    # Уникальные графики
    for alpha_unique, beta_unique in unique_params[i]:
        plt.plot(x, f(x, alpha_unique, beta_unique), label=f'α={alpha_unique}, β={beta_unique}')
    plt.title(f'Графики для α={alpha_common}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
plt.show()