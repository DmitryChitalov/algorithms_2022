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
info_table = {
    'Apple': 3000,
    'IBM': 10,
    'Tesla': 500,
    'Evergrind': -500,
    'Rosneft': 5,
    'Gazprom': 25
}
#Исправлена сложность
# Второй вариант алгоритма оптимальный, так как с найименьшей сложностью

def way_max_1(info_table):
    # Сложность: Т(n) =  O(n log n)
    copy_table = [[company, revenue] for company, revenue in info_table.copy().items()]  # O(n)
    copy_table.sort(key=lambda x: x[-1], reverse = True)                                 # O(n log n)

    max_revenues = {company: revenue for company, revenue in copy_table[0:3]}            # O(1)
    return max_revenues                                                                  # O(1)


def way_max_2(info_table):
    # Сложность: Т(n) =  O(n)
    copy_table = info_table.copy()                                          # O(n)
    max_revenues = {}                                                       # O(1)
    for i in range(3):                                                      # O(1)
        company, revenue = max(copy_table.items(), key = lambda x: x[1])    # O(n)
        del copy_table[company]                                             # O(1)
        max_revenues.update({company: revenue})                             # O(1)
    return max_revenues


# def way_max_3(info_table):
#     for key, val in sorted(info_table.items(), key= lambda x: x[1]):
#         info_table_sorted = {k: info_table[k] for k in sorted(info_table, key=info_table.get, reverse=True)}

print(way_max_1(info_table))
print(way_max_2(info_table))