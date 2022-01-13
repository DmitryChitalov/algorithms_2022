"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
import numpy as np

list = np.random.randint(-10, 10, 10)

print("Таков список: ",list)

def search_min_quadratic(list):
    min = list[0]  # O(1)
    for i in list:  # O(n)
        if i < min:  # O(1)
            min = i  # O(1)

    return min



def search_min_linear(list):
    min = list[0]       #O(1)
    for i in list:      #O(n)
        if i < min:     #O(1)
            min = i     #O(1)
    return min

print("Минимальный элемент: ", search_min_quadratic(list))
print("Минимальный элемент: ", search_min_linear(list))
