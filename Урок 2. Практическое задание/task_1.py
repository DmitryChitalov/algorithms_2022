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

SIGNS = ('+', '-', '*', '/')


def calc():
    result = 0
    sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sign == '0':
        print('Выход')
        return
    else:
        if sign in SIGNS:
            num_1 = input('Введите первое число: ')
            num_2 = input('Введите второе число: ')
            try:
                num_1 = int(num_1)
                num_2 = int(num_2)
            except ValueError:
                try:
                    num_1 = float(num_1)
                    num_2 = float(num_2)
                except ValueError:
                    print('Было введено не число')
                    return calc()
            if sign == '+':
                result = num_1 + num_2
            elif sign == '-':
                result = num_1 - num_2
            elif sign == '*':
                result = num_1 * num_2
            elif sign == '/':
                try:
                    result = num_1 / num_2
                except ZeroDivisionError:
                    print('Деление на 0')
                    return calc()
            print('Ваш результат: ' + str(result))
        else:
            print('Введен неверный знак операции')
    return calc()


calc()
