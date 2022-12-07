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
from uuid import uuid4

substrings = set()
some_string = input('Введите строку: ')
salt = str(uuid4().hex)
for id in range(len(some_string)):
    end = len(some_string) if id == 0 else len(some_string) + 1
    for id2 in range(id + 1, end):
        substr = some_string[id:id2]
        hashed_substr = hashlib.sha256((salt + substr).encode('utf-8')).hexdigest()
        substrings.add(hashed_substr)

print('У строки {} {} уникальных подстрок'.format(some_string, len(substrings)))
