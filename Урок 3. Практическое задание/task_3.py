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


def substring_amount(str):

    substr_hash = set()

    for i in range(len(str)):
        if i == 0:
            for j in range(len(str)):
                substr_hash.add(hashlib.sha256(str[i:j].encode()).hexdigest())
                # print(str[i:j])
        else:
            for j in range(len(str), i, -1):
                substr_hash.add(hashlib.sha256(str[i:j].encode()).hexdigest())
                # print(str[i:j])
    return len(substr_hash)


print(substring_amount('mother'))
