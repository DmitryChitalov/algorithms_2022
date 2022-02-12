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


line = input('Введите строку: ')
substring = set()

for i in range(len(line)):
    for j in range(i+1, len(line) + 1):
        if line[i:j] != line:
            substring.add(hashlib.sha256(line[i:j].encode()).hexdigest())
            print(line[i:j], end=' ')


print(substring)
print(len(substring))

