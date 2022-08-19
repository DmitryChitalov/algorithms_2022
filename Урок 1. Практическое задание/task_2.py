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

#Сложность O (n^2)
def square_function(lst_obj):
    for i in lst_obj:               #O(n)
        var = True                  #O(1)
        for x in lst_obj:           #O(n)
            if i > x:               #O(1)
                var = False         #O(1)
        if var:                     #O(1)
            return i                #O(1)


# Сложность: O(N)
def line_function(lst_obj):
    first_elem = lst_obj[0]     # O(1)
    for x in lst_obj:           # O(N)
        if x < first_elem:      # O(N)
            first_elem = x      # O(1)
    print(first_elem)           # O(1)
    return (sorted(lst_obj))    # O(1)


for j in (50, 10000):
    lst = sample(range(-100000, 100000), j)

print(line_function(lst))

print(square_function(lst))