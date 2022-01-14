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

##############################################################################

def check_max_profit_1(dct_obj):
    """Функция должна обеспечивать поиск трех компаний с наибольшей годовой прибылью.

    Алгоритм 1:
    Сложность: O(n**2).
    """
    sorted_dict = {}                                      # O(len(n))
    for i in sorted(dct_obj.values(), reverse=True)[:3]:  # O(n + n log n)
        for k in dct_obj:                                 # O(n)
            if dct_obj[k] == i:                           # O(1)
                sorted_dict[k] = dct_obj[k]               # O(1)
    return sorted_dict                                    # O(1)


##############################################################################
def check_max_profit_2(dct_obj):
    """Функция должна обеспечивать поиск трех компаний с наибольшей годовой прибылью.

    Алгоритм 2:
    Сложность: O(n log n).
    """
    sorted_dict = {
        k: dct_obj[k] for k in sorted(dct_obj, key=dct_obj.get, reverse=True)[:3]
    }                       # O(n + n log n)
    return sorted_dict      # O(1)



profit_dict = {'Aaa': 10000, 'Bbb': 20000, 'Ccc': 30000, 'Ddd': 40000, 'Fff': 50000,
               'Ggg': 60000, 'Vvv': 70000, 'Qqq': 80000, 'Www': 90000, 'Zzz': 1000}

print(check_max_profit_1(profit_dict))
print(check_max_profit_2(profit_dict))
