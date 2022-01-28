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
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


from binascii import hexlify
from hashlib import md5, sha512


def count_unique_substring(input_str):
    hash_set = set()
    for i in range(0, len(input_str) - 1):
        for j in range(i + 1, len(input_str) + i):
            s_hash = md5(input_str[i:j].encode()).hexdigest()
            hash_set.add(s_hash)
    return len(hash_set)


print(count_unique_substring('papa'))
