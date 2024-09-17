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

llist = [random.randint(0, 100) for i in range(20)]


def one(ll):  # O(N**2)
    self_ll = list(ll)  # O(1)
    while True:  # O(N)
        try:
            if self_ll[0] < self_ll[1]:  # O(1 + 1) = O(1)
                self_ll.remove(self_ll[1])  # O(N)
            else:
                self_ll.remove(self_ll[0])  # O(N)
        except:
            return self_ll[0]  # O(1)
            break  # O(1)


def two(ll):  # O(N)
    self_ll = list(ll)  # O(1)
    while True:  # O(N)
        try:
            if self_ll[0] < self_ll[1]:  # O(1 + 1) = O(1)
                self_ll.pop(1)  # O(1)
            else:
                self_ll.pop(0)  # O(1)
        except:
            return self_ll[0]  # O(1)
            break  # O(1)


print(llist)
print(one(llist))
print(two(llist))
