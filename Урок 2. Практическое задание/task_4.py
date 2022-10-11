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


def process(steps: int, curr_sum=0.0, curr_val=1.0):
    if steps == 0:
        return curr_sum
    else:
        curr_sum += curr_val
        curr_val = -1 * curr_val / 2
        return process(steps - 1, curr_sum, curr_val)


if __name__ == '__main__':
    num_txt = input('Введите количество элементов: ')
    if not num_txt.isdecimal():
        print('Некорректный ввод')
    else:
        print(f'Количество элементов - {int(num_txt)}, их сумма - {process(int(num_txt))}')
