"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def game(number, max_count):
    if max_count < 11:
        print(number)
        user_number = int(input(f"попытка № {max_count} введите число: "))
        if user_number == number:
            print('Victory')
        elif user_number < number:
            print("введите число больше")
            return game(number, max_count + 1)
        else:
            print("введите число меньше")
            return game(number, max_count + 1)
    else:
        print("У вас закончились попытки")


game(number=random.randint(1, 100), max_count=1)
