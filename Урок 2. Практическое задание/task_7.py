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
import random


def num_sum(n):
    if n == 1:
        return 1
    else:
        return num_sum(n - 1) + n


n = random.randint(1, 1000)
print(f'Вычислим сумму ряда для n = {n} и проверим равенство! ')
res = num_sum(n)
f_res = (n * (n + 1) / 2)
print(f'Получим результат: 1 + 2 + 3 +  ... n = {res} , n(n+1)/2  = {f_res}')
if res == f_res:
    print('Равенство верно!')
else:
    print('Равенство не верно!')
