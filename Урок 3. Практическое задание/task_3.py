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

some_str = 'papap'

def uniq_substrings(my_str):
    str_set = set()
    for i in range(0, len(my_str)):
        for j in range(len(my_str), i, -1):
            res = hashlib.sha256(my_str[i: j].encode()).hexdigest()
            str_set.add(res)
    str_set.remove(hashlib.sha256(my_str.encode()).hexdigest())
    return len(str_set)

print(uniq_substrings(some_str))