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


def equality_check(number: int, left_exp=0, right_exp=0):
    """
    Функция проверяет, выполняется ли равенство 1+2+...+n = n(n+1)/2,
    :param number: n - любое натуральное число
    :param left_exp: Служебный аргумент (не нужно указывать)
    :param right_exp: Служебный аргумент (не нужно указывать)
    :return:
    """
    if left_exp == 0:
        right_exp = int(number * (number + 1) / 2)
    left_exp = left_exp + number
    if number > 1:
        return equality_check(number - 1, left_exp, right_exp)
    else:
        return left_exp == right_exp


if __name__ == '__main__':
    print('Проверка равенства 1+2+...+n = n(n+1)/2')
    for user_number in range(1, 101):
        if user_number < 10:
            print(f'(Для n  = {user_number} - {equality_check(user_number)} ', end='')
        elif user_number % 10 != 0:
            print(f'Для n = {user_number} - {equality_check(user_number)} ', end='')
        else:
            print(f'Для n = {user_number} - {equality_check(user_number)}')