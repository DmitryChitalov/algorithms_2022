"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Алгоритм 1.   # Квадратичная сложность : О(n**2)


def function_of_determining_the_minimum_value_1(lst):  # Квадратичная сложность : О(n**2)
    for member in lst:
        this_element_is_minimal = True
        for element in lst:
            if element < member:
                this_element_is_minimal = False
        if this_element_is_minimal:
            return member


first_list = [45, 54645, 25324, -875678, 2342423, 1231, 4, -5, -1000000, 45646, -3453, 3453, 2344, 123, -345345, 456]


print(function_of_determining_the_minimum_value_1(first_list))


# Алгоритм 2.   # Линейная сложность : О(n**2)


def function_of_determining_the_minimum_value_2(lst):  # Линейная сложность : О(n**2)
    min_member_of_list = lst[0]
    for member in lst[1:]:
        if member < min_member_of_list:
            min_member_of_list = member
    return min_member_of_list


second_list = [45, 546454, 25324, -7875678, 2342423, 1231, 4, -5, -10000,
               45646, -63453, 3453, 2344, 12456453, -345345, 456,475734636]


print(function_of_determining_the_minimum_value_2(second_list))

