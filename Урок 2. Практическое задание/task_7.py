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


def test(n):
    if n == 1:
        print(n, end=' ')
        return n
    else:
        print(n, end='+')
        return test(n - 1) + n


try:
    n = int(input('Введите число: '))
    if test(n) == n * (n + 1) / 2:
        print(f'= {n} * ({n}+1) / 2')
    else:
        print(f'!= {n} * ({n}+1) / 2')
except ValueError:
    print('Введено не натуральное число')
