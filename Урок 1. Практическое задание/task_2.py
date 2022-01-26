"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def check_min_v1(min_list):  # O(n^2)
    for v in range(len(min_list)):
        min_num = min_list[0]
        for i in min_list:
            if i <= min_num:
                min_num = i
        return min_num


print(check_min_v1([6, 5, 1, 342, 5456, 33, 2, -1]))


def check_min_v2(min_list):  # O(n)
    min_num = min_list[0]
    for i in min_list:
        if i <= min_num:
            min_num = i
    return min_num


print(check_min_v2([6, 5, 1, 342, 5456, 33, 2]))
