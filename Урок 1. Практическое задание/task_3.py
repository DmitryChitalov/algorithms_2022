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

from copy import deepcopy


# сложность O(n**2)
def max_profit_company(companies):
    max_profit_top_sort = [list(companies.items())[0]]  # O(n)
    for company, profit in list(companies.items())[1:]:  # O(n**2)
        for i, el in enumerate(max_profit_top_sort):  # O(n)
            if el[1] < profit:  # O(1)
                max_profit_top_sort.insert(i, (company, profit))  # O(1)
                break  # O(1)
            elif i == len(max_profit_top_sort) - 1:  # O(n)
                max_profit_top_sort.append((company, profit))  # O(1)
                break  # O(1)
    return max_profit_top_sort[:3]  # O(1)


# сложность O(n)
def max_profit_company2(companies):
    max_profit = deepcopy(companies)  # O(n)?
    max_top = []  # O(1)
    for i in range(3):  # O(1)
        max_cur = list(max_profit.items())[0]  # O(n)
        for ind, el in enumerate(max_profit.items()):  # O(n)
            if max_cur[1] < el[1]:  # O(1)
                max_cur = deepcopy(el)  # O(1)
        max_top.append(max_cur)  # O(1)
        max_profit.pop(max_cur[0])  # O(1)
    return max_top


dict_company = {"«Сургутнефтегаз»": 742.9,
                "«Норильский никель»": 263.8,
                "«Транснефть»": 132.4,
                "«Полюс»": 122.6,
                "«Роснефть»": 181,
                "«Атомэнергопром»": 169.1,
                "«Газпром»": 162.4,
                "«Газпром нефть»": 120.6,
                "«Татнефть»": 102.6,
                "«Металлоинвест»": 98.8
                }

print(*max_profit_company(dict_company))
print(*max_profit_company2(dict_company))
