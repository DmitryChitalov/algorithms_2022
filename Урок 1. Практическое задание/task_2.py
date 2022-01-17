"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
list = [ 0, -1, 10, -25, 100, -3]

# O(n**2)
def search_min_quadratic(list):
    for i in list:   # O(n)
        if i < list[0]:  # O(1)
            list.insert(0, list[list.index(i)])  # O(n)
    return list[0]


O(n)
def search_min_linear(list):
    min = list[0]       #O(1)
    for i in list:      #O(n)
        if i < min:     #O(1)
            min = i     #O(1)
    return min

print("Минимальный элемент: ", search_min_quadratic(list))
print("Минимальный элемент: ", search_min_linear(list))
