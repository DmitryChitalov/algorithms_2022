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

EL_MY_NUM = 1


# from task_3 import enter_a_number()
def enter_num_el():
    my_flag = True
    while my_flag:
        try:
            my_number = int(input('Введите количество элементов: '))
            my_flag = False
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
    return my_number


def n_sum_sequence(my_num):
    global EL_MY_NUM
    EL_MY_NUM = EL_MY_NUM / (-2)
    # базовый случай         # рекурсивный случай (вызов ф-ции из себя)
    return 1 if my_num == 1 else EL_MY_NUM + n_sum_sequence(my_num - 1)


if __name__ == '__main__':
    inp_nam = enter_num_el()
    print(f'Количество элементов - {inp_nam}, их сумма - {n_sum_sequence(inp_nam)}')
