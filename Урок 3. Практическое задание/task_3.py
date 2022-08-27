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


def str_slices(str_in):
    set_substr = set()
    for left in range(len(str_in)):
        for right in range(left + 1, len(str_in) + 1):
            if str_in[left:right] != str_in:
                set_substr.add(hashlib.sha256(str_in[left:right].encode()).hexdigest())
    return set_substr


if __name__ == '__main__':
    str_to_slice = 'papa'
    print(f'{str_to_slice} - {len(str_slices(str_to_slice))} уникальных подстрок')
