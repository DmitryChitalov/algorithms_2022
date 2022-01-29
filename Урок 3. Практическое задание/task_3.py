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
import hashlib
def unique_set(some_string: str) -> set:
    """
    find unique substrings in string
    :param some_string: str
    :return: set
    """
    hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
                for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
    return hash_set


if __name__ == "__main__":
    print(unique_set("papa"))
