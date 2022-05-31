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


def calc_sum(n, num_iter=1, previos=0):
    if previos == 0:
        el = 1
    else:
        el = previos / 2 * -1

    if num_iter == n:
        return previos + el

    return previos + calc_sum(n, num_iter + 1, el)


if __name__ == '__main__':
    input_num = int(input('Введите число: '))
    print(calc_sum(input_num))
