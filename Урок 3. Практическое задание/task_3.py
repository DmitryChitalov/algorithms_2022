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

def check_str(string):
    """
    Функция подсчета уникальных подстрок.
    В вычисление хеша подставляется slice с минимальной разницей в единицу,
    посколько полное слово получать не нужно.
    """
    sub_s = set()
    for i in range(len(string)):
        for y in range(len(string) - 1, i, -1):
            sub_s.add(hashlib.sha256(string[i:y].encode()).hexdigest)
    return f'Количество уникальных подстрок: {len(sub_s)}'


print(check_str("Papa"))
