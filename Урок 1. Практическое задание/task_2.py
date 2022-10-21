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


def sorting_func_1(lst):

    """Функция со сложностью O(n^2)"""

    sorted_list = []
    low = lst[0]
    for i in lst:
        if i < low:
            low = i
        sorted_list.append(low)
        for j in sorted_list:
            lower = sorted_list.pop()

    return lower


def sorting_func_2(lst):

    """Функция имеет сложность O(n)"""

    low = lst[0]
    for elem in lst:
        if elem < low:
            low = elem
        # print(low)

    return low


my_list = [randint(0, 1000) for x in range(10000)]
print("Самое малое число в списке: ", sorting_func_2(my_list))
print("Самое малое число в списке: ", sorting_func_1(my_list))

