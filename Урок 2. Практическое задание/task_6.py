"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random
from random import randint

def game(count = 1, digit = random.randint(1, 100)):
    if count <= 10:
        print(f'Попытка №{count:2} из 10')
        user_number = int(input('Введите число от 1 до 100: '))
        if user_number == digit:
            print('Загаданное число угадано', digit)
        elif user_number > digit:
            print(f'Ваше число {user_number} больше загаданного')
        else:
            print(f'Ваше число {user_number} меньше загаданного')
            game(count + 1)
    elif count > 10:
        print('Было загадано число', digit, 'вы проиграли')
game()


