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

# Вариант-1
def searching_max_annual_profit(dict_obj):                              # итог: линейно-логарифмическая
    return sorted(dict_obj.items(), key=(lambda item: item[1]))[-3:]    # линейно-логарифмическая


# Вариант-2
def searching_max_annual_profit(dict_obj):         # итог: линейная
    result_list = []
    for i in range(3):                             # константная
        max_profit = 0
        for key, val in dict_obj.items():          # линейная
            if val > max_profit:                    
                max_profit = val
                company = key
        result_list.append((company, max_profit))  # константная
        del dict_obj[company]                      # константная
    return result_list

