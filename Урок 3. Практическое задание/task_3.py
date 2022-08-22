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

import random
import hashlib

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
           'v', 'b', 'n', 'm']
n = 4
s = ''.join([random.choice(letters) for x in range(n)])
# s = 'papa'

"""Если следовать ТЗ, то ход выполнения должен быть такой, но для 'papa' вместо 6 уникальных подстрок мы имеет 15
хешей неуникальных подстрок"""
substrings_h = set()
for i in range(len(s)+1):
    for j in range(len(s)):
        res = s[i:j + i + 1]
        if res != '' and res != s:
            substrings_h.add((hashlib.sha256(res.encode())).hexdigest())

# print(substrings_h)

"""Возможно правильнее было бы сначала подготовить множество подстрок, а потом преобразовать их в hash"""
substrings_set = set([s[i:j + i + 1] for j in range(len(s)) for i in range(len(s)+1)
                      if (s[i:j + i + 1]) != '' and (s[i:j + i + 1]) != s])
substrings_hash = [hashlib.sha256(i.encode()).hexdigest() for i in substrings_set]
# print(substrings_hash)
