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
from random import randint

list = []
for n in range(10):
    list.append(randint(0, 20))
print(list)

# 1. O(1) + O(N) * O(N) + O(1) = O(N^2)
def min_list1(list):
    x = 0
    for el in list:         # O(N)
        if x not in list:   # O(N)
            x += 1          # O(1)
        else:
            return x        # O(1)

print(min_list1(list))



# 2. O(1) + O(N) + O(1) + O(1) + O(1) = O(N)
def min_list2(list):
    small = list[0]     # O(1)
    for el in list:     # O(N)
        if el < small:  # O(1)
            small = el  # O(1)
    return small        # O(1)

print(min_list2(list))