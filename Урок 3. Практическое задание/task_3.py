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

import random
import hashlib

letters_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
                'c', 'v', 'b', 'n', 'm']


def create_hash_1(letters, num) -> set:
    """ Функция принимает в себя список букв и число букв для создания строки и возвращает уникальное количество хешей
    подстрок. Если следовать ТЗ, то ход выполнения должен быть такой, но для 'papa' вместо 6 уникальных подстрок
    мы имеет 15 хешей неуникальных подстрок"""
    s = ''.join([random.choice(letters) for _ in range(num)])
    substrings_h = set()
    for i in range(len(s)+1):
        for j in range(len(s)):
            res = s[i:j + i + 1]
            if res != '' and res != s:
                substrings_h.add((hashlib.sha256(res.encode())).hexdigest())
    return substrings_h


def create_hash_2(letters, num) -> set:
    """ Функция принимает в себя список букв и число букв для создания строки и возвращает уникальное количество
    хешей подстрок. Поэтому. Возможно правильнее было бы сначала подготовить множество подстрок,
    а потом преобразовать их в хеш"""
    s = ''.join([random.choice(letters) for _ in range(num)])
    substrings_set = set([s[i:j + i + 1] for j in range(len(s)) for i in range(len(s)+1)
                          if (s[i:j + i + 1]) != '' and (s[i:j + i + 1]) != s])
    substrings_hash = {hashlib.sha256(i.encode()).hexdigest() for i in substrings_set}
    return substrings_hash


n = 4

substrings_hash1 = create_hash_1(letters_list, n)
substrings_hash2 = create_hash_2(letters_list, n)

print(substrings_hash1)
print(substrings_hash2)
