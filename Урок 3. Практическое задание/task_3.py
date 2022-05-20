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

import hashlib


def sub_string(user_string):
    orig_hash = hashlib.sha1(user_string.encode('utf-8')).hexdigest()
    temp_set = set()
    for i in range(len(user_string)):
        for j in range(len(user_string)):
            temp_hash = hashlib.sha1(user_string[i:j + 1].encode('utf-8')).hexdigest()
            # Отсекаем пустую строку и оригинальную строку:
            temp_set.add(temp_hash) if orig_hash != temp_hash and len(user_string[i:j + 1]) > 0 else None
    return temp_set


input_string = input('Введите строку: ')
a = sub_string(input_string)
print(f'Количество уникальных подстрок в строке {input_string} составляет {len(a)} шт.')
