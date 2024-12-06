import re
# Задача №1
def check_license_plate(plate):
    plate = plate.upper()
    plate = re.sub(r'[^АВЕКМНОРСТУХ0123456789]', '', plate)
    if re.fullmatch(r'[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}', plate):
        return "Частный легковой автомобиль"
    elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}[0-9]{3}[0-9]{2,3}', plate):
        return "Такси"
    else:
        return "Некорректный номер"
while True:
    user_input = input("Введите номер (или 'exit' для выхода): ")
    if user_input.lower() == 'exit' or user_input == "":
        break
    result = check_license_plate(user_input)
    print(result)


# Задача №2
print(len(re.findall(r'\b[а-яА-ЯёЁa-zA-Z-]+\b', ",.sjjgdhfg kjsng, kljnsfdg параыдвлп дыFGвадподла  Ыодлавпо")))


# Задача №3
text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
time_pattern = r'\b(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])(:([0-5][0-9]))?\b'
updated_text = re.sub(time_pattern, '(TBD)', text)
print(updated_text)


# Задача №4
text = "Владимир устроился на работу в ФГУП НИЦ ГИДГЕО"
abbreviation_pattern = r'\b([А-ЯЁ]{2,}(?:s+[А-ЯЁ]{2,})*)\b'
abbreviations = re.findall(abbreviation_pattern, text)
print("Найденные аббревиатуры:")
for abbr in abbreviations:
    print(abbr)