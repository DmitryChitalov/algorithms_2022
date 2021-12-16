"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def min_1(lst_obj):  # O(n**2)
    min_ = lst_obj[0]  # O(1)
    for el in lst_obj:  # O(n)
        for i in range(lst_obj.index(el) + 1, len(lst_obj), 1):  # O(n)
            if min_ > lst_obj[i]:  # O(1)
                min_ = lst_obj[i]  # O(1)
    return min_  # O(1)


def min_2(lst_obj):  # O(n)
    min_ = lst_obj[0]  # O(1)
    for el in lst_obj:  # O(n)
        if el < min_:  # O(1)
            min_ = el  # O(1)
    return min_  # O(1)


lst_obj = [3, 8, 9, 2, 8]

print(min_1(lst_obj))
print(min_2(lst_obj))
