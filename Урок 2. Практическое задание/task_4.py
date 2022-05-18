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


# def sum_series_numbers(n, begin_series_numbers=1):
#     """
#     Функция находит сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#     """
#     if n > 1:
#         return begin_series_numbers + sum_series_numbers(n - 1, begin_series_numbers / -2)
#     return begin_series_numbers
#
#
# quantity = int(input('Введите количество элементов: '))
# print(f'Количество элементов - {quantity}, их сумма - {sum_series_numbers(quantity)}')

def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f"Количество элементов - {n_count}, их сумма - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum + numb)


try:
    N_COUNT = int(input("Введите количество элементов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь.")
