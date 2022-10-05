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


def adding_cycle():
    result = 0
    while True:

        nxt_num = input("Enter next number to add: \n")
        if nxt_num.isdigit():
            nxt_num = int(nxt_num)
        else:
            continue
        result += nxt_num
        if nxt_num == 0:
            return result

def calc_func(func, res, num_type):
    nxt_num = input("Enter the next number: \n")
    if nxt_num.isdigit():
        nxt_num = num_type(nxt_num)
        if nxt_num != 0:
            return calc_func(func, func(res, nxt_num), num_type)
        else:
            if func is float.__truediv__:
                print("Невозможно делить на ноль")
                return calc_func(func, res, num_type)
            return res
    else:
        print("Это не число \n")
        return calc_func(func, res, num_type)




def calculator(command):
    start_num = input('Enter number to start:')
    if not start_num.isdigit():
        calculator(command)
    match command:
        case '+':
            return calc_func(int.__add__, int(start_num), int)
        case "-":
            return calc_func(int.__sub__, int(start_num), int)
        case "*":
            return calc_func(float.__mul__, float(start_num), float)
        case "/":
            return calc_func(float.__truediv__, float(start_num), float)
        case _:
            return "Invalid command"


if __name__ == "__main__":
    while True:
        command = input("Введите знак операции: +, -, *, / \n\n")
        print(calculator(command))

