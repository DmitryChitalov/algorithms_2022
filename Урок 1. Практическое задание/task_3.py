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
from random import randint


def get_top3_1(in_dict: dict):
    """
    переводим в список и сортируем -   # O(n*log(n))
    """
    in_as_list = list(in_dict.items())  # O(n)
    in_as_list.sort(reverse=True, key=lambda elem: elem[1])  # O(n*log(n))
    return [in_as_list[0], in_as_list[1], in_as_list[2]]  # O(1)


def get_top3_2(in_dict: dict):
    """
    один обход словаря при фиксированной длине списка максимальных элементов - O(n)
    """
    max_dict = {}
    min_dict_val = min(in_dict.values())   # O(n)
    for key, value in in_dict.items():   # O(n)
        if len(max_dict) < 3:   # O(1)
            max_dict[value] = key   # O(1)
            min_dict_val = min(max_dict.keys())   # O(1), т.к. длина <=3
        elif min_dict_val < value:   # O(1)
            max_dict.pop(min_dict_val)   # O(1)
            max_dict[value] = key   # O(1)
            min_dict_val = min(max_dict.keys())   # O(1), т.к. длина <=3
    return max_dict   # O(1)


if __name__ == '__main__':
    company_dict = {'company' + str(i): randint(0, 10000) for i in range(15)}
    print(company_dict)
    print(get_top3_1(company_dict))
    print(get_top3_2(company_dict))

# Второй вариант лучше для списков длиной > 10
