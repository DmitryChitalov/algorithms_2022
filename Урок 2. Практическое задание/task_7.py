"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def process(steps: int, curr_num=0, curr_sum=0, curr_str=''):
    curr_num += 1
    curr_sum += curr_num
    if curr_num == 1:
        curr_str = str(curr_num)
    else:
        curr_str += '+' + str(curr_num)

    if steps == curr_num:
        return f'{curr_str} {"=" if curr_sum == steps * (steps + 1) / 2 else "<>"} {str(steps)}*({str(steps)}+1)/2'
    elif steps == 0:
        return 'Некорректный ввод'
    else:
        return process(steps, curr_num, curr_sum, curr_str)


if __name__ == '__main__':
    num_txt = input('Введите количество элементов: ')
    if not num_txt.isdecimal():
        print('Некорректный ввод')
    else:
        print(f'Количество элементов - {int(num_txt)}\n{process(int(num_txt))}')
