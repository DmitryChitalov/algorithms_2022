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
    oper = input('+, -, *, / или 0 для выхода: ')
    if oper == '0':
        return 'Выход'
    elif oper not in ['/', '+', '*', '-']:
        print('Вы ввели некорректный символ. Исправьтесь')
        return calculator()
    else:
        try:
            first_num = int(input('Введите первое число: '))
            second_num = int(input('Введите второе число: '))
            if oper == '+':
                print(first_num + second_num)
            elif oper == '-':
                print(first_num - second_num)
            elif oper == '/':
                print(first_num / second_num)
            elif oper == '*':
                print(first_num * second_num)
            return calculator()
        except ZeroDivisionError as e:
            print(f'{e}: деление на 0 недопустимо')
            return calculator()
        except ValueError as e:
            print(f'{e}: вы вместо числа ввели строку (((. Исправьтесь')
            return calculator()


if __name__ == '__main__':
    calculator()