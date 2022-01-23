"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def search_min_lst_quadratic_v1(lst):
    min_elem = lst[0]
    for i in range(0, len(lst)):
        if lst[i] == None:
            break
        elif min_elem > lst[i]:
            min_elem = lst.pop(i)
            lst.append(None)
    return min_elem


def search_min_lst_quadratic_v2(lst):
    lst_copy = lst.copy()
    min_elem = lst_copy[0]
    for elem in lst_copy:
        if min_elem > elem:
            min_elem = elem
    return min_elem


def search_min_lst_linear(lst):
    min_elem = lst[0]
    for elem in lst:
        if min_elem > elem:
            min_elem = elem
    return min_elem


test_lst = [28, 6, 15, 20, 2, 30, 100, 98, 16, 3, 7]
print(search_min_lst_quadratic_v1(test_lst))
test_lst = [28, 6, 15, 20, 2, 30, 100, 98, 16, 3, 7]
print(search_min_lst_quadratic_v2(test_lst))
print(search_min_lst_linear(test_lst))
