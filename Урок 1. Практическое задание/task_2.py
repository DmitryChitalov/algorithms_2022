from random import randint

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


def min_in_list(lst):
    """
    Поиск минимального значения в списки со сложностью O(n^2)
    :param lst: список чисел
    :return: минимальное число
    """
    for num_one in lst:  # O(n)
        is_min = True  # O(1)
        for num_two in lst:  # O(n)
            if num_one > num_two:  # O(1)
                is_min = False  # O(1)
        if is_min:  # O(1)
            return num_one  # O(1)


def min_in_list_on(lst):
    """
    Поиск минимального значения в списки со сложностью O(n)
    :param lst: список чисел
    :return: минимальное число
    """
    min_num = lst[0]  # O(1)
    for num in lst:  # O(n)
        if num < min_num:  # O(1)
            min_num = num  # O(1)
    return min_num  # O(1)


if __name__ == '__main__':
    lst_number = [randint(0, 50) for i in range(15)]
    print(lst_number)
    print(min_in_list(lst_number))
    print(min_in_list_on(lst_number))
