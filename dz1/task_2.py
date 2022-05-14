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


def min_num(num):
    result = 0
    for i in range(len(num)):  # O(N)
        if result > num[i]:    # O(1)
            result = num[i]    # O(1)
    return result


num = [randint(-100, 100) for i in range(30)]
print(min_num(num))


def find_min(arr, min_=None):
    if min_ is None:                     # O(1)
        min_ = arr.pop()                 # O(1)
    current = arr.pop()                  # O(1)
    if current < min_:                   # O(1)
        min_ = current                   # O(1)
    if arr:
        return find_min(arr, min_)
    return min_

print(find_min(num))








