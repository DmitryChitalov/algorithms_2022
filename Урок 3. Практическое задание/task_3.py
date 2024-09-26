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


def count_substrings(input_string):
    lst = []
    for i in range(len(input_string) + 1):
        for j in range(i, len(input_string) + 1):
            lst.append(input_string[j - i:j])

    lst = [item for item in lst if item != '' and item != input_string]

    result = set()
    for sub_string in lst:
        sub_string_hash = hashlib.md5(sub_string.encode()).hexdigest()
        result.add(sub_string_hash)

    return len(result)


if __name__ == '__main__':
    print(count_substrings('papa'))
