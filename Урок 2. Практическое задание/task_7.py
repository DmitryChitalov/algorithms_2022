"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


# from task_3 import enter_a_number № Почему-то возникает ошибка.
def enter_a_number():
    my_flag = True
    while my_flag:
        try:
            my_number = int(input('Введите угадываемое число: '))
            my_flag = False
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
    return my_number


def sum_to_num(input_num):
    if input_num == 1:
        return 1
    return input_num + sum_to_num(input_num - 1)


def print_num(pr_num):
    my_list = list(range(1, pr_num + 1))
    my_str = str(my_list[0])
    for i in range(1, len(my_list)):
        my_str = my_str + ' + ' + str(my_list[i])
    return my_str


if __name__ == '__main__':
    inp_nam = enter_a_number()
    str_left_side = print_num(inp_nam)
    str_right_side = f'{inp_nam}({inp_nam}+1)/2'
    right_side = inp_nam * (inp_nam + 1) / 2
    left_side = sum_to_num(inp_nam)
    print(f'{str_left_side} = {str_right_side}')
    print(f'left side: {str_left_side} = {left_side}')
    print(f'right_side: {str_right_side} = {right_side}')
    print(f'left side = right_side : {left_side == right_side}')
