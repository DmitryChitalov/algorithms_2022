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
    math_sign = input("Input math sign: +, -, *, / or 0 for exit: ")

    if math_sign == 0:
        return "Exit"

    if math_sign in ["+", "-", "*", "/"]:
        num1 = int(input("Input the first number: "))
        num2 = int(input("Input the second number: "))

        if math_sign == "+":
            result = num1 + num2
            print(f"Your result is: {result}")
            return calculator()

        elif math_sign == "-":
            result = num1 - num2
            print(f"Your result is: {result}")
            return calculator()

        elif math_sign == "*":
            result = num1 * num2
            print(f"Your result is: {result}")
            return calculator()

        elif math_sign == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print(f"You cannot divide by zero.")
            else:
                print(f"Your result is: {result}")
            finally:
                return calculator()

    else:
        print("Unknown sign.")
        return calculator()


calculator()