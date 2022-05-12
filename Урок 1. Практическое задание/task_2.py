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


def min_quad(in_list: list):    # O(n^2)
    for el in in_list:                # O(n)
        fl = True                     # O(1)
        for el2 in in_list:           # O(n)
            if el2 < el:              # O(1)
                fl = False            # O(1)
        if fl:                        # O(1)
            return el                 # O(1)
    return None                       # O(1)


def min_lin(in_list: list):       # O(n)
    if len(in_list) > 0:              # O(1)
        mi = in_list[0]               # O(1)
    else:                             # O(1)
        return None                   # O(1)
    for el in in_list[1::]:           # O(n)
        if el < mi:                   # O(1)
            mi = el                   # O(1)
    return mi                         # O(1)


if __name__ == "__main__":
    tst = [
        [1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 3, 3, 4, 4, 5, 6, 10, 1, -1, -1, 15],
        [1, 1, 1, 1, 1, 1],
        [1, 2, 3],
        [3],
        []
    ]
    for ts in tst:
        print(min_quad(ts), end="   ")  # -1   1   1   3   None
    print()
    for ts in tst:
        print(min_lin(ts), end="   ")  # -1   1   1   3   None
