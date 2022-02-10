"""
Задание 7.    Напишите программу, доказывающую или проверяющую, что для множества
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


def rec_func(num):
    if num <= 1:
        return num 
    else:
        return rec_func(num - 1) + num

num = 5
res_rec_func = float(rec_func(num))
res_calculate = num*(num+1)/2
res = ('отличается от','такая же как в') [res_rec_func == res_calculate]
print(f'рекурсивная сумма {res_rec_func} {res} правой части {res_calculate}')    