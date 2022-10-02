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

st = input('Введите строку состоящую только из строчных латинских букв: ')
hsh_set = set()

for i in range(0, len(st) + 1):
    for j in range(0, i):
        hsh = hashlib.sha256(st[j:i].encode('utf-8')).hexdigest()
        if hsh not in hsh_set and st[j:i] != st:
            print(st[j:i])
            hsh_set.add(hsh)