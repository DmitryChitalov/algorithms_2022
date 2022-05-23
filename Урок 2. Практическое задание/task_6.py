"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def random(random_number=randint(0, 100), i=0):
    if i < 10:
        num = (int(input('Введите число от 0 до 100: ')))
        if num == random_number:
            return fr'Вы угадали число {random_number}.'
        if num < random_number:
            i += 1
            print('Ваше число меньше')
            return random(random_number, i)
        if num > random_number:
            i += 1
            print('Ваше число больше')
            return random(random_number, i)
    else:
        return 'Попыток больше нет. Вы проиграли!'


print(random())
