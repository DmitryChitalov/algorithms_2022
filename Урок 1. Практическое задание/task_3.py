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

our_dict = {'company_1': 10000, 'company_2': 2000, 'company_3': 5000, 'company_4': 1}


def biggest_value_in_dict(dict):                                                 # O(n)
    new_list = []                                                                # O(1)
    for i in range(3):                                                           # O(1)
        richest_company, biggest_value = list(dict.items())[0]                   # O(1)
        for item in dict:                                                        # O(n)
            if dict[item] > biggest_value:                                       # O(1)
                biggest_value = dict[item]                                       # O(1)
                richest_company = item                                           # O(1)
        new_list.append(richest_company)                                         # O(1)
        dict.pop(richest_company)                                                # O(1)
    return new_list                                                              # O(1)


def biggest_value_in_dict2(dict):                                               # O(n^2)
    mylist = []                                                                 # O(1)
    for item in dict:                                                           # O(n)
        mylist.append((item, dict[item]))                                       # O(1)
    for i in range(len(mylist) - 1):                                            # O(n)
        for j in range(i, len(mylist)):                                         # O(n)
            if mylist[i][1] < mylist[j][1]:                                     # O(1)
                tempvar = mylist[j]                                             # O(1)
                mylist[j] = mylist[i]                                           # O(1)
                mylist[i] = tempvar                                             # O(1)
    return mylist[0][0], mylist[1][0], mylist[2][0]                             # O(1)


print(biggest_value_in_dict2(our_dict))
print(biggest_value_in_dict(our_dict))


"""

Вывод. 
Во втором решении используется вложенный цикл, перебирающий почти все элементы списка. 
Это увеличивает алгоритмическую сложность до квадратичной.
Первое решение эффективнее, так как линейная сложность ниже квадратичной. 

"""


