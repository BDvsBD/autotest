# Статистика букв
# Напишите функцию letter_stat, которая на вход принимает строку our_str и возращает словарь letters_dict,
# где в качестве ключей буквы строки, а значениями являются числа,
# соответствующие количеству вхождений данной буквы в строку.
# Например (Ввод --> Вывод) :
# 'letter' --> {'l': 1, 'e': 2, 't': 2, 'r': 1}


def letter_stat(our_str):
    # Здесь нужно написать код
    letters_dict = {}
    for el in our_str:
        if el in letters_dict:
            letters_dict[el] += 1
        else:
            letters_dict[el] = 1
    return letters_dict

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ['letter', "honduras", "тегусигальпа", "автотестирование", "тензор", "управлениекачеством", 'мануальщик', '',
        'курс', 'ы', 'лол', 'кек']

test_data = [{'l': 1, 'e': 2, 't': 2, 'r': 1}, {'h': 1, 'o': 1, 'n': 1, 'd': 1, 'u': 1, 'r': 1, 'a': 1, 's': 1},
             {'т': 1, 'е': 1, 'г': 2, 'у': 1, 'с': 1, 'и': 1, 'а': 2, 'л': 1, 'ь': 1, 'п': 1},
             {'а': 2, 'в': 2, 'т': 3, 'о': 2, 'е': 2, 'с': 1, 'и': 2, 'р': 1, 'н': 1},
             {'т': 1, 'е': 1, 'н': 1, 'з': 1, 'о': 1, 'р': 1},
             {'у': 1, 'п': 1, 'р': 1, 'а': 2, 'в': 2, 'л': 1, 'е': 3, 'н': 1, 'и': 1, 'к': 1,
              'ч': 1, 'с': 1, 'т': 1, 'о': 1, 'м': 1},
             {'м': 1, 'а': 2, 'н': 1, 'у': 1, 'л': 1, 'ь': 1, 'щ': 1, 'и': 1, 'к': 1},
             {},
             {'к': 1, 'у': 1, 'р': 1, 'с': 1},
             {'ы': 1}, {'л': 2, 'о': 1}, {'к': 2, 'е': 1}
             ]

for i, d in enumerate(data):
    assert letter_stat(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
