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


def evidence(n, i=0, sum_n=0):
    if i == n:
        result = n*(n+1)/2
        print(f" Сумма {n} натуральных чисел равна {sum_n}, так же, как и n(n+1)/2 = {result}")
    else:
        i += 1
        sum_n += i
        return evidence(n, i, sum_n)


number = int(input("Введите натуральное число: "))
evidence(number)

