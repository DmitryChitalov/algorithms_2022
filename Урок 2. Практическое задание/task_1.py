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

def recursion1():
   operator = sign()
   if operator == "0":
       return
   digit1 = digit("first")
   digit2 = digit("second")
   if operator == "/" and digit2 == 0 :
       print("Division to 0 isn't possible")
       recursion1()
   elif operator == "+":
       print(f'{digit1} + {digit2} =  {digit1 + digit2}')
       recursion1()
   elif operator == "-":
       print(f'{digit1} - {digit2} = {digit1 - digit2}')
       recursion1()
   elif operator == "*":
       print(f'{digit1} * {digit2} = {digit1 * digit2}')
       recursion1()
   else:
       print(f'{digit1} / {digit2} =  {digit1 * digit2}')
       recursion1()


def sign():
    while True:
        sign = input("\nPlease enter operation sign (+, -, *, / or 0 for exit): ")
        if sign in ("+", "-", "*", "/", "0"):
            return sign
        else:
            print(' Please try to enter sign again ')

def digit(param):
    while True:
        try:
            digit1 = int(input(f"Pls enter {param} value  : "))
            return digit1
        except ValueError:
            print(' Please try to enter digit again ')


recursion1()

# Script listing:
#
# Please enter operation sign (+, -, *, / or 0 for exit): abc
#  Please try to enter sign again
#
# Please enter operation sign (+, -, *, / or 0 for exit): /
# Pls enter first value  : 5
# Pls enter second value  : 0
# Division to 0 isn't possible
#
# Please enter operation sign (+, -, *, / or 0 for exit): +
# Pls enter first value  : 23
# Pls enter second value  : 34
# 23 + 34 =  57
#
# Please enter operation sign (+, -, *, / or 0 for exit): 0
#
# Process finished with exit code 0

