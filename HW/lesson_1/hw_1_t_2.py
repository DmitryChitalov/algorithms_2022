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

def min_el_1(obj : [list]) -> int: # O(n**2)
    answ = obj[0]       #O(1)
    for i in obj:       #O(n)
        if i < answ:    #O(1)
            for j in obj:#O(n)
                if i<j: #O(1)
                    answ = i #O(1)
    return answ # O(1)


def min_el_2(obj : [list]) -> int: # O(n)
    answ = obj[0] # O(1)
    for i in obj: # O(n)
        if i < answ: # O(1)
            answ = i # O(1)
    return answ # O(1)

obj = sample(range(1,20), 10)
print(obj)
print(min_el_1(obj))
print(min_el_2(obj))
