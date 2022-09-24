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

companies = {"Tencent Holdings Limited": 560118000000,
             "Microsoft": 8500000000,
             "Apple": 365820000000,
             "Netflix": 29700000000,
             "Amazon": 469800000000,
             }
# O(n^2)

big_revenues = sorted(companies.values())[:3]
result = {}
for i in big_revenues:
    for k in companies.keys(): # O(n)
        if companies[k] == i: # O(1)
            result[k] = companies[k] # O(1)
            break

print(result)

# O(n)

sorted_companies = {}
sorted_keys = sorted(companies, key=companies.get)
for i in sorted_keys[:3]:
    sorted_companies[i] = companies[i]

print(sorted_companies)