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

from random import randint
import hashlib


def task_3(n):
    letters = [chr(randint(97, 122)) for _ in range(n)]
    test_str = ''.join(letters)
    print(f'Исходная строка: {test_str}')
    sub_str_hash = set()
    for i in range(1, n):
        sub_str_hash.add(hashlib.sha256(test_str[:n - i].encode('utf-8')).hexdigest())
        if i < n - i:
            sub_str_hash.add(hashlib.sha256(test_str[i:n - i].encode('utf-8')).hexdigest())
        sub_str_hash.add(hashlib.sha256(test_str[i:].encode('utf-8')).hexdigest())

    print(f'Количество уникальных подстрок равно: {len(sub_str_hash)}')


if __name__ == '__main__':
    task_3(10)
