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


def check_max_rev1(dict_obj):
    """

    Сложность: O(n).
    """
    start_dict = dict_obj  # O(n)
    final_dict = {}  # O(1)
    for i in range(0, 3):  # O(1)
        max_val = max(start_dict.values())  # O(n)
        final_dict.update({k: v for k, v in start_dict.items() if v == max_val})  # O(n)
        k1 = [k for k, v in start_dict.items() if v == max_val]  # O(n)
        del start_dict[k1[0]]  # O(n)
    return final_dict


def check_max_rev2(dict_obj):
    """

    Сложность: O(n**2).
    """
    start_dict = dict_obj  # O(n)
    for i in range(len(start_dict) - 3):  # O(n)
        min_val = min(start_dict.values())  # O(n)
        k1 = [k for k, v in start_dict.items() if v == min_val]  # O(n)
        del start_dict[k1[0]]  # O(n)
    return start_dict


print(check_max_rev1({"Kavasaki": 1200, "Suzuki": 1500, "Toyota": 12900, "Mazda": 5500, "Nissan": 11000}))
print(check_max_rev2({"Kavasaki": 1200, "Suzuki": 1500, "Toyota": 12900, "Mazda": 5500, "Nissan": 11000}))

"""
Вывод:

наиболее оптимален 1 вариант реализации, так как на массивах данных, размер которых мы не можем предсказать,
сложность алгоритма в первом варианте меньшая, чем во втором
"""