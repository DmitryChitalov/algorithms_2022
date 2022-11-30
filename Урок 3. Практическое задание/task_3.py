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

def hashing_str(a):
    salt = 'peper'
    res = hashlib.sha256((a + salt).encode()).hexdigest()
    return res


def substrings(a):
    n = len(a)
    hash_set = set()
    for i in range(n):
        hash_set.add(hashing_str(a[i]))
        for j in range(2, n):
            if i + j > n:
                break
            else:
                hash_set.add(hashing_str(a[i:j + i]))
    return hash_set


user_input = input('Введите строку: ')
print(f'Из строки {user_input} можно получить {len(substrings(user_input))} уникальных подстрок')