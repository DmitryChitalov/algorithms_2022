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

s = input('Введите слово: ')
s_cp = s
# print(len(s))
hash_list = []

for i in range(1, len(s) + 1):
    hash_s_cp = hashlib.sha256(s_cp.encode()).hexdigest()

    if not (hash_s_cp in hash_list) and s_cp != s:
        hash_list.append(hash_s_cp)
        print(s_cp)

    for n in range(1, len(s_cp)):
        temp_s = s_cp[:len(s_cp) - n]
        hash_s_cp = hashlib.sha256(temp_s.encode()).hexdigest()

        if not (hash_s_cp in hash_list):
            print(temp_s)
            hash_list.append(hash_s_cp)

    s_cp = s[i:len(s)]

print(len(hash_list),'уникальных подстрок')


