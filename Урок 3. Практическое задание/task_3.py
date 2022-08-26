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


from uuid import uuid4
import hashlib


def create_hash_substring(string):
    """Создает хеш всех подстрок, дубли удаляет"""
    hash_set = set()
    salt = uuid4().hex
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            slice_str = string[i:j]
            if slice_str != string:
                hash_set.add(hashlib.sha256(salt.encode() +
                             slice_str.encode()).hexdigest())
    return hash_set


string = input('Введите строку: ')

hash_subs = create_hash_substring(string)

print('-' * 100)
print(f'Множество из хеш:')
for item in hash_subs:
    print(item)

print(f'Длина множества = {len(hash_subs)}')
print('*' * 100)
