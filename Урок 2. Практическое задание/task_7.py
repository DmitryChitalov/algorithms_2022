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


def proof(n):

    if n == 1:
        return n
    else:
        return proof(n - 1) + n


try:
    n = int(input('Введите число: '))
    if proof(n) == n * (n + 1) / 2:
        print(f'Равенство 1+2+...+n = n(n+1)/2. где n это {n} - верно')

except ValueError:
    print('Вы вместо числа ввели строку')