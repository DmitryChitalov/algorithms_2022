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
import hashlib, itertools

# не понимаю почему подстрок 6, у меня выходит 10 уникальных значений


def count_el_string(string):
    result_string = set()
    multi_hash = set()
    for i in range(len(string)):
        for item in itertools.combinations(string, i):
            result_string.add(''.join(item))
    result_string.remove('')
    print(result_string)

    for i in result_string:
        hash_obj = hashlib.sha256(i.encode("utf-8")).hexdigest()
        multi_hash.add(hash_obj)
    print(multi_hash)
    print(len(multi_hash), "Уникальных значений ")


count_el_string(input("Enter word: "))


