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


dict_1 = {'samsung': '7000', 'sony': '3000', 'apple': '4000', 'hp': '5000', 'lenovo': '6000'}  # O(1)
list_1 = []  # O(1)
for items in dict_1.items():  # O(n)
    list_1.append(items[1])  # O(1)
    list_1.sort()  # O(n log n)
print(list_1[:-4:-1])   # O(1)
# Итоговая сложность О(n log n)

list_ = []  # O(1)
for items in dict_1.items():  # O(n)
    for i in items:  # O(n)
        if i.isnumeric():  # O(1)
            list_.append(i)  # O(1)
            list_.sort()  # O(n log n)
print(list_[:-4:-1])  #O(1)
# Итоговая сложность О(n^2)


### Эффективнее будет первое решение, потомучто оно быстрее ###