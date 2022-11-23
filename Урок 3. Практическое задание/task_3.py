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


def get_hash_set(user_string):
    res = set()

    for i in range(len(user_string)):
        for j in range(len(user_string)+1):
            if len(user_string[i:j]) != 0 and len(user_string[i:j]) != len(user_string):
                res.add(hashlib.sha256(user_string[i:j].encode()).hexdigest())

    return res

if __name__ == '__main__':
    user_str = 'papa'
    print(get_hash_set(user_str))
