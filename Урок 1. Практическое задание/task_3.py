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
some_company = {'BP': 450000, 'Shell': 800000, 'Rosneft': 350000, 'Lukoil': 11000000, 'Bashneft': 750000}
print(len(some_company))


# сложность O(n log n)

def by_values(item):
    return item[1]                                                      # O(1)


max_job_dollars = {}                                                    # O(1)
i = 0                                                                   # O(1)
for x, m in sorted(some_company.items(), key=by_values, reverse=True):  # O(n log n)
    if i < 3:                                                           # O(len(i)
        max_job_dollars.setdefault(x, m)                                # O(1)
    i = i + 1                                                           # O(1)

print(max_job_dollars)                                                  # O(1)


# второй способ
#сложность: O(n)
try:
    some_company = {'BP': 450000, 'Shell': 800000, 'Rosneft': 350000, 'Lukoil': 11000000, 'Bashneft': 750000}
    print('\nвторое решение:')                                          #O(1)
    print(max(some_company, key=some_company.get))                      #O(n)

    v = list(some_company.values())                                     #O(len(...))
    k = list(some_company.keys())                                       #O(len(...))
    print(k[v.index(max(v[0:3]))])                                      #O(n)

except Exception as e:
    print(e)
