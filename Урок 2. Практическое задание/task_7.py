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

from random import randrange


def checker(n, sum=0):
    if n == 0:
        return sum
    else:
        return checker(n - 1, sum=sum + n)


n = randrange(4, 15)
print(f'n равно: {n}')
if checker(n) == n * (n + 1) / 2:
    print('Для множества натуральных чисел  равенство выполняется')
else:
    print('Для множества натуральных чисел  равенство не выполняется')
