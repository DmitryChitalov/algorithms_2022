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

def list_value_1(value):
    for i in value:
        min_value = True
        for m in value:
            if m < i:
                min_value = False
        if min_value:
            return i


# o(n)


def list_value_2(value):
    min_value = value.pop()
    for number in value:
        if number < min_value:
            min_value = number
    return min_value


value1 = [20, 10, 8, 16, 18]

print(list_value_1(value1))
print(list_value_2(value1))
