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

def calc():

    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if operation == '0':
        exit()

    else:
        try:
            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))
            if operation == '+':
                res = num_1 + num_2
                print(f"Ваш результат {res}")
                return  calc()

            elif operation == '-':
                res = num_1 - num_2
                print(f"Ваш результат {res}")
                return calc()

            elif operation == '*':
                res = num_1 * num_2
                print(f"Ваш результат {res}")
                return calc()

            elif operation == '/':
                try:
                    res = num_1 / num_2
                except ZeroDivisionError:
                    print('На ноль делить нельзя!')

                else:
                    print(f"Ваш результат {res}")
                finally:
                    return calc()

        except ValueError:
            print("Вы вместо числа ввели строку. Исправьтесь")
            return calc()
        else:
            print("Введен неверный символ, попробуйте еще раз")

    return calc()

calc()
