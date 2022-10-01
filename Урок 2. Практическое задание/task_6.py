"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

def guess_number(hidden : int, n : int = 0):
    n += 1
    if n == 11:
        print(f'Вы не угадали с 10 попыток. Было загадано число {hidden}')
        return

    num = int(input(f'Попытка {n}: Введите число от 0 до 100: '))

    if num == hidden:
        print(f'Вы угадали с попытки {n}')
        return
    else:
        if num > hidden:
            print(f'Загаданное число меньше.')
        else:
            print(f'Загаданное число больше.')
        return guess_number(hidden, n)

hidden = randint(0, 100)
guess_number(hidden)