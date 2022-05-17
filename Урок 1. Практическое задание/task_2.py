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
from random import shuffle


def min_n2(lst_obj):
    # Сложность O(N^2)
    result = lst_obj[0]  # O(1)
    for i in lst_obj:  # O(N)
        result_of_iteration = i  # O(1)
        for j in lst_obj:  # O(N)
            if j < i:  # O(1)
                result_of_iteration = j  # O(1)
        if result_of_iteration < result:  # O(1)
            result = result_of_iteration  # O(1)
    return result  # O(1)


def min_n(lst_obj):
    # Сложность: O(N):
    result = lst_obj[0]  # O(1)
    for i in lst_obj:  # O(N)
        if i < result:  # O(1)
            result = i  # O(1)
    return result


list_test = list(range(1, 10000))  # Последовательность чисел от 1 до 10000
shuffle(list_test)  # Перемешиваем последовательность
print(min_n(list_test))
print(min_n2(list_test))
