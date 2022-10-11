"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def numbers_summ(n, result, number = 1.0):
    if n == 0:
        print(f'Сумма чисел: {result}')
    else:
        result = result + number
        number = number / 2 * -1
        return numbers_summ(n - 1, result, number)

number = int(input('Введите количество элементов: '))
numbers_summ(number, 0)