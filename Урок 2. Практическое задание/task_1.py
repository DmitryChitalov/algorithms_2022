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


def is_number(my_str):
    try:
        float(my_str)
        return True
    except ValueError:
        return False


def get_data(step, all_data):
    my_step = step
    if my_step == 0:
        data = input('Введите операцию (+, -, *, / или 0 для выхода) ')
        if data not in ['+', '-', '*', '/', '0']:
            print('Вы ввели что-то помимо допустимого знака операции, введите еще раз')  # что то пошло не так,
            # вызываем функцию заново с этого же шага, передаем ей структуру, которая частично заполнена на
            # предыдущих шагах
            all_data = get_data(my_step, all_data)
            return all_data  # если все прошло хорошо во вложенном вызове функции, то структура заполнена и ее можно
            # возвращать
        else:
            all_data['operator'] = data
            my_step += 1
    if all_data['operator'] == '0':
        return all_data

    if my_step == 1:
        data = input('Введите число номер %s ' % my_step)
        if not is_number(data):
            print('Вы ввели не число, попробуйте еще раз')
            all_data = get_data(my_step, all_data)  # что то пошло не так,
            # вызываем функцию заново с этого же шага, передаем ей структуру, которая частично заполнена на
            # предыдущих шагах
            return all_data  # если все прошло хорошо во вложенном вызове функции, то структура заполнена и ее можно
            # возвращать, и не идти дальше по функции

        my_step += 1
        all_data['num_1'] = float(data)

    if my_step == 2:
        data = input('Введите число номер %s ' % my_step)
        if not is_number(data):
            print('Вы ввели не число, попробуйте еще раз')
            all_data = get_data(my_step, all_data)
            return all_data
        elif all_data['operator'] == '/' and float(data) == 0:
            print('Деление на ноль. Введите другой делитель, отличный от 0')
            all_data = get_data(my_step, all_data)
            return all_data

        my_step += 1
        all_data['num_2'] = float(data)

    if my_step == 3:
        return all_data


def calculate():
    data = {'operator': '', 'num_1': '', 'num_2': ''}
    data = get_data(0, data)
    if data['operator'] == '0':
        exit()
    else:
        if data['operator'] == '+':
            result = data['num_1'] + data['num_2']
        elif data['operator'] == '-':
            result = data['num_1'] - data['num_2']
        elif data['operator'] == '*':
            result = data['num_1'] * data['num_2']
        elif data['operator'] == '/':
            result = data['num_1'] / data['num_2']

        print('Ваш результат %s' % result)
        calculate()


calculate()
