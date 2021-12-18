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
"""

companies_income = {
    "company_1": 1500000,
    "company_2": 900000,
    "company_3": 3000000,
    "company_4": 50000000,
    "company_5": 70000,
    "company_6": 800000000}


# 1: O(n^2)
list_income = list(companies_income.values())  # O(len(n))
list_income.sort(reverse=True)                 # O(n log n)


def get_key(*args):
    keys = []                                        # O(1)
    for arg in args:                                 # O(n)
        for key, value in companies_income.items():  # O(n^2)
            if arg == value:                         # O(n)
                keys.append(key)                     # O(1)
    return keys


top_companies_income = list_income[0:3]
top_companies = get_key(*top_companies_income)
print(f'Top 3 companies (according to income): {str(top_companies).strip("[]")}')


# 2: O(n log n)
list_income = list(companies_income.values())  # O(len(n))
list_income.sort(reverse=True)                 # O(n log n)


def get_key(val):
    for key, value in companies_income.items():  # O(n)
        if val == value:                         # O(n)
            return key


top_company_1 = get_key(list_income[0])
top_company_2 = get_key(list_income[1])
top_company_3 = get_key(list_income[2])

print(f'Top 3 companies (according to income): {top_company_1}, {top_company_2}, {top_company_3}')

"""
Вывод: предпочтительнее второй вариант, так как он характеризуется линейно-логарифмической сложностью, в отличие от
первого - у него квадратичная сложность. Следовательно, время выполнения второго алгоритма будет меньше.
"""
