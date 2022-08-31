"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""


import random


def guesser(attempts):
    if attempts == 0:
        return exit('Вы проиграли!')
    try:
        answer = int(input('Введите число от 0 до 100: '))
        if answer == number:
            return exit('Вы победили!')
        elif answer > number:
            print(f'Загаданное число меньше! Попыток осталось: {attempts - 1}')
        else:
            print(f'Загаданное число больше! Попыток осталось: {attempts - 1}')
    except ValueError:
        print(f'Это не число! Попыток осталось: {attempts - 1}')
    return guesser(attempts - 1)


number = random.randint(0, 100)
number_of_attempts = 10
guesser(number_of_attempts)
