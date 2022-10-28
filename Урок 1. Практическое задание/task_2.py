"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.

"""


def min_of_lst_1(lst):
    minimum = lst[0]  # O(1)
    for i in range(len(lst)):  # O(n)
        for j in range(i, len(lst)):  # O(n)
            if lst[i] < lst[j] and lst[i] < minimum:  # O(1)
                minimun = lst[i]  # O(1)
    return minimun  # O(1)

    # O(n^2)


"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""


def min_of_lst_2(lst):
    minimun = lst[0]  # O(1)
    for i in range(len(lst)):  # O(n)
        if lst[i] < minimun:  # O(1)
            minimun = lst[i]  # O(1)
    return minimun  # O(1)

    # O(n)


inp_lst = list(map(int, input().split()))
print(min_of_lst_1(inp_lst))
print(min_of_lst_2(inp_lst))


"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
