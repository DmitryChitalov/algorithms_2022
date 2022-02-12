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
def recursion_calc():

    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    """Рекурсия"""
    # базовый случай
    if operator == 0:
        return result
    elif operator == '-' or operator == '+' or operator == '*' or operator == '/':
        try:
            num1 = int(input('Введите первое число: '))
            if not isinstance(num1, int):
                print('Вы ввели не число!!!')
                return recursion_calc()
            num2 = int(input('Введите второе число: '))
            if not isinstance(num2, int):
                print('Вы ввели не число!!!')
                return recursion_calc()
        except ValueError:
            print('Вы ввели не число!!!')
            return recursion_calc()
        if operator == '/' and num2 == 0:
            print('Деление на 0 не возможно!!!')
            return recursion_calc()
        elif operator == '+':
            result = num1 + num2
            print(result)
            return recursion_calc()
        elif operator == '-':
            result = num1 - num2
            print(result)
            return recursion_calc()
        elif operator == '*':
            result = num1 * num2
            print(result)
            return recursion_calc()
        elif operator == '/':
            result = num1 / num2
            print(result)
            return recursion_calc()
        else:
            return recursion_calc()
    else:
        print('Введен не правильный оператор!!!')
        return recursion_calc()


recursion_calc()