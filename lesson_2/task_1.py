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


def calc():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода):')

    if operation in '0':
        return
    elif operation in '+-/*':
        try:
            num_1 = int(input('Введите первое число:'))
            num_2 = int(input('Введите второе число:'))
            if operation == '+':
                return print('Ваш результат: ', num_1 + num_2), calc()
            elif operation == '-':
                return print('Ваш результат: ', num_1 - num_2), calc()
            elif operation == '/':
                try:
                    num_1 / num_2
                except ZeroDivisionError:
                    print('На ноль невозможно делить.')
                else:
                    print('Ваш результат: ', num_1 / num_2)
                finally:
                    return calc()
            elif operation == '*':
                return print('Ваш результат: ', num_1 * num_2), calc()
        except ValueError:
            print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь'), calc()
    else:
        return print('Ошибка, неверный знак. Исправьтесь.'), calc()


calc()
