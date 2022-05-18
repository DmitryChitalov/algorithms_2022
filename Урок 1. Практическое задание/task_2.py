"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.
"""

def list_variant_1(user_list):

    for i in range(len(user_list)):
        for j in range(len(user_list)):
            if user_list[i] < user_list[j]:
                us_el = user_list[i]
            else:
                us_el = user_list[i]

    return us_el

"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""

def list_variant_2(user_list):

    us_el = user_list[0]  # O(1)
    for i in range(len(user_list)):  # O(n)
        if user_list[i] < us_ell:  # O(1)
            us_el = user_list[i]  # O(1)
    return us_el  # O(1)

"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
