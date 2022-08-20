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

def min_squre(list_in):
    copy_list = []                                     # О(1) - константная
    copy_list.extend(list_in)                          # O(N) - линейная

    for _ in range(len(copy_list)):                    # O(N) - линейная
        for idx in range(len(copy_list) - 1):          # O(N) - линейная
            if copy_list[idx] > copy_list[idx + 1]:    # О(1) - константная
                buf = copy_list[idx]                   # О(1) - константная
                copy_list[idx] = copy_list[idx + 1]    # О(1) - константная
                copy_list[idx + 1] = buf               # О(1) - константная

    min_val = copy_list[0]                             # О(1) - константная
    return min_val                                     # О(1) - константная


def min_lin(list_in):
    min_val = list_in[0]     # О(1) - константная
    for val in list_in:      # O(N) - линейная
        if val < min_val:    # О(1) - константная
            min_val = val    # О(1) - константная
    return min_val           # О(1) - константная


if __name__ == '__main__':
    test_list = [2, 6, 9, 1, 3, 7]

    print(min_squre(test_list))
    print(min_lin(test_list))
