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


word = 'papri'
underlines = set()
for left_index in range(len(word)):
    for right_index in range(left_index + 1, len(word) + 1):
        if word[left_index:right_index] != word:
            underlines.add(hashlib.sha512(word[left_index:right_index].encode()).hexdigest())
            print(word[left_index:right_index])


for underline in underlines:
    print(underline)  
print(f'Количество элементов в множестве: {len(underlines)}')

