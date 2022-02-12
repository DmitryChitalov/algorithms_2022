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


def arithmetic_operations():


    def division(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            pass
        else:
            return result


    operator = input()
    first_argument = int(input())
    second_argument = int(input())
    dict_in_func = {'+': first_argument + second_argument, '-': first_argument - second_argument,
                    '*': first_argument * second_argument, '/': division(first_argument, second_argument)}
    if operator == '0':
        return 'Выход'
    elif operator == '/' and second_argument == 0:
        print("Деление на 0 невозможно")
        arithmetic_operations()
    elif operator in list(dict_in_func.keys()) and second_argument != 0:
        print(dict_in_func.get(operator))
        arithmetic_operations()
    elif operator in ['-', '+', '*'] and second_argument == 0:
        print(dict_in_func.get(operator))
        arithmetic_operations()
    else:
        print("Введены неверные символы. Введите , на выбор: 0,-,+,*,/")
        arithmetic_operations()


arithmetic_operations()

