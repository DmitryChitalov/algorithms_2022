"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцию-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def check_quantity(num):
    if num == 1:
        return num
    else:
        return check_quantity(num - 1) + num


number = 5

if check_quantity(number) == number * (number + 1) / 2:
    print('Quantities are equal')
else:
    print('Quantities are not equal')


