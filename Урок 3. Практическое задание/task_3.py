"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

def definition_substrings(definition_str):
    substrings_set = set()
    for i in range(len(definition_str)):
        for j in range(len(definition_str)):
            if definition_str[i:j + 1] != '' and definition_str[i:j + 1] != definition_str:
                substrings_set.add(definition_str[i:j + 1])
    return substrings_set


strings_1 = input('Введите строку: ')
substrings = definition_substrings(strings_1)
print(f'{strings_1} - {len(substrings)} уникальных подстрок')
print(*(el for el in substrings), sep='\n')
