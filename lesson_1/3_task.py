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

companies = {"VTB": 12541, "Gazprom": 12521, "Sberbank": 34533, "Tinkoff": 35253, "Yandex": 1254}


#   Сложность: O(n log n)
def top_three_profit(comp: dict):
    sort_comp = sorted(comp, key=comp.get, reverse=True)  # O(n log n)
    return sort_comp[0:3]  # O(1)


# Сложность: O(n)
def top_three_profit_sec(comp: dict):
    profit_list = list(comp.values())  # O(n)
    sort_profit_list = []  # O(1)
    new_comp = {}  # O(1)
    while profit_list:
        maximum = profit_list[0]  # O(1)
        for el in profit_list:  # O(n)
            if el > maximum:
                maximum = el  # O(1)
        sort_profit_list.append(maximum)  # O(1)
        profit_list.remove(maximum)  # O(n)
    for val in sort_profit_list[0:3]:  # O(1)
        for key, value in comp.items():  # O(n)
            if val == value:
                new_comp[key] = val  # O(1)
    return new_comp  # O(1)


print(top_three_profit(companies))
print(top_three_profit_sec(companies))
