"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


list_num = [8, 4, 76, 9, 55]


def quadratic(lst):
    """ O(n^2) """
    for i in lst:
        if i < lst[0]:
            lst.insert(0, lst[lst.index(i)])
    return lst[0]


def linear(lst):
    """ O(n) """
    res = lst[0]
    for i in lst:
        if i < res:
            res = i
    return res


print(quadratic(list_num))
print(linear(list_num))
