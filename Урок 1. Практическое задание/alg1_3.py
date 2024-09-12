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

# 1 o(n^2)
from collections import OrderedDict

company = [{
    'Chanel': 160000,
    'Lancome': 58000,
    'Lanvin': 49000,
    'Dolce & Gabbana': 10900,
    'Versace': 800000,
    'Givenchy': 969000,
    'Gucci': 93000}]


def sorted_1(company):
    top_3 = {}
    for i in company:
        for key, value in i.items():
            max_value = top_3.get(key)
            if max_value != None:
                if max_value > value:
                    value = max_value
            top_3.update({key: value})

    s = (OrderedDict(sorted(top_3.items(), key=lambda t: t[1], reverse=True)))
    top_3 = list(s)[0:3]
    print(top_3)


sorted_1(company)

# 2 сложность не знаю
from collections import Counter

company = {
    'Chanel': 160000,
    'Lancome': 58000,
    'Lanvin': 49000,
    'Dolce & Gabbana': 10900,
    'Versace': 800000,
    'Givenchy': 969000,
    'Gucci': 93000}


def sorted_2(company):
    count = Counter(company)
    print(count.most_common(3))


# 3 o(n)
def sorted_3(company):
    company_sort = sorted([(v, k) for (k, v) in company.items()], reverse=True)
    top3_company = [(v) for (k, v) in company_sort[:3]]
    print(top3_company)


sorted_2(company)
sorted_3(company)

# кажется, что 2 вариант решения самый эффективный (но я не уверена)
