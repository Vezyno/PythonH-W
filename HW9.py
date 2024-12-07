import numpy as np
import matplotlib.pyplot as plt

# Задача №1-2
def f(x, a, b):
    return (x**b + a**b) / (x**b)
x_pos = np.linspace(0.1, 10, 400)  # для x > 0
x_neg = np.linspace(-10, -0.1, 400)  # для x < 0
params = [(1, 1), (2, 1), (1, 2), (1, 0.5), (1, -0.5), (1, -1.5)]
plt.figure(figsize=(10, 8))
for a, b in params:
    y_pos = f(x_pos, a, b)
    plt.plot(x_pos, y_pos, label=f'a={a}, b={b}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функции f(x) для различных значений a и b (x > 0)')
plt.grid(True)
plt.legend()
# Вставка для малых x (для x около 0)
plt.axes([0.1, 0.5, 0.35, 0.35]) 
for a, b in params:
    y_pos_zoom = f(np.linspace(0.1, 1, 100), a, b)
    plt.plot(np.linspace(0.1, 1, 100), y_pos_zoom, label=f'a={a}, b={b}')
plt.title('Малые x')
plt.grid(True)
# Вставка для больших x (для x > 5)
plt.axes([0.55, 0.5, 0.35, 0.35]) 
for a, b in params:
    y_pos_zoom_large = f(np.linspace(5, 10, 100), a, b)
    plt.plot(np.linspace(5, 10, 100), y_pos_zoom_large, label=f'a={a}, b={b}')
plt.title('Большие x')
plt.grid(True)
plt.savefig('graph_x_pos.svg', format='svg')
plt.show()


# Задача №3
plt.figure(figsize=(10, 8))
# Строим графики для x < 0
for a, b in params:
    y_neg = f(x_neg, a, b)
    plt.plot(x_neg, y_neg, label=f'a={a}, b={b}')
# Добавляем прямую f(x) = 0
plt.axhline(0, color='black', linestyle='--', label='f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функции f(x) для различных значений a и b (x < 0)')
plt.grid(True)
plt.legend()
plt.axes([0.55, 0.5, 0.35, 0.35]) 
for a, b in params:
    y_neg_zoom = f(np.linspace(-10, -5, 100), a, b)
    plt.plot(np.linspace(-10, -5, 100), y_neg_zoom, label=f'a={a}, b={b}')
plt.title('x → -inf')
plt.grid(True)
plt.savefig('graph_x_neg.svg', format='svg')
plt.show()