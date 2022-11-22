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


def sum_finder(number, founded_sum=0, row_element=1):
    if number > 0:
        founded_sum += row_element
        row_element /= -2
        number -= 1
        return sum_finder(number, founded_sum, row_element)
    else:
        return founded_sum


def user_input(input_number):
    try:
        input_number = int(input_number)
        print(f'Количество элементов - {input_number}, их сумма - {sum_finder(input_number)}')
        return
    except ValueError:
        print('Вы ввели строку вместо числа.')
        return user_input(input(f'Введите количество элементов: '))


user_input(input(f'Введите количество элементов: '))
