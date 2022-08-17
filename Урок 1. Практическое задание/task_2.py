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


def list_min_n1(inner_list):
    """
    Сложность O(n)
    """
    res = max(inner_list)  # O(n)
    for i, val in enumerate(inner_list):  # O(n)
        if val < res:  # O(1)
            res = val  # O(1)
    return res  # O(1)


def list_min_n2(inner_list):
    """
    Сложность O(n*2)
    """
    for val in inner_list:  # O(n)
        for s_val in inner_list:  # O(n)
            if val >= s_val:  # O(1)
                val = s_val  # O(1)
    return val  # O(1)


if __name__ == '__main__':
    test_list = [2, 6, 8, 1, 2, 9, 0, 7]
    print(list_min_n2(test_list))
