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
    try:
        symb = input('Select operation: +, -, *, / or 0 to exit: ')
        if symb in ('+', '-', '*', '/'):
            try:
                first_numb = int(input('Enter first number: '))
                sec_numb = int(input('Enter second number: '))
                if str(first_numb).isdigit() and str(sec_numb).isdigit():
                    if symb == "+":
                        print('Result = ', first_numb + sec_numb)
                    elif symb == "-":
                        print('Result = ', first_numb - sec_numb)
                    elif symb == "*":
                        print('Result = ', first_numb * sec_numb)
                    elif symb == "/":
                        try:
                            print('Result = ', first_numb / sec_numb)
                        except ZeroDivisionError:
                            print("Cant divide by zero, try again")
            except ValueError:
                print("Wrong data value, try again")
        else:
            if symb != "0":
                raise TypeError("Wrong symbol, try again")
    except Exception:
        print("Wrong symbol, try again")
    finally:
        if symb == "0":
            exit(0)
        else:
            calculator()


if __name__ == "__main__":
    calculator()
