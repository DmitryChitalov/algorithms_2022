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


base_str = input('Введите строку из латинских букв: ')

set_hash = set()
for len_substr in range(1, len(base_str)):
    for start_index in range(len(base_str) - len_substr + 1):
        substr = base_str[start_index : start_index + len_substr]
        set_hash.add(hashlib.sha256(substr.encode()).hexdigest())

print(f'Количество уникальных подстрок: {len(set_hash)}')