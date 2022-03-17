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
def find_min_1(lst):
    for i in lst:                   # O(n)
        is_min = True               # O(1)
        for j in lst:               # O(n)
            if i > j:               # O(1)
                is_min = False      # O(1)
        if is_min:                  # O(1)
            return i                # O(1)


# O(n)
def find_min_2(lst):
    min_dig = lst[0]                # O(1)
    for i in lst:                   # O(n)
        if min_dig > i:             # O(1)
            min_dig = i             # O(1)
    return min_dig                  # O(1)


lst_ = [randint(1, 99) for i in range(10)]
print(lst_)

print(find_min_1(lst_))
print(find_min_2(lst_))
