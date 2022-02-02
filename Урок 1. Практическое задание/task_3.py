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

company_revenue = {'Apple inc': 109, 'Microsoft': 69, 'Meta Platforms': 32, 'Alphabet': 38,
                   'Amazon': 22, 'Alibaba Group': 14, 'Dell Technologies': 5, 'IBM': 4}


# Вариант №1: O(n log n)
def answer_first(company):
    sort_dict = {k: v for k, v in sorted(company.items(), key=lambda item: item[1])}  # O(n log n)
    max_revenue = {}  # O(1)
    for i in range(3):  # O(1)
        tmp_lst = list(sort_dict.popitem())  # O(n)
        max_revenue[tmp_lst[0]] = tmp_lst[1]  # O(1)
    return max_revenue  # O(1)


# Способ №2: O(n)
def answer_two(company):
    list_dict = dict(company.items())  # O(n)
    max_revenue = {}  # O(1)
    for i in range(3):  # O(1)
        maximum_revenue = max(list_dict.items(), key=lambda x: x[1])  # O(n)
        del list_dict[maximum_revenue[0]]  # O(n)
        max_revenue[maximum_revenue[0]] = maximum_revenue[1]  # O(1)
    return max_revenue  # O(1)


print("answer_first", answer_first(company_revenue))
print("answer_two", answer_two(company_revenue))
