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
from functools import reduce


def get_number(description):
    try:
        operator = int(input(description))
    except ValueError:
        print('Это не число.')
        operator = get_number(description)
    return operator


def get_operation():
    current_operations = ('+', '-', '*', '/', '0')
    try:
        operation = input('Введите оперцию(+, -, *, / или 0 для выхода): ')
        if operation not in current_operations:
            raise ValueError
    except ValueError:
        print('Вы ввели неверный код операции. Попробуйте снова.')
        operation = get_operation()
    return operation


def calc():
    operands = []
    operands.append(get_operation())
    if operands[0] == '0':
        print('Программа завершена пользователем')
        return
    operands.append(get_number('Введите первое число: '))
    operands.append(get_number('Введите второе число: '))

    operation = operands[0]
    if operation == '+':
        print(f'Ваш результат {reduce(lambda x, y: x + y, operands[1:])}')
    elif operation == '-':
        print(f'Ваш результат {reduce(lambda x, y: x - y, operands[1:])}')
    elif operation == '*':
        print(f'Ваш результат {reduce(lambda x, y: x * y, operands[1:])}')
    elif operation == '/':
        try:

            print(f'Ваш результат {reduce(lambda x, y: x / y, operands[1:])}')
        except ZeroDivisionError:
            print('Деление на 0.')
    else:
        print(f'Неверная операция {operation}')

    calc()


if __name__ == '__main__':
    calc()
