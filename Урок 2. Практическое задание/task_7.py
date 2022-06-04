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


def rec_func(num, _sum=0):
    if num <= 1:
        _sum += num
        return _sum
    else:
        _sum += num
        return rec_func(num - 1, _sum)


number = 11
numb = number*(number+1)/2
rec = rec_func(number)
if rec == numb:
    print(f'{rec} == {numb}')
else:
    print(f'{rec} != {numb}')