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

def check_left(num):
    if num == 1:
        return num
    else:
        return num + check_left(num-1)

def check_right(num):
    return num * (num + 1) / 2

try:
    num = int(input('Введите число: '))
    if check_left(num) == check_right(num):
        print(f'Числа {check_left(num)} и {int(check_right(num))} равны')
    else:
        print(f'Числа {check_left(num)} и {int(check_right(num))} не равны')
except ValueError:
    print('Вы вместо числа ввели строку (((. Исправьтесь')