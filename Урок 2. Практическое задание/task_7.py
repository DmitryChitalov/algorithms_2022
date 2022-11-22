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


def recur_sum(number):
    if number == 1:
        return number
    else:
        return recur_sum(number - 1) + number


def user_input(input_number):
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        print('Вы ввели строку вместо числа.')
        return user_input(input(f'Введите число: '))


user_number = user_input(input(f'Введите число: '))
if recur_sum(user_number) == user_number * (user_number + 1) / 2:
    print('Равенство верно!')

