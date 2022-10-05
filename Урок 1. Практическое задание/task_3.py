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

companys_data = {'A': 1, 'B': 5, 'C': 15, 'D': 25, 'E': 10, 'F': 20}


# Сложность O(n log n)
def max_val_1(c_d):
    three_comp = {}  # O(1)
    sort_comp_data = dict(sorted(c_d.items(), reverse=True, key=lambda x: x[1]))  # O(n log n)
    i = 0  # O(1)
    for key, value in sort_comp_data.items():  # O(n)
        if i < 3:  # O(1)
            three_comp.setdefault(key, value)  # O(n)
        i += 1  # O(1)
    return three_comp  # O(1)


# Сложность O(n) линейная
def max_val_2(c_d):
    three_comp = {}  # O(1)
    while len(three_comp) < 3:  # O(1)
        mval = 0  # O(1)
        mkey = 0  # O(1)
        for key, val in c_d.items():  # O(n)
            if mval < val:  # O(1)
                mval = val  # O(1)
                mkey = key  # O(1)
        c_d.pop(mkey)  # O(1)
        three_comp.setdefault(mkey, mval)  # O(1)
    return three_comp  # O(1)


print(max_val_1(companys_data))
print(max_val_2(companys_data))


# первое решение лучше потому что сложность квадратичной функции влечет за собой большее количество операций.
