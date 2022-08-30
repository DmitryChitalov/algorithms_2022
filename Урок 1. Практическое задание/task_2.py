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

def min_num_sqr(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[minimum], lst[i] = lst[i], lst[minimum]
    return lst[0]

def min_num_line(lst):
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i
    return min_num


lst = [randint(0, 100) for i in range(10)]
print(lst)
print(min_num_sqr(lst))
print(min_num_line(lst))