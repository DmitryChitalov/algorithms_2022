"""
Задание 4.    Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def func(num, start=-2):
    if num == 0:
        print(f'return base {start}')
        return 0
    else:
        start = start / (-2)
        # print(f'return num {num} start  {start}')
        return func(num - 1, start) + start

num = 3
res = func(num)
print(f'количество элементов {num} результат {res}')

























'''def func(count, digit=1):
    if count <= 1:
        print(f'digit {digit}')
        return digit
    else:
        digit = -(digit / 2)
        print(f'digit {digit}')
        return func(count-1, digit) + digit 




count = int(input('Введите количество элементов: '))
summ = func(count)
print(f'Количество элементов - {count}, их сумма  {summ}')'''