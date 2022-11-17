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


def get_reversed_num(n, i=0, num=1.0, num_sum=0.0):
    if i == n:
        return num_sum
    num_sum += num
    num /= -2
    i += 1
    return get_reversed_num(n, i, num, num_sum)


if __name__ == '__main__':
    try:
        user_num = int(input('Введите число: '))
        print(f'Количество элементов - {user_num}, их сумма - {get_reversed_num(user_num)}')
    except ValueError as e:
        print(f'{e}: Вы ввели не число')

