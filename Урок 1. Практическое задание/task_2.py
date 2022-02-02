"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def first_min_alg(example):  # O(n^2)
    min_value = example[0]
    for i in range(len(example) - 1):
        for j in range(i + 1, len(example)):
            if j < min_value:
                min_value = example[j]
    return min_value


def second_min_alg(example):  # O(n)
    min_value = example[0]
    for i in example:
        if i < min_value:
            min_value = i
    return min_value


example_list = [12, 16, 27, 42, 11, -15, 2]
print(first_min_alg(example_list))
print(second_min_alg(example_list))
