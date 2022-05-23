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

def sum_numbers(number):
    if number > 1:
        return number + sum_numbers(number - 1)
    return number


def set_numbers(number):
    return int((number * (number + 1)) / 2)


def result(number):
    if sum_numbers(number) == set_numbers(number):
        return f'При number = {number} равенство: 1+2+...+n = n(n+1)/2 - выполняется'
    else:
        return f'При number = {number} равенство: 1+2+...+n = n(n+1)/2 - не выполняется'


number_num = int(input('Введите количество чисел: '))
print(result(number_num))
