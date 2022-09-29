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

from random import randint


def search_min(val):
    """
    O(n^2).
    """
    for el in val:               # O(n)
        is_min = True            # O(1)
        for elem in val:         # O(n)
            if elem < el:        # O(1)
                is_min = False   # O(1)
        if is_min:               # O(1)
            return el
    return 0


def find_min_2(val):
    """
    O(n).
    """
    min_value = val[0]          # O(1)
    for elem in val:            # O(n)
        if min_value > elem:    # O(1)
            min_value = elem    # O(1)
    return min_value            # O(1)


my_list = [randint(0, 20) for i in range(20)]
print(my_list)
print(search_min(my_list))
print(search_min_2(my_list))