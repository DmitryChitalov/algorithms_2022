"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)

def quessing_game(hidden_number, remaining_try = 10):
    quess = get_number(f'Try quess number, you have left {remaining_try} attempts: ')

    if quess == hidden_number:
        print('You win')
        return

    remaining_try -= 1

    if not remaining_try:
        print(f'You lose, {hidden_number=}')
        return

    additional_message = ''

    if abs(quess - hidden_number) < 10:
        additional_message = 'but very hot'

    if quess > hidden_number:
        print(f'You enter too big number {additional_message}')
    elif quess < hidden_number:
        print(f'You enter too low nuber {additional_message}')

    quessing_game(hidden_number, remaining_try)


hidden_number = random.randint(0, 100)

quessing_game(hidden_number)