"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guess_number(counter=10, number=None, generate=True):
    if counter == 0:
        print(f'Вы не угадали! Было загадано число {number}')
        return

    if generate:
        number = randint(0, 100)
        print('Отгадайте число от 0 до 100 за 10 попыток')

    try:
        guess = int(input(f'Попыток осталось: {counter}. Введите число: '))
    except ValueError:
        print('Ошибка! Введено не число!')
        guess_number(counter, number=number, generate=False)
    else:
        if guess == number:
            print(f'Вы угадали - загадано число {number}!')
            return
        elif guess < number:
            print('Неверно! Загаданное число больше')
            return guess_number(counter - 1, number=number, generate=False)
        elif guess > number:
            print('Неверно! Загаданное число меньше')
            return guess_number(counter - 1, number=number, generate=False)


guess_number()
