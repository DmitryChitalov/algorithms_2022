"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

"""

from random import randint


def list_minimal_one(lst):
    for i in lst:
        minimal = True
        for x in lst:
            if i > x:
                minimal = False
        if minimal:
            return i


"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""


def list_minimal_two(lst):
    minimal_val = lst[0]
    for i in lst:
        if i < minimal_val:
            minimal_val = i
    return minimal_val


lst1 = [randint(0, 100) for i in range(25)]
print(lst1)
print(list_minimal_one(lst1))
print(list_minimal_two(lst1))

"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
