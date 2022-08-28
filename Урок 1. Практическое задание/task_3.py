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

profit_company = {'Nike': 10000, 'Adidas': 7000, 'Puma': 8500, 'TH': 6000, 'UA': 3000}
print(len(profit_company))


# сложность O(n log n)
def by_value(item):
    return item[1]


max_profit = {}
i = 0
for k, v in sorted(profit_company.items(), key=by_value, reverse=True):
    if i < 3:
        max_profit.setdefault(k, v)
    i = i + 1
print(max_profit)

# Сложность O (n**2)
global max_value
global key_max_value

max_profit_2 = {}
while len(max_profit_2) < 3:
    max_value = 0
    for key, value in profit_company.items():
        if max_value < value:
            max_value = value
            key_max_value = key
    max_value = profit_company.pop(key_max_value)
    max_profit_2.setdefault(key_max_value, max_value)

print(max_profit_2)
