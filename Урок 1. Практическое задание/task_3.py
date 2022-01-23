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
companies = {"Firm1": 100000, "Firm2": 140000, "Firm3": 90000, "Firm4": 120000, "Firm5": 50000}


# Вариант 1 Сложность O(n log n)
def sort_v1(companies):
    companieslist = list(companies.items())  # O(1)
    companieslist.sort(key=lambda k: k[1], reverse=True)    # O(n log n)
    for i in range(3):  # O(1)
        if len(companieslist) > i:  # O(1)
            print(companieslist[i][0], ':', companieslist[i][1])    # O(1)


# Вариант 2 Сложность O(n)
def sort_v2(companies):
    for i in range(3):  # O(1)
        _max = 0    # O(1)
        _max_key = ''   # O(1)
        for company in companies:   # O(n)
            if companies[company] > _max:   # O(1)
                _max = companies[company]   # O(1)
                _max_key = company  # O(1)
        print(_max_key, companies.pop(_max_key))    # O(1)
        if len(companies) == 0:     # O(1)
            break   # O(1)


sort_v1(companies)
sort_v2(companies)

"""
Вариант 2 лучше, линейная сложность лучше линейно-логарифмической
"""