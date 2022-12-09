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


def calc_():
    try:
        num1 = float(input('введите первое число '))
        num2 = float(input('введите второе число '))
        attribute = input('Введите операцию "+,-,*,/" или 0 для выхода ')
        if attribute == '0':
            return 'Exit'
        if attribute not in ("+", "-", "*", "/", "0"):
            print('Неизвестная операция')
            attribute = input('Введите операцию "+,-,*,/" или 0 для выхода')
        if attribute == "+":
            print(f'Результат вычислений : {num1 + num2}')
        elif attribute == "-":
            print(f'Результат вычислений : {num1 - num2}')
        elif attribute == "*":
            print(f'Результат вычислений : {num1 * num2}')
        elif attribute == "/":
            try:
                print(f'Результат вычислений : {num1 / num2}')
            except ZeroDivisionError:
                print('На ноль делить нельзя')
            return calc_()
        return calc_()
    except ValueError:
        print('Введены данные, отличные от чисел. Введите число')
        return calc_()


print(calc_())