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

def min_list(enum):
    for i in enum:
        min_value = True
        for el in enum:
            if i > el:
                min_value = False
        if min_value:
            return i

# Сложность - О(N^2)

def min_list_o(enum_o):
    min_val = enum_o[0]
    for i in enum_o:
        if i < min_val:
            min_val = i
    return min_val

# Сложность - О(N)
list = [1000, -8, 5, 6, 100]
res = min_list(list)
print(res)
result = min_list_o(list)
print(result)


