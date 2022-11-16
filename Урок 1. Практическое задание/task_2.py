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


def min_n2(data_list):
    min_val = data_list[0]  # O(1)
    for i in range(len(data_list)):  # O(n)
        for j in range(len(data_list)):  # O(n)
            if data_list[i] < data_list[j] and data_list[i] < min_val:  # O(1)
                min_val = data_list[i]  # O(1)
    return min_val  # O(1)


def min_n(data_list):
    min_val = data_list[0]  # O(1)
    for i in range(1, len(data_list)):  # O(n)
        if data_list[i] < min_val:  # O(1)
            min_val = data_list[i]  # O(1)
    return min_val  # O(1)
