"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def top_game_in_the_world(mystery_num, counter=10):
    user_num = int(input('Введите число от 0 до 100: '))
    if user_num == mystery_num:
        print(f'Победа! Таинственное число - {mystery_num}')
    elif counter == 1:
        print(f'Поражение! Закончились попытки. Таинственное число - {mystery_num}')
    elif user_num > mystery_num:
        print(f'Слишком большое число. Осталось попыток: {counter - 1}')
        top_game_in_the_world(mystery_num, counter - 1)
    elif user_num < mystery_num:
        print(f'Слишком маленькое число. Осталось попыток: {counter - 1}')
        top_game_in_the_world(mystery_num, counter - 1)


top_game_in_the_world(randint(0, 100))
