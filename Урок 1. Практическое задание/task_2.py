"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# O(n) - линейная
def min_one(el):
    n_min = el[0]
    for i in el:
        if i < n_min:
            n_min = i
    return n_min


# O(n^2) - квадратичная
def min_two(el):
    for i in el:
        n_min = True
        for j in el:
            if i > j:
                n_min = False
        if n_min:
            return i


numb = [3, 5, 7, 9, 1, 0, -1]
print(min_one(numb))
print(min_two(numb))

"""O(n^2) - квадратичная"""

from functools import reduce

numbers = [3, 5, 7, 9, 1, 0]
print(reduce(lambda x, y: x if x < y else y, numbers))





"""O(n) - линейная"""

def min_num(n):
    low = n[0]      # O(1) - Константная
    for i in n:     # O(N) - Линейная
        if i < low: # O(1) - Константная
            low = i # O(1) - Константная
    return low      # O(1) - Константная


numbers = [3, 5, 7, 9, 1, 0]
print(min_num(numbers))
