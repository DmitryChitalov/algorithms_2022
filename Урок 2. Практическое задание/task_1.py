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
    operation = input("Введите операцию: +, - , *, /, Введите 0 если хотите выйти из программы: ")
    if operation == '0':
        return 'Выход'
    elif operation == '+' or operation == '-' or operation == '*' or operation == '/':
        number_1 = int(input("Введите первое число"))
        number_2 = int(input("Введите второе число"))
        if operation == '+':
            result = number_1 + number_2
            print(result)
            return calculator()
        elif operation == '-':
            result = number_1 - number_2
            print(result)
            return calculator()
        elif operation == '*':
            result = number_1 * number_2
            print(result)
            return calculator()
        elif operation == '/':
            try:
                result = number_1 / number_2
            except ZeroDivisionError:
                print('Деление на ноль')
            else:
                print(result)
            finally:
                return calculator()
    else:
        print('Ввели некорректный символ')
        return calculator()

calculator()







