"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

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


def unique_subrows(row, set_hash_subrows=set(), dict_hash_subrows={}):
    for i in range(len(row)):
        for j in range(1, len(row) + 1):
            if row[i:j] != row and row[i:j]:
                hash_subrow = hashlib.sha256(row[i:j].encode()).hexdigest()
                set_hash_subrows.add(hash_subrow)
    return set_hash_subrows


print(len(unique_subrows('papa')))
