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

# Сложность: O(n^2)

companies = {
    'company_1': 1000005,
    'company_2': 345873,
    'company_3': 4000150,
    'company_4': 105000,
    'company_5': 4356791,
    'company_6': 113459}

list_income = list(companies.values())           # O(n)
list_income.sort(reverse=True)                   # O(n log n)


def get_key(*args):
    keys = []                                        # O(1)
    for arg in args:                                 # O(n)
        for key, value in companies.items():         # O(n)
            if arg == value:                         # O(1)
                keys.append(key)                     # O(1)
    return keys

best_companies = list_income[0:3]
top_companies = get_key(*best_companies)
print(top_companies)


# Сложность: O(n log n)

list_income = list(companies.values())         # O(n)
list_income.sort(reverse=True)                 # O(n log n)


def get_key(val):
    for key, value in companies.items():         # O(n)
        if val == value:                         # O(1)
            return key

top_1, top_2, top_3 = get_key(list_income[0]), get_key(list_income[1]), get_key(list_income[2])

print(top_1, top_2, top_3, sep=', ')

# Вывод: эффективнее будет второй вариант решения, так как линейно-логарифмическая сложность требует меньше времени на выполнение, чем квадратичная.

