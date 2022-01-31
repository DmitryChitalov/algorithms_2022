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
рара - 6 уникальных подстрок рар ра ар ара р а
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify
import itertools

hash_lst = []


def unique_substr(salt, full_str):
    for i in range(0, len(full_str)):
        for j in range(i + 1, len(full_str) + 1):
            # print(full_str[i:j])
            if full_str[i:j] != full_str:
                obj = pbkdf2_hmac(hash_name='sha256',
                                  password=full_str[i:j].encode('utf-8'),
                                  salt=salt.encode('utf-8'),
                                  iterations=10000)

            hash_lst.append(hexlify(obj))
    return print(len(set(hash_lst)))


unique_substr('salt', 'momo')
# print(len(set([full_str[x:y] for x, y in itertools.combinations(range(len(full_str)), r = 2)])))
