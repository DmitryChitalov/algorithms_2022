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


def calc_func():
    operations = ('+', '-', '/', '*', '**')
    operation = input('Введите знак операции, для выхода из программы введиие 0: ')

    if operation == '0':
        return print('Выход из программы'), exit(0)
    else:
        if operation in operations:
            try:
                operand_a = int(input('Введите первое число: '))
                operand_b = int(input('Введите второе число: '))
            except ValueError:
                print('Вы ввели не число. Попробуйте еще раз')
            else:
                operand_a = int(operand_a)
                operand_b = int(operand_b)
                if operation == '+':
                    print(f'Результат сложения {operand_a} и {operand_b} равен: {operand_a + operand_b}')
                else:
                    if operation == '-':
                        print(f'Результат вычитания {operand_a} и {operand_b} равен: {operand_a - operand_b}')
                    elif operation == '/':
                        try:
                            print(f'Результат деления {operand_a} и {operand_b} равен: {operand_a / operand_b}')
                        except ZeroDivisionError:
                            print('На ноль делить нельзя!')
                    elif operation == '*':
                        print(f'Результат умножения {operand_a} и {operand_b} равен: {operand_a * operand_b}')
                    elif operation == '**':
                        print(f'Результат возведения {operand_a} в степень {operand_b} равен: {operand_a ** operand_b}')
        else:
            print('Вы ввели неверный символ, попробуйте снова')
    return calc_func()


calc_func()
