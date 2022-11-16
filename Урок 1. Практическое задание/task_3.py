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


def find_company(company_list):  # O(n log n)
    sorted_comp = sorted(company_list, key=company_list.get, reverse=True)  # O(n log n)
    return sorted_comp[:3]  # O(1)


def find_company_slow(company_list):  # O(n^2)
    values = sorted(company_list.values(), reverse=True)  # O(n)
    top_list = []  # O(1)
    for val in values[:3]:  # O(1)
        for key, value in company_list.items():  # O(n)
            if val == value:  # O(1)
                top_list.append(key)  # O(1)

    return top_list  # O(1)


list_company = {"Лукойл": 1000, "Сургутнефтегаз": 10000, "Магнит": 1, "СБЕР": 89999, "ГАЗПРОМ": 20984, "ВТБ": -1}
print(find_company(list_company))
print(find_company_slow(list_company))

# решение 1 предпочтительней так как имеет логарифмическую но не квадратичную скорость