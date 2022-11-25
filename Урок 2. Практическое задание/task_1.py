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


def guess_the_number():
    OPERATIONS = ['+', '-', '*', '/', '0']

    operation = input('Input operation (+, -, *, / or 0 for exit): ')

    if operation not in OPERATIONS:
        print('Unknown operation')
        return guess_the_number()

    if operation == '0':
        print("Have a good day")
        return
    else:
        try:
            first = int(input('Please enter first number: '))
            second = int(input('Please enter second number: '))
        except ValueError:
            print("You should enter not a string")
            return guess_the_number()

        if operation == '+':
            result = first + second
            print(f"Result {first + second}")
        elif operation == "-":
            print(f"Result {first - second}")
        elif operation == "*":
            print(f"Result {first * second}")
        elif operation == "/":
            try:
                print(f"Result {first / second}")
            except ZeroDivisionError:
                print("Can't divide by zero")

    return guess_the_number()


guess_the_number()
