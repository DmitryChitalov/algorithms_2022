"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
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

"""
третья функция самая эфективная
Ее сложность O(n), использование max() - оказалось самым выгодным вариантом 
"""
from collections import OrderedDict


def first_func(dict_in: dict) -> dict:
    # O(n^2)
    res = {}
    for i in range(3):  # O(1)
        for k, v in dict_in.items():  # O(n)
            if k == 0:  # O(1)
                pass  # O(1)
            is_max = True  # O(1)
            for n_v in dict_in.values():  # O(n)
                if n_v > v:  # O(1)
                    is_max = False  # O(1)
            if is_max:  # O(1)
                res[k] = v  # O(1)
                dict_in[k] = 0  # O(1)

    return res


def sec_func(dict_in: dict) -> dict:
    # O(n log n)
    sorted_dict = OrderedDict(sorted(dict_in.items(), key=lambda i: i[1], reverse=True))  # O(n log n)
    res = {}
    for k, v in sorted_dict.items():  # O(1) беру только три элекмента массива
        res[k] = v  # O(1)
        if len(res) == 3:  # O(1)
            return res  # O(1)
    return res

def third_func(dict_in: dict) -> dict:
    # O(n)
    res = {}# O(1)
    for i in range(3): # O(1)
        maxim = max(dict_in.items(), key= lambda i: i[1]) # O(n)
        del dict_in[maxim[0]] # O(1)
        res[maxim[0]] = maxim[1] # O(1)
    return res # O(1)


print(first_func(
    {'first': 100, 'sec': 200, 'third': 300, 'fourth': 400, 'fifth': 500, 'sixth': 600, "seventh": 700, "eighth": 800,
     'ninth': 900}))
print(sec_func(
    {'first': 100, 'sec': 200, 'third': 300, 'fourth': 400, 'fifth': 500, 'sixth': 600, "seventh": 700, "eighth": 800,
     'ninth': 900}))
print(third_func(
    {'first': 100, 'sec': 200, 'third': 300, 'fourth': 400, 'fifth': 500, 'sixth': 600, "seventh": 700, "eighth": 800,
     'ninth': 900}))
