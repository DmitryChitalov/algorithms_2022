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

company = {'company_a': 90000, 'company_b': 6000, 'company_c': 2000, 'company_d': 50, 'company_e': 40,
           'company_f': 300}


# сложность O(n log n)
def key_value(item):
    return item[1]  # O(1)


max_profit = {}  # O(1)
i = 0  # O(1)
for k, v in sorted(company.items(), key=key_value, reverse=True):  # O(n + n log n)
    if i < 3:  # O(len(i))
        max_profit.setdefault(k, v)  # O(1)
    i = i + 1  # O(1)
print(max_profit)  # O(1)

# Сложность O (n**2)
global max_value  # O(1)
global key_max_value  # O(1)

max_profit_2 = {}  # O(1)
while len(max_profit_2) < 3:  # O(n)
    max_value = 0  # O(1)
    for key, value in company.items():  # O(n)
        if max_value < value:  # O(len(max_value))
            max_value = value  # O(1)
            key_max_value = key  # O(1)
    max_value = company.pop(key_max_value)  # O(1)
    max_profit_2.setdefault(key_max_value, max_value)  # O(1)

print(max_profit_2)

# Победил первый способ так как O(n log n) занимает меньше ресурса чем (n**2).
