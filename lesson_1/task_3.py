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
company_profits = {'Яндекс': 5123, 'Газпром': 61200, 'Сбер': 452000, 'Аэрофлот': 8795000, 'Русал': 8973000}

# O(n^2) квадратичная

greatest_profit = sorted(company_profits.values(), reverse=True)[:3] # O(1)
result = {}                                     # O(1)
for i in greatest_profit:                       # O(n)
    for j in company_profits.keys():            # O(n)
        if company_profits[j] == i:             # O(1)
            result[j] = company_profits[j]      # O(1)
            break

print(result)

# O(n) лиейная

sorted_companies = {}                                                               # O(1)
sorted_keys = sorted(company_profits, key=company_profits.get, reverse=True)        # O(1)
for i in sorted_keys[:3]:                                                           # O(n)
    sorted_companies[i] = company_profits[i]                                        # O(1)

print(sorted_companies)
# Вывод: Первый способ выполняется медленнее так как это алгоритм квадратичный, а не линейный как во втором способе.
