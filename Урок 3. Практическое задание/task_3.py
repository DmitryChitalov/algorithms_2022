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
from hashlib import sha1


def substring_count(string):
    str_len = len(string) + 1
    hash_count = set()
    for i in range(str_len):
        for k in range(i + 1, str_len):
            if string[i:k] != string:
                hash_count.add(sha1(string[i:k].encode()).hexdigest())
    return len(hash_count)


x = str(input("Enter string: "))
print(f'String {x} has {substring_count(x)} unique substring.')