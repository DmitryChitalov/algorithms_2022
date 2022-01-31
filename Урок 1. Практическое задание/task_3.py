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
"Первое решение"
" Итогова сложность O(n log n) "
company = {
    'Fifa': 2000000,
    'Lima': 10000000,
    'Myzla': 20000,
    'vnykvov': 100,
    'metallov': 100000,
    'gazetaru': 1
}
x = {}
sorted_tuple = sorted(company.items(), key=lambda x: x[1])  # O(n log n) + O(1) + O(len()))
print(dict(sorted_tuple[-1:-4:-1]))                         # O(b - a)

"Второе решение "
"Итоговая сложнасть O(k*n) "
company = {
    'Fifa': 2000000,
    'Lima': 10000000,
    'Myzla': 20000,
    'vnykvov': 100,
    'metallov': 100000,
    'gazetaru': 1
}
x = {}                                                       # O(1)
for i in range(3):                                           # O(3)
    z = (max(company.values()))                              # O(n)
    x[max(company, key=company.get)] = z                     # O(k * n)
    company.pop(max(company, key=company.get))               # O(n)
print(x)                                                     # O(1)

"Второе решение лучше в плане сложности алгоритма, можно задать выборку на большее кол-во итераций" \
"Перове решение лаконичнее, но задача решена под определенное условие," \
" не такая универсальная и проигрывает по сложности"


