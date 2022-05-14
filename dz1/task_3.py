
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

companny_money = {'nike': 12000, 'adidas': 15000, 'apple': 20000, 'sumsung': 18000, 'ozon': 10000, 'marvel': 23000}


def max_money(companny):
    a = sorted(companny.values())[:2:-1]
    result = {}
    for i in a:
        for key, val in companny.items():
            if i == val:
                result[key] = val
    return result


print(max_money(companny_money))

##############################################################################
import heapq


def max_mooney_func(money):
    result = {}
    companny = heapq.nlargest(3, money, key=money.get)
    for key, val in money.items():
        if key in companny:
            result[key] = val
    return result


print(max_mooney_func(companny_money))



