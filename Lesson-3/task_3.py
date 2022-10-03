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


def count_str(string):
    substring = set()
    str_1 = string
    for i in range(len(str_1)):
        for j in range(len(str_1)):
            el = str_1[0:j + 1]
            el = hashlib.sha256(el.encode('utf-8')).hexdigest()
            substring.add(el)
        str_1 = str_1[1:]
    substring.discard(hashlib.sha256(string.encode('utf-8')).hexdigest())
    print(substring)
    print(f'{string} - {len(substring)} уникальных подстрок')


if __name__ == "__main__":
    count_str('papa')
