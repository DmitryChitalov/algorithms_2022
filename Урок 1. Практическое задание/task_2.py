"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Сложность: O(N²) - квадратичная


def min_val_1(list_1):
    min_num_1 = list_1[0]                                           # O(1)
    for i in list_1:                                                # O(N)
        for k in range(list_1.index(i) + 1, len(list_1) - 1, 1):    # O(N)
            if min_num_1 > list_1[k]:                               # O(1)
                min_num_1 = list_1[k]                               # O(1)
        return min_num_1                                            # O(1)


lst = [666, 555, 54987, 46, 5, 856, 985]
print(min_val_1(lst))


# Сложность: O(N) - линейная

def min_val_2(list_2):
    min_num_2 = list_2[0]                # O(1)
    for y in list_2:                     # O(N)
        if y < min_num_2:                # O(1)
            min_num_2 = y                # O(1)
    return min_num_2                     # O(1)


print(min_val_2(lst))
