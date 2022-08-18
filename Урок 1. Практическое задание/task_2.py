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


def search_minimum_element(lst_obj):       # итог: квадратичная
    for i in range(len(lst_obj)):          # линейная
        flag = False                       # константная
        for j in range(len(lst_obj)):      # линейная
            if lst_obj[i] > lst_obj[j]:    # константная
                flag = True                # константная
        if flag is False:                  # константная
            minimum_element = lst_obj[i]   # константная
    return minimum_element                 # константная


def search_minimum_element_2(lst_obj):      # итог: линейная
    minimum_element = lst_obj[0]            # константная
    for i in range(1, len(lst_obj)):        # линейная
        if lst_obj[i] < minimum_element:    # константная
            minimum_element = lst_obj[i]    # константная
    return minimum_element                  # константная

