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


def calculator(op='', n1=None, n2=None):
    if op == '':
        input_str = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if input_str in ('+', '-', '*', '/'):
            calculator(op=input_str)
        elif input_str == '0':
            print('Программа завершила работу. Спасибо!')
        else:
            print('Некорректная команда, исправьтесь')
            calculator()
    elif n1 is None:
        input_str = input('Введите первое число: ')
        if not input_str.isnumeric():
            print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
            calculator(op=op)
        else:
            calculator(op=op, n1=int(input_str))
    elif n2 is None:
        input_str = input('Введите второе число: ')
        if not input_str.isnumeric():
            print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
            calculator(op=op, n1=n1)
        else:
            calculator(op=op, n1=n1, n2=int(input_str))
    else:
        print('Ващ результат: ', end='')
        match op:
            case '+':
                print(n1 + n2)
            case '-':
                print(n1 - n2)
            case '*':
                print(n1 * n2)
            case '/':
                print(n1 / n2)
            case _:
                print('Неизвестная операция')


if __name__ == '__main__':
    calculator()
