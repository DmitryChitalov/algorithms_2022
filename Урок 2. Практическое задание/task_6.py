"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def user_input(input_number):
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        print('Вы ввели строку вместо числа.')
        return user_input(input(f'Введите число от 0 до 100: '))


def guess_game(rand_number, counter=1):
    user_guess = user_input(input(f'Введите число от 0 до 100: '))
    print()
    while counter < 10 and user_guess != rand_number:
        if user_guess > rand_number:
            print(f'Загаданное число меньше {user_guess}')
        else:
            print(f'Загаданное число больше {user_guess}')
        print(f'У вас осталось {10 - counter} попыток')
        print()
        counter += 1
        return guess_game(rand_number, counter)
    else:
        if user_guess == rand_number:
            print('Верно!')
        print(f'Загаданное число: {rand_number}')
        return


guess_game(randint(0, 100))
