"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


def guess_the_number(i=1, random_number=random.choice(range(0, 101))):
    my_number = int(input('Введите число: '))
    if i == 10:
        return print(random_number)
    elif my_number == random_number:
        return print('Число отгадано')
    elif my_number > random_number:
        print('Ваше число больше загаданного')
    elif my_number < random_number:
        print('Ваше число меньше загаданного')
    return guess_the_number(i + 1, random_number)


guess_the_number()
