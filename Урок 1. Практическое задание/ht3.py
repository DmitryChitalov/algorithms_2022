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

# Метод 1, общая сложность O(NlogN)
comp_dict = {
    'first': 10000,
    'second': 6000,
    'third': 13000,
    'fourth': 29000,
    'fifth': 4000
} # O(1)
values_list = [] # O(1)
for val in comp_dict.values(): # O(N)
    values_list.append(val) # O(1)
values_list.sort() # NlogN
values_list = values_list[-3:] # O(1)
for key in comp_dict: # O(N)
    if comp_dict[key] in values_list: # O(1)
        print(comp_dict[key]) # O(1)

# Метод 2, общая сложность O(N)
comp_dict = {
    'first': 10000,
    'second': 6000,
    'third': 13000,
    'fourth': 29000,
    'fifth': 4000
} # O(1)
values_list_1 = [] # O(1)
values_list_2 = [] # O(1)
for val in comp_dict.values(): # O(N)
    values_list_1.append(val) # O(1)

for i in range(3): #O(1)
    a = max(values_list_1) #O(N)
    values_list_2.append(a) #O(N)
    values_list_1.remove(a) # O(N)

for key in comp_dict: # O(N)
    if comp_dict[key] in values_list_2: # O(1)
        print(comp_dict[key]) # O(1)

