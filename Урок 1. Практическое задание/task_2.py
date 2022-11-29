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

my_list = [1, 2, -5, 4, 100, 0]


def find_min_1(lst: list):
    res = lst[0]  # O(1)
    for cur_el in lst:  # O(n)
        for check in lst:  # O(n)
            flag = False  # O(1)
            if cur_el < check:  # O(1)
                flag = True  # O(1)
            if flag and cur_el < res:  # O(1)
                res = cur_el  # O(1)
    return res  # O(1)


def find_min_2(lst: list):
    res = lst[0]  # O(1)
    for el in lst:  # O(n)
        if el < res:  # O(1)
            res = el  # O(1)
    return res  # O(1)


print(find_min_1(my_list))
print(find_min_2(my_list))
