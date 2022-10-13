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


# O(n)
def min_num1(num_list):
    result = num_list[0]
    for i in num_list[1:]:
        if i < result:
            result = i
    return result


# O(n^2)
def min_num2(num_list):
    for i in num_list:
        result = i
        for j in num_list:
            if j < result:
                result = j
        return result
