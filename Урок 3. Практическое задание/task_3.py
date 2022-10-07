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

def uniqueness(unique_value):
    len_value = len(unique_value)
    hash_set = set()
    for i in range(len_value):
        for l in range(i + 1, len_value + 1):
            if unique_value[i:l] != unique_value:
                hash_set.add(hashlib.sha256(unique_value[i:l].encode('utf-8')).hexdigest())
    return len(hash_set)

print(uniqueness('papa'))