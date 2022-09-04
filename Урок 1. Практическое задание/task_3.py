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

Companies = {'Toyota': 2000,
             'Opel': 2500,
             'Nissan': 6000,
             'BMW': 5000,
             'Mazda': 4000}

# Вариант 1 - O(n log n)

def max_profit(dict_obj):
    sorted_dict_obj = sorted(dict_obj.items(), key=lambda x: x[1], reverse=True)
    final_lst = sorted_dict_obj[:3]
    return final_lst

# Вариант 2 - O(n)

def max_profit_2(dict_obj):
    final_dict = {}
    dict_obj_copy = dict(dict_obj)
    for i in range(3):
        max_value = max(dict_obj_copy.items(), key=lambda elem: elem[1])
        del dict_obj_copy[max_value[0]]
        final_dict[max_value[0]] = max_value[1]
    return final_dict


# Вариант 3

def max_profit_3(dict_obj):
    lst = list(dict_obj.items())
    for i in lst:
        idx = lst.index(i)
        max_value = lst[0]
        if max_value[1] < lst[idx+1][1]:
            max_value = lst[idx+1][1]
            continue
        return max_value

#print(max_profit(Companies))
#print(max_profit_2(Companies))
print(max_profit_3(Companies))


