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

str_obj1 = 'marka'
sub_strings = set()


def sub_string_counter(str_obj, set_obj):
    start = 0
    end = len(str_obj)
    while start < len(str_obj):
        s = hashlib.sha256(str_obj[start:end].encode('utf-8')).hexdigest()
        start += 1
        set_obj.add(s)
    start = 0
    end = 0
    while end <= len(str_obj):
        s = hashlib.sha256(str_obj[start:end].encode('utf-8')).hexdigest()
        end += 1
        set_obj.add(s)
    start = 0
    while start < len(str_obj):
        s = hashlib.sha256(str_obj[start:end].encode('utf-8')).hexdigest()
        start += 1
        set_obj.add(s)
    start = 1
    end = 2
    while start < len(str_obj) - 1:
        while end != len(str_obj):
            s = hashlib.sha256(str_obj[start:end].encode('utf-8')).hexdigest()
            end += 1
            set_obj.add(s)
        start += 1
        end = start
    set_obj.remove(hashlib.sha256(''.encode('utf-8')).hexdigest())
    set_obj.remove(hashlib.sha256(str_obj.encode('utf-8')).hexdigest())
    return len(set_obj)


print(sub_string_counter(str_obj1, sub_strings))



