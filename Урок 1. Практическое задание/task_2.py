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

""" Алгоритм: 1 
    Сложность: O(n^2) """


def check_min_1(elements):
    min_value = None  # O(1)
    for el in elements:  # O(n)
        if min_value not in elements:  # O(n)
            min_value = el  # O(1)
        elif el < min_value:  # O(1)
            min_value = el  # O(1)
    return min_value  # O(1)


""" Алгоритм: 2 
    Сложность: O(n) """


def check_min_2(elements):
    min_value = elements[0]  # O(1)
    for el in elements:  # O(n)
        if el < min_value:  # O(1)
            min_value = el  # O(1)
    return min_value  # O(1)


my_list = [56, 23, 18, 6, 256, 12, 88, 1, 48, -8, 654, 222, 12]

print(check_min_1(my_list))
print(check_min_2(my_list))
