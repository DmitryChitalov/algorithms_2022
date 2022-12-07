"""Задание 3.
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


def hashing_str(s):
    salt = 'sugar'
    res = hashlib.sha256((s + salt).encode()).hexdigest()
    return res


def substrings(s):
    n = len(s)
    hash_set = set()
    for i in range(n):
        hash_set.add(hashing_str(s[i]))
        for j in range(2, n):
            if i + j > n:
                break
            else:
                hash_set.add(hashing_str(s[i:j + i]))
    return hash_set


user_input = input('Введите строку, состоящую из строчных латинских букв: ')
print(f'{user_input} - {len(substrings(user_input))} уникальных подстрок')