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


def count(string):
    list_1 = []
    for i in range(len(string) + 1):
        for j in range(i, len(string) + 1):
            list_1.append(string[j - i:j])

    list_1 = [item for item in list_1 if item != '' and item != string]

    result = set()
    for substring in list_1:
        substring_hash = hashlib.sha256(substring.encode()).hexdigest()
        result.add(substring_hash)

    return len(result)


if __name__ == '__main__':
    print(count('papa'))
