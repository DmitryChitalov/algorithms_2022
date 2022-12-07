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
def new_value():
    in_st = input('Введите строку для перебора: ')
    get_hashes = get_hash(in_st)
    print(f"{in_st} - {len(get_hashes)} уникальных подстрок")
    print('Hash Подстроки:', *get_hashes, sep='\n')


def get_hash(s):
    value = set()
    for size in range(1, len(s)):
        in_f = 0
        in_n = size
        while in_n <= len(s):
            string_to_hash = s[in_f: in_n]
            hash_string = hashlib.sha256(string_to_hash.encode('utf-8')).hexdigest()
            value.add(hash_string)
            in_f += 1
            in_n += 1
    return value
new_value()