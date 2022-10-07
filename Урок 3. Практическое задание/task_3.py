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


def set_string(work_str):
    """
    Создание множества хэш для подстрок заданной строки
    :param work_str: заданная строка
    :return: множество хэш подстрок
    """
    res_set_str = set()
    res_set_hash = set()
    for i in range(len(work_str)):
        for j in range(i + 1, len(work_str) + 1):
            if work_str[i:j] != work_str:
                res_set_hash.add(hashlib.sha256(work_str[i:j].encode('utf-8')).hexdigest())
                res_set_str.add(work_str[i:j])
                print(work_str[i:j])
    print(res_set_str)
    print(res_set_hash)
    return res_set_str


if __name__ == '__main__':
    my_str = input('Введите слово: ')
    print(f'Количество уникальных подстрок в строке - {my_str} равно {len(set_string(my_str))}')