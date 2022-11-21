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


def sum_numbers(number, number_start=1, count_number=0, sum_number=0):
    if number == 0:
        print(f"Количество элементов - {count_number}, их сумма - {sum_number}")
    else:
        count_number += 1
        sum_number += number_start
        number_start = number_start / (-2)
        number -= 1
        return sum_numbers(number, number_start, count_number, sum_number)


input_number = input("Введите количество элементов:")
if input_number.isdigit():
    sum_numbers(int(input_number))
else:
    print("Вы ввели строку, надо вводить число")

