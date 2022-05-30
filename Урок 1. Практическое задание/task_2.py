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


def minimum_value_1(lst):                   # Сложность: O(n^2)
    value = lst[0]                          # O(1)
    for i in range(len(lst)):               # O(n)
        for j in range(len(lst)):           # O(n)
            if i != j:                      # O(1)
                if lst[i] < lst[j]:         # O(1)
                    if lst[i] < value:      # O(1)
                        value = lst[i]      # O(1)
                else:
                    if lst[j] < value:      # O(1)
                        value = lst[j]      # O(1)

    return value                            # O(1)


def minimum_value_2(lst):                   # Сложность: O(n)
    value = lst[0]                          # O(1)
    for i in lst:                           # O(n)
        if i < value:                       # O(1)
            value = i                       # O(1)
    return value                            # O(1)


# user_list = [10, 20, 50, 5, 40]
#
# print(minimum_value_1(user_list))
# print(minimum_value_2(user_list))
