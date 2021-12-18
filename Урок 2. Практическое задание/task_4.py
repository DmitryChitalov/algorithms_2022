"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""

def check(num, a = 2, b = 0):
    if num == 0:
        return b
    else:
        if a % 2 == 0:
            a = a / 2
        else:
            a = -(a / 2)
        num -= 1
        b += a
        return check(num, a, b)

try:
    num = int(input('Введите количество элементов: '))
    print(f'Количество элементов - {num}, их сумма - {check(num)}')
except ValueError:
    print('Вы вместо числа ввели строку (((. Исправьтесь')