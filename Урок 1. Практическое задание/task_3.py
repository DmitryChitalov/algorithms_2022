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

# O(N) линейный
def top_3_1(companies):
    top = {}  # O(1)
    n = 0  # O(1)
    while n < 3:  # O(1)
        prof_max = 0  # O(1)
        comp_max = ''  # O(1)
        for comp, prof in companies.items():  #O(N)
            if prof > prof_max:  # O(1)
                prof_max = prof  # O(1)
                comp_max = comp  # O(1)
        top[n] = {comp_max: prof_max}  # O(1)
        del companies[comp_max]  # O(1)
        n += 1  # O(1)
    return top  # O(1)


list = {'yandex': 2000,
         'gazprom': 500,
         'microsoft': 2300,
         'perecrestok': 5400,
         'rosnano': 10,
         'appel': 2000,
         'biocad': 4030,
         'apteka': 299,
         'hiomi': 569,
         'wacom': 8901,
         'adidas': 4313,
         'acron': 6703}
print(top_3_1(list))


def key_ls(sublist):
    return sublist[1]  # O(1)

# # O(NlogN) линейно-логарифмическая
def top_3_2(companies):
    lst = []  # O(1)
    for key, val in companies.items():  # O(N)
        lst.append([key, val])  # O(1)
    lst.sort(key=key_ls)  # O(NlogN)
    return lst[:-4:-1]  # O(1)


list = {'yandex': 2000,
         'gazprom': 500,
         'microsoft': 2300,
         'perecrestok': 5400,
         'rosnano': 10,
         'appel': 2000,
         'biocad': 4030,
         'apteka': 299,
         'hiomi': 569,
         'wacom': 8901,
         'adidas': 4313,
         'acron': 6703}
print(top_3_2(list))
# Первое решение более эффетивное, т.к. не используется ресурсоемкая сортировка списка и тоько один цикл for.
