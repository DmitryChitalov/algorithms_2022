"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

# o(n^2)


def min_value_1(value):
    for i in value:
        min_v = True
        for m in value:
            if m < i:
                min_v = False
        if min_v:
            return i


# o(n)


def min_value_2(value):
    min_v = value.pop()
    for number in value:
        if number < min_v:
            min_v = number
    return min_v


value = [20, 10, 8, 16, 18]

print(min_value_1(value))
print(min_value_2(value))