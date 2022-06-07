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

def quantity_sub (some_str):
    some_set = set()
    some_sub = set()
    for i in range(len(some_str)):
        for j in range(i + 1, len(some_str) + 1):
            if some_str[i:j] != some_str:
                some_set.add(hashlib.sha256(some_str[i:j].encode()).hexdigest())
                some_sub.add(some_str[i:j])
    return [some_set, some_sub]


for i in quantity_sub("papa")[1]: print(i)
print(f'\n{quantity_sub("papa")[0]}')
print(f'Количество элементов в множестве: {len(quantity_sub("papa")[0])}')