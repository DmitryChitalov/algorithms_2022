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


def math_operation():
    num1 = int(input('Введите первое число \n'))
    num2 = int(input('Введите второе число \n'))
    math_oper = input('Введите математическое действие или 0 для выхода \n')
    try:
        if math_oper in '+, -, *, /, 0':

            if math_oper == '0':
                return 'Выход'
            elif math_oper == '+':
                result = num1 + num2
                print(f'Результат {num1}{math_oper}{num2}={result}')
                return math_operation()
            elif math_oper == '*':
                result = num1 * num2
                print(f'Результат {num1}{math_oper}{num2}={result}')
                return math_operation()
            elif math_oper == '-':
                result = num1 - num2
                print(f'Результат {num1}{math_oper}{num2}={result}')
                return math_operation()
            elif math_oper == '/':
                try:
                    result = num1 / num2
                    print(f'Результат {num1}{math_oper}{num2}={result}')
                    return math_operation()
                except ZeroDivisionError:
                    print('Деление на ноль невозможно!')
                finally:
                    return math_operation()
        else:
            print('Неверная математическая операция')
            return math_operation()
    except ValueError:
        print('Неверное значение, повторите ввод')
        return math_operation()


print(math_operation())
