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

from hashlib import sha256

hash_set = set()
origin_set = set()
text = input('Введите строку в которой хотите подсчитать колическтво уникальных подстрок: ')

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        if text[i:j] != text:
            hash_set.add(sha256(text[i:j].encode()).hexdigest())
            origin_set.add(text[i:j])

print(origin_set)
print(hash_set)
print(f'Количество элементов в множестве: {len(hash_set)}')