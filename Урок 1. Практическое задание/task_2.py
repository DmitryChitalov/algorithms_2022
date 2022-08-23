"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from collections import deque


# Вариант-1
def searching_min_elem_1(lst_obj):      # итог: линейно-логарифмическая
    return lst_obj.sort()[0]


# Вариант-2
def searching_min_elem_2(lst_obj):      # итог: квадратичная
    for i in range(len(lst_obj)):       # линейная
        flag = False                    # константная
        for j in range(len(lst_obj)):   # линейная
            if lst_obj[i] > lst_obj[j]: # константная
                flag = True             # константная
        if flag is False:               # константная
            min_elem = lst_obj[i]       # константная
    return min_elem                     # константная


# Вариант-3
def searching_min_elem_3(lst_obj):      # итог: линейная
    min_elem = lst_obj[0]               # константная
    for i in range(1, len(lst_obj)):    # линейная
        if lst_obj[i] < min_elem:       # константная
            min_elem = lst_obj[i]       # константная
    return min_elem                     # константная


# Вариант-4
def searching_min_elem_4(lst_obj):             # итог: линейная
    res_lst = deque()                          
    res_lst.append(lst_obj[0])                 # константная
    for i in range(1, len(lst_obj)):           # линейная
        if lst_obj[i] >= res_lst[0]:           # константная
            res_lst.append(lst_obj[i])         # константная
        else:
            res_lst.appendleft(lst_obj[i])     # константная
    return res_lst[0]                          # константная

