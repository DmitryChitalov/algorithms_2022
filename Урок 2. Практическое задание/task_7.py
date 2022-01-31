"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb - 1) + numb


try:
    NUMB = int(input("Введите число: "))
    if recur_method(NUMB) == NUMB * (NUMB + 1) / 2:
        print('Равенство верно')
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")
