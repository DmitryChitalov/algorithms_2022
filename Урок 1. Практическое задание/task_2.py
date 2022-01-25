"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

from random import randint


# сложность O(n)
def min_num(lst):
    min_num = lst[0]  # O(1)
    for i in lst:  # O(n)
        if i < min_num:  # O(len(i)
            min_num = i  # O(1)
    return min_num  # O(1)


# Сложность O(n**2)
def min_num_2(lst):
    min_num_2 = lst[0]  # O(1)
    for i in lst:  # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_num_2 > lst[j]:  # O(len(lst[j])
                min_num_2 = lst[j]  # O(1)
    return min_num_2  # O(1)


# сложность O(len(n))
def random_list():
    rl = []  # O(1)
    for i in range(3):  # O(len(n))
        rl.append(randint(0, 99))  # O(1)
    return rl  # O(1)

print(min_num(random_list()))
print(min_num_2(random_list()))
