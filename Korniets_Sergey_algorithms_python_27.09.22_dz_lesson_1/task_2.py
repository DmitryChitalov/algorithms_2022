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

# Сложность: O(n^2)
def quadratic_min(data):
    min = data[0]           # O(1)
    for i in data:          # O(n)
        for j in data:      # O(n)
            k = j           # O(1)
        if i < min:         # O(1)
            min = i         # O(1)
    return min              # O(1)

# Сложность: О(n)
def linear_min(data):
    min = data[0]           # O(1)
    for i in data:          # O(n)
        if i < min:         # O(1)
            min = i         # O(1)
    return min              # O(1)

data = [5, -2, 3, -21, 7, 4, 6, -18, 62, 34, 8, 57, 12, -8, 41]
quadratic_min_value = quadratic_min(data)
print(f"Minimal quadratic: {quadratic_min_value}")

linear_min_value = linear_min(data)
print(f"Minimal linear: {linear_min_value}")
