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


def calculator(total=0.0):
    operator = input('Enter an operator (+, -, *, /, total or 0 to exit): ')
    if operator == '0':
        return 'Exit'
    elif operator == 'total':
        return total
    try:
        first_num = int(input('Enter the first number: '))
        second_num = int(input('Enter the second number: '))
    except ValueError:
        print('You must enter a number')
        return calculator()
    if operator == '+':
        number = first_num + second_num
        print(number)
        return total + calculator(number)
    elif operator == '*':
        number = first_num * second_num
        print(number)
        return total + calculator(number)
    elif operator == '-':
        number = first_num - second_num
        print(number)
        return total + calculator(number)
    elif operator == '/':
        number = first_num / second_num
        print(number)
        return total + calculator(number)
    else:
        print("You've entered invalid operator")
        return total + calculator()


print(calculator())
