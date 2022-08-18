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


def func1(dict_obj):

    """
    Сложность алгоритма: O((n log n)
    """
    sorted_obj = {}                                              # O(n)
    sorted_keys = sorted(dict_obj, key=dict_obj.get, reverse=1)  # O(n log n)
    idx = 0                                                      # O(1)
    for i in sorted_keys:                                        # O(n)
        sorted_obj[i] = dict_obj[i]                              # O(1)
        idx += 1                                                 # O(1)
        if idx > 2:                                              # O(1)
            break                                                # O(1)
    return sorted_obj                                            # O(1)


def func2(dict_obj):
    """
    Сложность алгоритма: O(n)
    """
    lst_obj = []                                    # O(n)
    for i in dict_obj:                              # O(n)
        lst_obj.append(dict_obj[i])                 # O(1)
    max_income = []                                 # O(n)
    top3_income = {}                                # O(n)
    for i in lst_obj:                               # O(n)
        max_income.append(max(lst_obj))             # O(1)
        lst_obj.remove(max(lst_obj))                # O(1)
    for i in dict_obj:                              # O(n)
        if dict_obj[i] in max_income:               # O(n)?
            top3_income.setdefault(i, dict_obj[i])  # O(1)
    return top3_income                              # O(1)

"""func2 эфективнее за счет использования более простых циклов в отличии от сортировки"""


