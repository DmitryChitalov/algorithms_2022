"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

guessed_number = randint(1, 100)

def guess_number(count=10):
    try:
        user_number = int(input('Введите свое число: '))
    except ValueError:
        print('Введено неправильное число')
    if count == 0:
        print(f'Вы проиграли! Было загадано число: {guessed_number}')
        return
    elif user_number == guessed_number:
        print(f'Вы угадали c {10 - count} попыток')
    else:
        print(f'Осталось попыток {count}')
        if user_number < guessed_number:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
        guess_number(count - 1)
guess_number()


