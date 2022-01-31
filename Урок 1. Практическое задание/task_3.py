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

#O(n log(n)) максимальная сложность
my_dict = {'intel': 200000, 'amd': 150000, 'xerox': 270000, 'nvidia': 450000, 'hp': 382000}  #O(k)
sort_dict = sorted(my_dict, key=my_dict.get) #O(n log(n))
print(sort_dict[:3:]) #O(n)

dict1 = {'intel': 200000, 'amd': 150000, 'xerox': 270000, 'nvidia': 450000, 'hp': 382000} #O(k)
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1]) #O(n**2)
print(sorted_tuples[:3:]) #O(n)
