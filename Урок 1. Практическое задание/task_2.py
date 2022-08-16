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


# O(n^2)
def find_min_n_square(lst):
    for i in lst:  # O(n)
        mini = True
        for j in lst:  # O(n)
            if i > j:  # O(1)
                mini = False
        if mini:
            return i  # O(1)


# O(n)
def find_min_n(lst):
    mini = lst[0]
    for item in lst:  # O(n)
        if item < mini:  # O(1)
            mini = item

    return mini  # O(1)


lst = [randint(0, 50) for _ in range(30)]
print(lst)
print(find_min_n_square(lst))
