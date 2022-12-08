"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной
попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randrange


def guess(number, t=0, count=10):
    if count == 0:
        return print(f'Число не угадано за 10 попыток, загаданное число {number}')
    t = int(input('Введите число от 0 до 100 '))
    if t > number:
        print('Введеное число больше загаданного')
    elif t < number:
        print('Введеное число меньше загаданного')
    elif t == number:
        print(f'Вы угадали число {number}')
    return guess(number, t, count - 1)


guess(randrange(0, 100))
