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

def recursia(number=int(input('Введите количество элементов: ')), i=0, result=0, result_number=1):
    if number == i:
        return fr'Количество элементов: {number}, Сумма: {result}'
    if number != i:
        result += result_number
        result_number /= -2
        i += 1
        return recursia(number, i, result, result_number)


print(recursia())
