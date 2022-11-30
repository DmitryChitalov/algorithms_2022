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

def calculator():
    main_process = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if main_process not in ('+', '-', '*', '/', '0'):
        print('Введите операцию из списка!')
        calculator()

    if main_process == '0':
        print('Программа завершила свою работу!')
        return 0   

    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = 'empty'

    if main_process == '+':
        result = a + b
    elif main_process == '-':
        result = a - b
    elif main_process == '*':
        result = a * b
    elif main_process == '/':
        if b != 0:
            result = a / b
        else:
            print('Нельзя делить на 0!')

    if result != 'empty':
        print('Ваш результат: {result}')
    calculator()

calculator()