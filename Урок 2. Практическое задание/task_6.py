"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_num(num, attempt=0):
    print(num)
    print(f'Attempt #: {attempt+1}')
    player_num = input('Insert number: ')
    if attempt == 9:
        return print('Loss')
    elif player_num == str(num):
        return print('Win')
    else:
        attempt += 1
        return guess_num(num, attempt)


guess_num(num=random.randint(0, 100))
