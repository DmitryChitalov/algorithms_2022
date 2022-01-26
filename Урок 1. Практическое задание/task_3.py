"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from itertools import islice

companies_salaries = {'Amazon': 10000, 'Audi': 5000, 'Tesla': 30000000000000, 'Coca-Cola': 2000, 'KFC': 9202,
                      'SpaceX': 3440, 'Facebook': 49395, 'Google': 354645400000, 'Apple': 7757345000000}
key_val = list(companies_salaries.items())


def sorted_ver():  # Итог: O(n log n)
    key_val_sorted = sorted(key_val, key=lambda i: i[1], reverse=True)  # O(n log n)
    for v in islice(key_val_sorted, 3):  # O(n)
        print('sorted: ', v)  # O(1)


sorted_ver()


def max_ver():  # Итог: O(n)
    for v in islice(key_val, 3):  # O(1)
        print('max: ', max(key_val, key=lambda i: i[1]))  # O(n)
        key_val.remove(max(key_val, key=lambda i: i[1]))  # O(n)


max_ver()

# Вывод: решение с sorted_ver() эффективнее, т.к O(n log n) потребляет меньше времени чем O(n^2)
