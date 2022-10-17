"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def rec_calc(n):
    if n == 1:
        return n
    return n + rec_calc(n - 1)


def check_equality():
    n = int(input('Enter n : '))
    view = f'{" + ".join([str(x + 1) for x in range(n)])} = {n}({n}+1)/2'
    left_result = rec_calc(n)
    right_result = n*(n+1)/2
    return f"{view}\nequation is : {left_result == right_result}"


if __name__ == '__main__':
    print(check_equality())

