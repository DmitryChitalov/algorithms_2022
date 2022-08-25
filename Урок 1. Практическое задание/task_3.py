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


def find_top_three_1(company_data):
    """
    Нахождение в словаре, по значению, трех наибольших элементов - сложность O(n^2)
    :param company_data: словарь
    :return: словарь с 3 наибольшими элементами
    """
    list_from_dict = list(company_data.items())  # O(n)
    for i in range(len(list_from_dict)):  # O(n)
        lowest_index = i  # O(1)
        for j in range(i + 1, len(list_from_dict)):  # O(N)
            if list_from_dict[j][1] > list_from_dict[lowest_index][1]:  # O(1)
                lowest_index = j  # O(1)
        list_from_dict[i], list_from_dict[lowest_index] = \
            list_from_dict[lowest_index], list_from_dict[i]  # O(1)
    return dict(list_from_dict[0:3])  # O(1)


def find_top_three_2(company_data):
    """
    Нахождение в словаре, по значению, трех наибольших элементов - сложность O(n log n)
    :param company_data: словарь
    :return: словарь с 3 наибольшими элементами
    """
    sorted_tuple_data = sorted(company_data.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    return dict(sorted_tuple_data[:3])  # O(1)


def find_top_three_3(company_data):
    """
    Нахождение в словаре, по значению, трех наибольших элементов - сложность O(n)
    :param company_data: словарь
    :return: словарь с 3 наибольшими элементами
    """
    res_max_dict = {}  # O(1)
    dict_copy = company_data.copy()  # O(n)
    while len(res_max_dict) < 3:  # O(1)
        maximum_el = max(dict_copy.items(), key=lambda k_v: k_v[1])  # O(n)
        del dict_copy[maximum_el[0]]  # O(1)
        res_max_dict[maximum_el[0]] = maximum_el[1]  # O(1)
    return res_max_dict  # O(1)


if __name__ == '__main__':
    company_profit = {
        'google': 150000,
        'lukhoil': 110000,
        'dixi': 90000,
        'appel': 175000,
        'gmk': 95000,
        'shell': 117000,
        'pochta': 50000,
        'spar': 87000,
        'intel': 101000,
        'toyota': 99000,
        'bmw': 56000,
        'footband': 48000,
        'metro': 69000,
        'ashan': 74000,
        'lada': 88000
    }

    print(find_top_three_1(company_profit))
    print(find_top_three_2(company_profit))
    print(find_top_three_3(company_profit))

    """
    Лучшим по сложности используя О нотацию будет третий вариант, т.к. 
    имеет минимальную вычислительную 
    сложность, так как не использует вложенные циклы и сортировку
    """
