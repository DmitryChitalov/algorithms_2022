'''1. Написать программу, которая будет складывать, вычитать, умножать или
делить два числа. Числа и знак операции вводятся пользователем. После
выполнения вычисления программа не должна завершаться, а должна запрашивать
новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак
(не "0", "+", "-", "*", "/"), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.'''

def calculation():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    operation = input('Введите знак операции: ')
    if operation == '0':
        return ()
    elif operation == '+':
        print(number_1 + number_2)
        return calculation ()
    elif operation == '/':
        if number_2 == 0:
            print('Деление на ноль невозможно!')
            return calculation()
        else:
            print(number_1 / number_2)
            return calculation()
    elif operation == '-':
        print(number_1 - number_2)
        return calculation()
    elif operation == '*':
        print(number_1 * number_2)
        return calculation()
    else:
        print ('Неверный ввод знака операции!')
        return calculation()

calculation()

