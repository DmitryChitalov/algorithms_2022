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
""" Рекурсивное исполнение """

def programm_calc():
    number1 = float(input('Введите первое число\n'))
    operand = input('Введите знак операции (+, -, *, /) или 0 для прекращения программы\n')
    number2 = float(input('Введите второе число\n'))
    operand_sign = ['+', '-', '*', '/']
    if operand == '0':
        quit()
    elif operand not in ("+", "-", "*", "/", "0"):
        print('Неизвестная операнда\n')
        operand = input('Введите знак операции (+, -, *, /) или 0 для прекращения программы\n')
    elif operand not in operand_sign:
        print('Введите знак операции!\n')
    elif operand == '+':
        print(f'Результат {number1} + {number2} = {number1 + number2}')
        return programm_calc()
    elif operand == '-':
        print(f'Результат {number1} - {number2} = {number1 - number2}')
        return programm_calc()
    elif operand == '*':
        print(f'Результат {number1} * {number2} = {number1 * number2}')
        return programm_calc()
    elif operand == '/':
        try:
            print(f'Результат {number1} / {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')
        return programm_calc()
    else:
        pass
programm_calc()

# """ Через цикл """

# while True:
#     try:
#         number1, operation, number2 = [
#                 i for i in
#                 input(
#                     'Введите число пробел знак операции (+, -, *, /) или 0 для прекращения программы пробел число: '
#                     ).split()
#                 ]
#     except ValueError:
#         print('Неправильный ввод.')
#         continue
#     number1 = int(number1)
#     number2 = int(number2)

#     if operation == '0':
#         break
#     elif operation == '+':
#         print(f'{number1} {operation} {number2} = {number1 + number2}')
#     elif operation == '-':
#         print(f'{number1} {operation} {number2} = {number1 - number2}')
#     elif operation == '*':
#         print(f'{number1} {operation} {number2} = {number1 * number2}')
#     elif operation == '/':
#         try:
#             print(f'{number1} {operation} {number2} = {number1 / number2}')
#         except ZeroDivisionError:
#             print('Ошибка. Деление на ноль')
