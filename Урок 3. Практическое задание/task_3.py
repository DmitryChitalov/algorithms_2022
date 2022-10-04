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

# a = 0
# ab = 2 a b
# abc = 5 a ab b bc c
# abcd = 9  a ab abc b bc bcd cd c d
# abcde = 14 a ab abc abcd b bc bcd bcde cd cde c d de e

import hashlib

s = 'рара'
n = len(s)
my_set = set()
my_hash_set = set()
for el in range(n):
    for i in range(n + 1):
        substring = s[el:i]
        if substring != '' and substring != s:
            my_set.add(substring)
            my_hash = hashlib.sha256(substring.encode()).hexdigest()
            my_hash_set.add(my_hash)
print(f'{s} - {len(my_hash_set)} уникальных подстрок.')
print(*my_set, sep='\n')
