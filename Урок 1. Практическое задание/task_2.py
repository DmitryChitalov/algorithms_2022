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
import time
from time import perf_counter
import random
array = [random.randint(-10, 10) for i in range(10)]

def get_min1(n):                                            # O(n**2)
    length = len(n)                                         # O(n)   согласен. понял ошибку
    for i in range(length):                                 # O(n)
        for a in range(length - i - 1):                     # O(n)
            if n[a] > n[a + 1]:                             # O(1)
                n[a], n[a + 1] = n[a + 1], n[a]             # O(1)
    return n[0]                                             # O(1)



def get_min2(n):  # O(n)
    value = n[0]                  # O(1)
    for i in n:                   # O(n)
        if i < value:             # O(1)
            value = i             # O(1)
    return value                  # O(1)



print(array)
start1 = perf_counter()
print(get_min1(array),(perf_counter() - start1))
start2 = perf_counter()
print(get_min2(array),(perf_counter() - start2))
