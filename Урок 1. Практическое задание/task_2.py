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


# O(n^2)
def quadra_min(arr: list):
    min = arr[0]  # O(1)
    for x in arr:  # O(n)
        for i in arr:  # O(n)
            v = i  # O(1)
        if x < min:  # O(1)
            min = x  # O(1)
    return min  # O(1)


# O(n)
def linear_min(arr: list):
    min = arr[0]  # O(1)
    for x in arr:  # O(n)
        if x < min:  # O(1)
            min = x  # O(1)
    return min  # O(1)


arr = [0, 1, 2, -80, 3, 4, 5, -2, 53, 21, 5, 73, -4, 2, 54]
quadra_min_value = quadra_min(arr)
print(f"Minimal quadra: {quadra_min_value}")

linear_min_value = linear_min(arr)
print(f"Minimal linear: {linear_min_value}")
