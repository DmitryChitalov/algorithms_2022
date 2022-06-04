"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def int_inp():
    return int(input('Insert the number: '))


def my_func():
    try:
        val_1 = int_inp()
        sign = input('Insert +, -, *, / or 0 (for exit): ')
        if sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != '0':
            raise ValueError
        elif sign == '0':
            print('Bye bye!')
        else:
            val_2 = int_inp()
            if sign == '+':
                print(f'{val_1} {sign} {val_2} = {val_1 + val_2}')
            elif sign == '-':
                print(f'{val_1} {sign} {val_2} = {val_1 - val_2}')
            elif sign == '/':
                print(f'{val_1} {sign} {val_2} = {val_1 / val_2}')
            elif sign == '*':
                print(f'{val_1} {sign} {val_2} = {val_1 * val_2}')
            return my_func()
    except ValueError:
        print(f'Oops, you enter wrong value. Try again!', '...', sep='\n')
    except ZeroDivisionError as f:
        print(f'You can`t {f}. Try again!', '...', sep='\n')


my_func()