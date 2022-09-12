"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,.
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


def my_func(my_value):
    len_value = len(my_value)
    my_set = set()
    for i in range(len_value):
        for j in range(i + 1, len_value + 1):
            if my_value[i:j] != my_value:
                my_set.add(hashlib.sha256(my_value[i:j].encode('utf-8')).hexdigest())
    return len(my_set)


print(my_func('papa'))  # 6
