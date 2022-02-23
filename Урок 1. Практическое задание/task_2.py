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
# O(n^2)
def list_min1(lst):
    for i in lst:
        is_min = 1
        for k in lst:
            if i > k:
                is_min = 0
        if is_min:
            return i

# O(n)
from random import randint
def list_min2(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

lst1 = [randint(0, 100) for i in range(20)]
print(lst1)
print(list_min1(lst1))
print(list_min2(lst1))
