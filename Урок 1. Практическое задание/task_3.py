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


def find_company_1(dict): # O(n log n)
    sorted_dict = {}  # O(1)
    new_dict = {}  # O(1)
    sorted_keys = sorted(dict, key=dict.get)  # O(n log n)
    for w in sorted_keys:  # O(n)
        sorted_dict[w] = dict[w]  # O(1)
    i = 1  # O(1)
    while i != 4: # O(3)
        new_dict[list(sorted_dict.keys())[-i]] = sorted_dict.get(list(sorted_dict.keys())[-i]) # O(1)
        i += 1  # O(1)
    return new_dict  # O(1)


def find_company_2(dict):  # O(n)
    i = 0   # O(1)
    new_dict = {}  # O(1)
    max_money = dict.get(list(dict.keys())[0])  # O(1)
    index = 0  # O(1)
    while i != 3:  # O(3)
        max_money = dict.get(list(dict.keys())[0])  # O(1)
        index = 0  # O(1)
        for key, value in dict.items():  # O(n)
            if max_money < value:  # O(1)
                max_money = value  # O(1)
                index = key  # O(1)
        dict.pop(index, max_money)  # O(n)
        new_dict[index] = max_money  # O(n)
        i += 1  # O(n)
    return new_dict  # O(n)








dict_of_comp  = {"Nike": 5000, "Adidas": 3000, "Sber": 50000, "Gasprom": 100000, "Samsung": 10000, "Yandex": 1000}
print(find_company_1(dict_of_comp))
print(find_company_2(dict_of_comp))