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

Решите через рекурсию. Решение через цикл не принимается.

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


def calculator():
    operation = input('Input operator (+, -, *, / or 0 to exit): ')
    if operation == '0':
        return
    if operation in '/+-*':
        try:
            operand_1 = int(input('Input the first integer: '))
            operand_2 = int(input('Input the second integer: '))
            if operation == '+':
                print(f'Result: {operand_1 + operand_2}')
                return calculator()
            elif operation == '-':
                print(f'Result: {operand_1 - operand_2}')
                return calculator()
            elif operation == '*':
                print(f'Result: {operand_1 * operand_2}')
                return calculator()
            elif operation == '/':
                try:
                    print(f'Result: {operand_1 / operand_2}')
                except ZeroDivisionError:
                    print('You cannot divide by zero!')
                else:
                    print(f'Result: {operand_1 / operand_2}')
                finally:
                    return calculator()
        except ValueError:
            print('You input wrong symbol. Try again!')
            return calculator()


if __name__ == '__main__':
    calculator()
