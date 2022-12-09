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

corporations = {'Intel': 5000, 'Google': 7000, 'Yandex': 3000,
                'Microsoft': 10000, 'Amazon': 1000} # 1 O(n^2)
sorted_values = sorted(corporations.values(), reverse=True)  # O(n log n)
sorted_corp = {}  # O(1)
for value in sorted_values:  # O(n)
    for key in corporations.keys():  # O(n)
        if corporations[key] == value:  # O(1)
            sorted_corp[key] = corporations[key]  # O(1)
print(dict(list(sorted_corp.items())[:3]))  # O(n) + O(n) + O(1)

# Var 2 O(n log n)
top_3_corporations = (sorted(corporations.items(),
key=lambda items: items[1], reverse=True))[:3]  # O(n log n), срез O(1)
print(top_3_corporations)  # O(1)
