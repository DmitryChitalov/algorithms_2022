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
def summa(num):
    s = 0
    if num < 1:
        return 0
    else:
        s = num + summa(num - 1)
        return s

def compare(num):
    if (num*(num+1))/2==summa(num):
        return True
    return False
num=5
print(compare(num))