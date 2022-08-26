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
from random import sample


def min_1(lst_1):  # O(n^2)
    min_number = lst_1[0]  # O(1)
    for i in range(len(lst_1)):  # O(n)
        for _ in lst_1:  # O(n)
            if min_number > lst_1[i]:  # O(1)
                min_number = lst_1[i]  # O(1)
    return min_number  # O(1)


def min_2(lst_1):  # O(n)
    min_number = lst_1[0]  # O(1)
    for i in lst_1:  # O(n)
        if i < min_number:  # O(1)
            min_number = i  # O(1)
    return min_number  # O(1)


for j in (50, 500, 1000, 5000, 10000):
    lst_1 = sample(range(-100000, 100000), j)

print(min_1(lst_1))
print(min_2(lst_1))
