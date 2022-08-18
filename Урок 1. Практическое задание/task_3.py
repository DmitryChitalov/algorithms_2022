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

Примечание: ПРОШУ  ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def search1(in_dict: dict):         # O(n log n)
    lst = list(in_dict.values())           # O(n)
    lst.sort()                             # O(n log n)
    if len(lst) >= 3:                      # O(1)
        lst = [lst[-1], lst[-2], lst[-3]]  # O(1)
    else:                                  # O(1)
        lst = lst[::-1]                    # O(1)
    res = {}                               # O(1)
    for val in lst:                        # O(n)
        for el in in_dict:                 # O(n)
            if val == in_dict[el]:         # O(1)
                res.setdefault(el, val)    # O(1)
    return res                             # O(1)


def search2(in_dict: dict):                                 # O(n)
    if len(in_dict) >= 1:                                        # O(1)
        max1 = in_dict.popitem()                                 # O(1)
    else:                                                        # O(1)
        return {}                                                # O(1)
    if len(in_dict) >= 1:                                        # O(1)
        max2 = in_dict.popitem()                                 # O(1)
    else:                                                        # O(1)
        return dict([max1])                                      # O(1)
    if max1[1] < max2[1]:                                        # O(1)
        max1, max2 = max2, max1                                  # O(1)
    if len(in_dict) >= 1:                                        # O(1)
        max3 = in_dict.popitem()                                 # O(1)
    else:                                                        # O(1)
        return dict([max1, max2])                                # O(1)
    if max1[1] < max3[1]:                                        # O(1)
        max1, max2, max3 = max3, max1, max2                      # O(1)
    if max2[1] < max3[1]:                                        # O(1)
        max2, max3 = max3, max2                                  # O(1)
    for el in in_dict:                                           # O(n)
        if in_dict[el] > max1[1]:                                # O(1)
            max1, max2, max3 = (el, in_dict[el]), max1, max2     # O(1)
        elif in_dict[el] > max2[1]:                              # O(1)
            max2, max3 = (el, in_dict[el]), max2                 # O(1)
        elif in_dict[el] > max3[1]:                              # O(1)
            max3 = (el, in_dict[el])                             # O(1)
    return dict([max1, max2, max3])                              # O(1)


if __name__ == "__main__":
    company = [
        {
            "yandex": 1000000,
            "gb": 500000,
            "google": 999999999,
            "mail": 600000,
            "rambler": 100000,
            "avito": 200000
        },

        {
            "yandex": 1000,
            "gb": 500,
            "google": 9999
        },

        {
            "google": 999,
            "yandex": 100
        },

        {
            "yandex": 10
        },

        {

        }
    ]
    for cm in company:
        print(search1(cm))
    print("------------------------------------------------------------------")
    for cm in company:
        print(search2(cm))
# Эффективнее search2 т.к. имеет линейную сложность
