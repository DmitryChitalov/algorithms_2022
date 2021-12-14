"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
####################################################
an = [-2, 3, 5, -1, 7, 1, 0]

def check_1(a):
    """
    Сложность: O(n^2)
    """
    n = a[0]                     # O(1)
    lst = list(a)                # O(n)
    for i in range(len(a)-1):    # O(n)
        if lst[i] < n:           # O(1)
            n = lst[i]           # O(1)
    return n                     # O(1)


####################################################

def check_2(a):
    """
    Сложность: O(n)
    """
    n = a[0]                   # O(1)
    for i in range(len(a)-1):  # O(n)
        if a[i] < n:           # O(1)
            n = a[i]           # O(1)
    return n                   # O(1)

print(check_1(an))
print(check_2(an))
