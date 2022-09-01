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
    operation = input('Enter operation: ')
    if operation == '0':
        print('Calculator Exited')
        return None
    else:
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            while True:
                number1 = input("Please, enter the first number: ")
                if not number1.isdigit():
                    print(f' "{number1}" is a string. Enter number, please!')
                else:
                    number1 = int(number1)
                    break
            while True:
                number2 = input("Please, enter the second number: ")
                if not number2.isdigit():
                    print(f' "{number2}" is a string. Enter number, please!')
                else:
                    number2 = int(number2)
                    break
            if operation == '+':
                print(f'The result is {number1 + number2}')
                return calculator()
            elif operation == '-':
                print(f'The result is {number1 - number2}')
                return calculator()
            elif operation == '*':
                print(f'The result is {number1 - number2}')
                return calculator()
            elif operation == '/':
                if number2 != 0:
                    print(f'The result is {number1 / number2}')
                    return calculator()
                else:
                    print(f'Division by Zero!!!')
                    return calculator()
        else:
            print('Wrong operation. + - * / operations are acceptable. Others not. Type "0" to exit calculator.')
            return calculator()
# calculator()

print(calculator())
