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


def min_el_1(lst):              # O(n^2)
    for el in lst:              # O(n)
        is_min = True           # O(1)
        for i in lst:           # O(n)
            if el > i:          # O(1)
                is_min = False  # O(1)
        if is_min:              # O(1)
            return el           # O(1)



def min_el_2(lst):          # O(n)
    min_el = lst[0]         # O(1)
    for el in lst:          # O(n)
        if el < min_el:     # O(1)
            min_el = el     # O(1)
    return min_el           # O(1)


lst = [6,22,35,56,22,10]
print(min_el_1(lst))
print(min_el_2(lst))