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

# Решение № 1
# СЛОЖНОСТЬ O(n^2)
def max_profit(dict):
    profit = list(dict.values())           # O(n)
    profit.sort(reverse=True)              # O (n log n)
    res = profit[:3]                        # O(3)
    comp_names = []                         # O(1)
    for i in res:                           # O(n^2)
        for key, val in dict.items():       # O(n)
            if val == i:
                comp_names.append(key)      # O(1)

    return comp_names                       # O(1)

comp = {
    'comp1': 2000,
    'comp2': 2500,
    'comp3': 5000,
    'comp4': 10000,
    'comp5': 10
}

# Решение № 2
# СЛОЖНОСТЬ O (n log n)
def max_profit_2(names, values):
    new_val = sorted(values, reverse=True)[:3]     # O (n log n)
    max_profit_comp = []                           # O(1)
    for i in new_val:                              # O(n)
        max_profit_comp.append(names[values.index(i)])   # O(1)
        values.pop(values.index(i))                # O(n)

    return max_profit_comp                         # O(1)

comp_names = ['comp1', 'comp2', 'comp3', 'comp4', 'comp5']
profits = [1000, 500, 3000, 200, 10000]
# print(max_profit_2(comp_names, profits))


# Решение № 3
# СЛОЖНОСТЬ O (n log n)
def max_profit_3(dict):
    new_dict = sorted(dict, key=dict.get, reverse=True)[:3]  # O(n log n)
    return new_dict

# print(max_profit_3(comp))

# ВЫВОД: решение №3 считаю наименее сложным и наиболее лаконичным,
# без циклов и с минимальным количеством операций присваивания
