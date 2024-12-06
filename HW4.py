# Задача №1
input_string = "абнннмноннпннн"
max_count = 0
count = 0
result = ""
max_count_list = []
for i in range(len(input_string)):
    if input_string[i] == 'н':
        max_count += 1
        count += 1
        result += "!"
    else:
        max_count_list.append(max_count)
        max_count = 0
        result += input_string[i]
print(f"Всего было выполненно {count} замен")
print(f"Максимальная длинна замены: {max(max_count_list)}")
print("Новая строка:", result)


# Задача №2
input_string = "Пример строки (содержимое) для теста."
open_index = input_string.find('(')
close_index = input_string.find(')')
if open_index < close_index:
    inside_content = input_string[open_index + 1:close_index]
else:
    print("Скобки не найдены или расположены некорректно.")
print("Символы внутри скобок:", inside_content)


# Задача №3
input_string = "Абстракция, авария, аллея, машина, земля, арка, зебра"
words = input_string.split()
print(words)
result = []
for word in words:
    if word.lower()[:1] == "а" or word.lower()[-1:] == "я":
        result.append(word)
print("Подходящие слова:", result)