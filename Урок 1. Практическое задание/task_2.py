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
import random


def get_min1(in_list: list):
    """ O(n^2) Перебираем все элементы и по очереди сравниваем со всеми"""
    for elem4check in in_list:  # O(n)
        is_minimal = True  # O(1)
        for elem in in_list:  # O(n)
            if elem < elem4check:
                is_minimal = False  # O(1)
        if is_minimal:
            return elem4check  # O(1)


def get_min2(in_list: list):
    """ O(n) Через промежуточную переменную"""
    min_elem = in_list[0]  # O(1)
    for elem in in_list:  # O(n)
        if elem < min_elem:
            min_elem = elem  # O(1)
    return min_elem  # O(1)


if __name__ == '__main__':
    my_list = random.sample(range(10, 100), 10)
    print(my_list)
    print(get_min1(my_list))
    print(get_min2(my_list))
