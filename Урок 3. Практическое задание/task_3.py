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


def hash_password(str_x):
    str_x = bytes(str_x, encoding='utf-8')
    result = hashlib.sha256(str_x).hexdigest()
    return result

def for_x(str_x):
    result = set()
    for i in range(len(str_x)):
        for j in range(i + 1, len(str_x) + 1):
            if str_x[i:j] == str_x:
                continue
            else:
                result.add(hash_password(str_x[i:j]))
    return len(result)


if __name__ == '__main__':
    user_str = input('Введите строку: ')
    print(f'{user_str} - {for_x(user_str)} уникальных подстрок')
