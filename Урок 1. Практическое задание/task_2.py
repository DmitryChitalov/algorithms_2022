"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.
"""

lst = [5, 8, 10, 3, 18, 4, 75]

"""
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
"""


def min_val_v1(list):
    for i in list:
        element = True
        for j in list:
            if i > j:
                element = False
        if element:
            return i


print(min_val_v1(lst))

"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""


def min_val_v2(list):
    first_element = list.pop()
    for i in list:
        if i < first_element:
            first_element = i
    return first_element


print(min_val_v2(lst))

"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
