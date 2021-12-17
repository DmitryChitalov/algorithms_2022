"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def find_min1(lst_in):  # O(n^2)
    min1 = lst_in[0]  # O(1)
    for i in range(len(lst_in)):  # O(n)
        min_flag = 0  # O(1)
        for j in range(i, len(lst_in)):  # O(n)
            if lst_in[j] < min1:  # O(1)
                min1 = lst_in[j]  # O(1)
                min_flag = 1  # O(1)
                break
        if min_flag == 0:  # O(1)
            return min1  # O(1)


def find_min2(lst_in):  # O(n)
    min2 = lst_in[0]  # O(1)
    for i in range(len(lst_in)):  # O(n)
        if lst_in[i] < min2:  # O(1)
            min2 = lst_in[i]  # O(1)

    return min2  # O(1)


lst1 = [0, 2, -1, -9, 0, -243, -3]
print(find_min1(lst1))
print(find_min2(lst1))
