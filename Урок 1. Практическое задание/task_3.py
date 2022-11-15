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
companies_list = {'asus': 12853, 'apple': 220859, 'samsung': 3541, 'rzd': 28356,
                  'bork': 259813, 'xiaomi': 14073, 'jeep': 250983, 'nissan': 43350}


def first_method(companies):                                                            # O(n log n)
    sorted_values = sorted(companies.items(), key=lambda item: item[1], reverse=True)   # O(n log n)
    return sorted_values[:3]                                                            # O(n)


def second_method(companies):           # O(n^2)
    lst = []                            # O(1)
    for k in companies:                 # O(n)
        lst.append(companies[k])        # O(1)
    lst.sort(reverse=True)              # O(n log n)
    top3 = []                           # O(1)
    for el in lst[:3]:                  # O(n)
        for k, v in companies.items():  # O(n)
            if v == el:                 # O(1)
                top3.append((k, v))     # O(1)
    return top3                         # O(1)


print(first_method(companies_list))
print(second_method(companies_list))
