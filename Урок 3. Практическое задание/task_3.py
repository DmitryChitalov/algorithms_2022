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



def get_set_hash (str):
    set_hash = set()

    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            sub = str[i:j]
            sub_hash = hashlib.sha256(sub.encode('utf-8')).hexdigest()
            set_hash.add(sub_hash)
        set_hash.discard(str)
    return set_hash

str = 'helloworld'
sub_str_hash = get_set_hash(str)
print(sub_str_hash)


# def get_set_sub (str):
#     set_sub = set()
#
#     for i in range(len(str)):
#         for j in range(i+1, len(str)+1):
#             sub = str[i:j]
#             # print(i, j, sub)
#             set_sub.add(sub)
#         set_sub.discard(str)
#     return set_sub


# sub_str = get_set_sub(str)
# print(sub_str)




