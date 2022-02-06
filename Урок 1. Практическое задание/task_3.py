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

company_balance = {'WB': 1000, 'OZON': 4000, 'YANDEX': 2000, 'GOOGLE': 5000, 'AMAZON': 3000}
print(len(company_balance))

# Первый способ:
# сложность O(n log n)


def best_balance(item):
    return item[1]                                                          # O(1)


max_profit = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(company_balance.items(), key=best_balance, reverse=True):     # O(n + n log n)
    if i < 3:                                                               # O(len(i)
        max_profit.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)
print(max_profit)                                                           # O(1)

# 2 способ
sorted_companies = sorted(company_balance, key=company_balance.get, reverse=True)[:3]    # O(n*log n)
for i in sorted_companies:                                                               # O(1)
    print(i, ':', company_balance.get(i))                                                # O(1)

# Эффективнее 2 способ

