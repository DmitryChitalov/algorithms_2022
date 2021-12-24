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
import hashlib


def substring_count(input_string):

    input_string = str(input_string).lower()

    length = len(input_string)
    print(input_string, length)
    hash_set = set()

    for i in range(length):
        for j in range(i + 1, length + 1):
            if input_string[i:j] != input_string:
                h = hashlib.sha256(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    print(hash_set)

    return len(hash_set)


some_string = 'рара'

print(f'Количество подстрок в строке {some_string}: {substring_count(some_string)}')