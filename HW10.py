import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

list_data = [1, 2, 3, 4, 5, 1, 2, 3]
series_from_list = pd.Series(list_data)

numpy_array = np.array([10, 20, 30, 20, 10, 10])
series_from_numpy = pd.Series(numpy_array)

data_dict = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
             }
df_from_dict = pd.DataFrame(data_dict)

print("Series из списка:")
print(series_from_list)
print("\nSeries из массива NumPy:")
print(series_from_numpy)
print("\nDataFrame из словаря:")
print(df_from_dict)







# Получаем частоты уникальных элементов для Series
series_frequency = series_from_list.value_counts()

# Для нескольких столбцов DataFrame (если нужно)
columns_frequency = df_from_dict[['A', 'B']].apply(pd.Series.value_counts).fillna(0)

# Вывод частот уникальных элементов
print("\nЧастоты уникальных элементов в первой Series:")
print(series_frequency)
print("\nЧастоты уникальных элементов в столбцах DataFrame:")
print(columns_frequency)

# Построение гистограммы для частот элементов в series_from_list
plt.figure(figsize=(8, 6))
plt.bar(series_frequency.index.astype(str), series_frequency.values, color='skyblue')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма частот уникальных значений в Series')
plt.show()

# Построение семейства гистограмм для нескольких столбцов DataFrame
columns_frequency.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограммы частот уникальных значений в столбцах DataFrame')
plt.show()

