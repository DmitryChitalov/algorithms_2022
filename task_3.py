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

profit_company = {'Ozon': 4000000, 'Wildberries': 1000000, 'IKEA': 2000000,
                  'X5 Retail Group': 5000000, 'Evraz': 3000000}
print(len(profit_company))

#########################################################################
"""
Решение 1
Сложность: O(nlogn) - Линейно-логарифмическая
"""


def by_value(item):
    return item[1]                                                       # O(1) - Константная


max_profit = {}                                                          # O(1) - Константная
i = 0                                                                    # O(1) - Константная
for k, v in sorted(profit_company.items(), key=by_value, reverse=True):  # O(n + nlogn) - Линейная
    if i < 3:                                                            # O(len(...)) - Линейная
        max_profit.setdefault(k, v)                                      # O(1) - Константная
    i = i + 1                                                            # O(1) - Константная
print(max_profit)                                                        # O(1) - Константная

#########################################################################
"""
Решение 2
Сложность: O (n^2) - Квадратичная
"""

global max_value                                                         # O(1) - Константная
global key_max_value                                                     # O(1) - Константная

max_profit_2 = {}                                                        # O(1) - Константная
while len(max_profit_2) < 3:                                             # O(n) - Линейная
    max_value = 0                                                        # O(1) - Константная
    for key, value in profit_company.items():                            # O(n) - Линейная
        if max_value < value:                                            # O(len(...)) - Линейная
            max_value = value                                            # O(1) - Константная
            key_max_value = key                                          # O(1) - Константная
    max_value = profit_company.pop(key_max_value)                        # O(1) - Константная
    max_profit_2.setdefault(key_max_value, max_value)                    # O(1) - Константная

print(max_profit_2)

"""
Вывод: Решение 1 эффективнее, так как линейно-логарифмическая сложность выполняется быстрее квадратичной
"""
