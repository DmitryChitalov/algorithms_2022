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

company = {'AAPL': 110000, 'GOOG': 25000, 'FTSE': 690000, 'HSI': 782000, 'S&P': 4123000, 'DOWJ': 5480000,
           'YHOO': 745200}


# 1 вариант. Сложность O(n log n)

dict_list = []
for key, value in company.items():  # O(n)
    temp = (key, value)  # O(1)
    dict_list.append(temp)  # O(1)


def sort_key(e):
    return e[1]  # O(1)


top_3_1 = sorted(dict_list, key=sort_key, reverse=True)[:3]  # O(n log n)

print(top_3_1)


# 2 вариант. Сложность O(n)

global max_value                     # O(1)
global key_max_value                  # O(1)

top_3_2 = {}                     # O(1)
while len(top_3_2) < 3:          # O(1)
    max_value = 0                   # O(1)
    for key, value in company.items():     # O(n)
        if max_value < value:       # O(1)
            max_value = value       # O(1)
            key_max_value = key        # O(1)
    max_value = company.pop(key_max_value)      # O(1)
    top_3_2.setdefault(key_max_value, max_value)    # O(1)

print(top_3_2)

#  Второе решение эффективнее, т.к. O(n) выполняеется быстрее, чем O(n log n).