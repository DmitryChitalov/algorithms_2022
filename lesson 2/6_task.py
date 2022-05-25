"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def riddle(n_count=1, number=0):
    if n_count == 1:
        number = randint(0, 100)
    n_guess = input('Enter your number: ')
    if n_count and n_guess != number:
        if int(n_guess) < number:
            print(f'You guessed to small, try again! {10 - n_count} attempts left')
        elif int(n_guess) > number:
            print(f'You guessed to high, try again! {10 - n_count} attempts left')
        else:
            return print('You guessed!')
    riddle(n_count + 1, number)


riddle()
