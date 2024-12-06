# Задача №1
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Ошибка: количество строк должно быть положительным целым числом.")
        return
    f = open(file, 'r', encoding="utf-8")
    all_lines = f.readlines()  
    f.close()  
    for line in all_lines[-lines:]:
        print(line, end='') 
read_last(5, 'article.txt')


# Задача №2
import os
def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Содержимое директории: {root}")
        for name in dirs:
            print(f"  Подкаталог: {name}")
print_docs('C:\Right\Games\GameDev')


# Задача №3
def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("?","")
    text = text.replace("!","")
    words = text.split()
    max_length = 0
    longest_words_list = []
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_words_list = [word]
        elif word_length == max_length:
            longest_words_list.append(word)
    print(longest_words_list)
longest_words('article.txt')


# Задача №4
def simple_text_editor():
    filename = input("Введите имя файла (без расширения): ")
    filename += ".txt" 
    with open(filename, 'w', encoding='utf-8') as file:
        print("Введите строки текста. Для сохранения файла введите пустую строку или строку со спец. символом.")
        while True:
            line = input() 
            if line == "!5" or line == "":
                print(f"Файл '{filename}' сохранен.")
                break
            file.write(line + '\n')  
simple_text_editor()