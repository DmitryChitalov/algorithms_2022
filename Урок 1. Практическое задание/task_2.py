"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

MY_LIST = [3, 5, -4, 0, 45, 10, -1]


def val_found_1(my_list):
    """
    Фунция поиска минимального значения в списке:
    линейная сложность
    """
    min_el = my_list[0]
    for el in my_list[1:]:
        if el < min_el:
            min_el = el
    return min_el


if __name__ == '__main__':
    print(val_found_1(MY_LIST))


def val_found_2(my_list):
    """
    Фунция поиска минимального значения в списке:
    квадратичная сложность
    """
    min_el = my_list[0]
    for el in my_list:
        for elem in range(my_list.index(el) + 1, len(my_list) - 1, 1):
            if min_el > my_list[elem]:
                min_el = my_list[elem]
    return min_el


if __name__ == '__main__':
    print(val_found_2(MY_LIST))
