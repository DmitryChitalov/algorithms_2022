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
#7
def proverka(n:int,b=0):
    if n != 0:
        b = b + n
        return proverka(n-1,b)
    else:
        return b
a = 5
right = a *(a +1)/2
b = proverka(a)
if right == b:
    print(f'{float(right)} = {float(b)}')
