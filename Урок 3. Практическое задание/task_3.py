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


def unique_substrings(word, sub_dict={}, sub_list=[]):
    """
    Решение через словарь, т.к. подсказку увидел после написания кода =3
    """
    for index in range(1, len(word)):
        sub_dict[hashlib.sha256(word[:index].encode('utf-8')).hexdigest()] = word[:index]
    for index in range(0, len(word) - 1):
        sub_dict[hashlib.sha256(word[:index:-1].encode('utf-8')).hexdigest()] = word[:index:-1]
    for value in sub_dict.values():
        sub_list.append(value)
    return sub_list


if __name__ == '__main__':
    print(unique_substrings('papa'))
