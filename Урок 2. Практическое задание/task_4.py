"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def numbers_el(n):
    n = int(n)

    if n % 2 == 0:
        first_el_row = -1
        final_row = ((first_el_row / 2) ** (n-1))  # число n ряда
        print(f'финальное число ряда {final_row} от четного числа')
        count_sum = (first_el_row * ((-0.5) ** n - 1)) / (-0.5 - first_el_row)  # формула суммы прогрессии где 0.5 = 1/2
        print(count_sum)

    elif n % 2 != 0:
        first_el_row = 1
        final_row = ((first_el_row / 2) ** (n - 1))  # число n ряда
        print(f'финальное число ряда {final_row} от не четного числа')
        count_sum = (first_el_row * ((-0.5) ** n - 1)) / (-0.5 - first_el_row)  # формула суммы прогрессии где 0.5 = 1/2
        print(count_sum)


numbers_el(input("Введите количество элементов: "))


def func_progression(n, first_el_row=1):
    n = int(n)

    if n > 52:
        print(f'{0.6} в периоде')  # n = 52 будет являться числом в периоде
    else:
        count_sum = (first_el_row * ((-0.5) ** n - 1)) / (-0.5 - first_el_row)  # формула суммы прогрессии где 0.5 = 1/2
        print(count_sum)


func_progression(input('Введите количества элементов: '))