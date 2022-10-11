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
def series_numbers(num, sum_series=0, count=0, range_number=1):
    if count == int(num):
        print(f'Количество элементов - {num}, их сумма - {sum_series}')
    else:
        sum_series += range_number
        range_number /= -2
        count += 1
        series_numbers(num, sum_series, count, range_number)


if __name__ == '__main__':
    number = input('Введите количество элементов:')
    series_numbers(number)