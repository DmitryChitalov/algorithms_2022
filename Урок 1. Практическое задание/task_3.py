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

def top_3_search_1(dict):
    # # O(N log N) - линейно-логарифмическая
    import operator # O(1)
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1)) # O(N log N)
    return list(sorted_dict)[(len(sorted_dict)-3):len(sorted_dict)] # O(N)

def top_3_search_2(dict):
    # O(Nˆ2) -квадратичная
    sorted_dict = {} # O(1)
    sorted_values = sorted(dict.values()) # O(N log N)
    sorted_keys = sorted(dict, key=dict.get) # O(N log N)
    for i in sorted_values:  # O(N)
        for k in dict.keys(): # O(N)
            if dict[k] == i: # O(1)
                sorted_dict[k] = dict[k] # O(1)
                break # O(1)
    return (list(sorted_dict.items())[(len(sorted_dict)-3):len(sorted_dict)]) # O(1)

def top_3_search_3(dict):
    # O(N) - линейная
    sorted_list = {} # O(1)
    for _ in range(3):  # O(1)
        max_value = max(dict.items(), key=lambda item: item[1])  # O(N)
        sorted_list[max_value[0]] = max_value[1] # O(1)
        dict.pop(max_value[0]) # O(1)
    return sorted_list # O(1)

profit_dict={'Apple':57411, 'Saudi Aramco':49287, 'SoftBank':47053, 'ICB China':45783, 'Microsoft':44281, 'Alphabet':40269, 'Facebook': 29146, 'JPMorgan Chase & Co.':29131, 'Alibaba Group Holding':22224, 'Samsung Electronics':22116 }
print(top_3_search_1(profit_dict))
print(top_3_search_2(profit_dict))
print(top_3_search_3(profit_dict))

# Последний алгорит имеет наименьшую сложность и меньше действий по сравнению остальными алгоритмами. Встроенные функции со словарями обеспечивают наименьшую сложность выполнения алгоритма.