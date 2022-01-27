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

def average(n, val):
    if n == 0:
        return 0
    else:
        return (-0.5) ** (val - n) + average(n - 1, val)

number = int(input('Введите количество элементов: '))
print(f'Количество элементов - {number}, их сумма - {average(number,number)}')
