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


def calc():
    sing = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sing == '0':
        return
    if sing not in ('+', '-', '*', '/'):
        print('Неверный знак, введите операцию (+, -, *, / или 0 для выхода)')
        return calc()
    try:
        fst_num = int(input('Введите первое число: '))
        sec_num = int(input('Введите второе число: '))
    except ValueError:
        print('Упс, ввели не число')
        return calc()
    if sing == '+':
        answ = fst_num + sec_num
    elif sing == '-':
        answ = fst_num - sec_num
    elif sing == '*':
        answ = fst_num * sec_num
    elif sing == '/':
        try:
            answ = fst_num / sec_num
        except ZeroDivisionError:
            print('Нельзя делить на 0')
            return calc()
    else:
        answ = 'ОШИБКА'
    print(f'Ваш результат {answ}')
    calc()


calc()
