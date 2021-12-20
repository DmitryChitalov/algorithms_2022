"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
from random import randint


def guess_number(number, count=1):
    if count > 10:
        print('Вы проиграли')
        print(f'Загаданное число {number}')
        return
    try:
        num = int(input('Введите число: '))
        if num == number:
            print('Вы победили!')
            return
        elif num > number:
            print('Загаданное число меньше')
            return guess_number(number, count + 1)
        else:
            print('Загаданное число больше')
            guess_number(number, count + 1)

    except ValueError:
        print('Вы ввели строку, введите число')
        guess_number(number, count + 1)


guess_number(randint(1, 100))
