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

string = input("Введите строку: ")
sum_str = set()
for i in range(len(string)):
    for j in range(len(string), i, -1):
        hast_str = hashlib.sha256(string[i:j].encode()).hexdigest()
        sum_str.add(hast_str)
print(f'{string} - {len(sum_str) -1} уникальных подстрок')
