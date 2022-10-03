"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guessing_game(count, random_number):

    print(f'Попытка №{count}')
    user_number = int(input('Введите число от 0 до 100:'))

    if user_number == random_number or count == 10:
        if user_number == random_number:
            print('Победа!')
        else:
            print('Проигрыш')
    else:
        count += 1
        if user_number > random_number:
            print('Меньше!')
        else:
            print('Больше!')
        return guessing_game(count, random_number)

guessing_game(1, randint(0, 100))