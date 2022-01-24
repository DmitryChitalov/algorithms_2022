"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""

import sys


# стек переполяется при вводе 499 из-за проверки в декораторе
# def recursion_check(func):
#     def wrapper(n, i=1, sum_i=0):
#         if sys.getrecursionlimit() == 1000 and n > 498:
#             print('Введено число больше 498. Стек переполнен')
#             return exit(0)
#         return func(n, i, sum_i)
#
#     return wrapper


# @recursion_check
# без декоратора можно вводить число не больше 997
def check_nat_numbers(n, i=1, sum_i=0):
    if sys.getrecursionlimit() == 1000 and n > 997:
        print('Введено число больше 998. Стек переполнен')
        return exit(0)
    if i <= n:
        sum_i += i
        return check_nat_numbers(n, i + 1, sum_i)
    check_num = int(n * (n + 1) / 2)
    return check_num == sum_i


if __name__ == '__main__':
    print(check_nat_numbers(n=int(input('Введите любое натуральное число: '))))
