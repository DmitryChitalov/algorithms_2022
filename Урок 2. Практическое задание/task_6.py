"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

def guess_the_number(attempt=1, number=-1):
    if attempt > 10:
        return print('Ваши попытки закончились')
    if number < 0:
        number = random.randint(0, 100)
    answer = int(input(f'Угадайте число от 0 до 100 включительно.\nПопытка номер {attempt}.\nВведите число - '))
    if answer == number:
        return print('Поздравляю, вы угадали!!!')
    elif answer < number:
        return print('Ваше число МЕНЬШЕ загаданного.\n'), guess_the_number(attempt+1, number)
    else:
        return print('Ваше число БОЛЬШЕ загаданного.\n'), guess_the_number(attempt + 1, number)

guess_the_number()