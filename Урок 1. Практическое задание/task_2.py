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
test_lst = [30, 24, 25, 6, 47, 19, 21, 10, 10, 44]


def first_min_el(lst):                  # O(n^2)
    min_els = [lst[0]]                  # O(1)
    for el in lst:                      # O(n)
        if el < min_els[0]:             # O(1)
            min_els.insert(0, el)       # O(n)
        else:
            pass                        # O(1)
    return min_els[0]                   # O(1)


def second_min_el(lst):                             # O(n)
    min_els = [lst[0]]                              # O(1)
    for i in range(len(lst)):                       # O(n)
        if lst[i] < min_els[(len(min_els) - 1)]:    # O(1)
            min_els.append(lst[i])                  # O(1)
        else:
            pass
    return min_els[(len(min_els) - 1)]              # O(1)


print(first_min_el(test_lst))
print(second_min_el(test_lst))
