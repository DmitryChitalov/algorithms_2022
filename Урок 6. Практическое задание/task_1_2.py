"""
Задание 1.

Это файл для второго скрипта
"""
'''
Урок 2. Задание 1
Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
'''


from memory_profiler import profile


@profile
def calculator():
    operation = input('Введите операцию: +,-,* или / (для выхода введите 0) ')
    result = ''

    if operation == '0':
        print('До новых встреч')
    else:
        try:
            num1 = int(input('Введите первое число '))
            num2 = int(input('Введите второе число '))
        except ValueError:
            print("Вы вместо числа ввели строку (((. Исправьтесь")
            return calculator()

        if operation == '+':
            result = num1 + num2
        if operation == '-':
            result = num1 - num2
        if operation == '*':
            result = num1 * num2
        if operation == '/':
            if num2 != 0:
                result = num1 + num2
            else:
                print('Деление на ноль запрещено (((')

        if operation in '+-*/':
            print(f'Ваш результат {result}')
        else:
            print('Знак операции не расспознан, попробуйте снова')
        calculator()


def calculator_optim():
    operation = input('Введите операцию: +,-,* или / (для выхода введите 0) ')
    while operation != '0':
        if operation not in '+-*/':
            print('Знак операции не расспознан, попробуйте снова')
            continue
        num1 = int(input('Введите первое число '))
        num2 = int(input('Введите второе число '))
        if operation == '+':
            result = num1 + num2
        if operation == '-':
            result = num1 - num2
        if operation == '*':
            result = num1 * num2
        if operation == '/':
            if num2 != 0:
                result = num1 + num2
            else:
                print('Деление на ноль запрещено (((')
        print(f'Ваш результат {result}')
        operation = input('Введите операцию: +,-,* или / (для выхода введите 0) ')


calculator_optim()
calculator()

'''
16.2  18.9
Замена рекурсии на цикл положительно сказывается на использовании памяти
ппоскольку при использовании рекурсии храниться стек вызовов функции
'''


