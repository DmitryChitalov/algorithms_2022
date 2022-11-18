"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random
from random import randint


def guess(count=1, random_num=(random.randint(1, 100))):
    user_num = int(input('Угадайте, какое число я загадал: '))
    if user_num == random_num and count <= 10:
        return print(f'Вы угадали с {count} попыток')
    elif count > 10:
        return print('Вы проиграли! Попытки закончились')
    else:
        if user_num > random_num:
            print('Слишком большое число!')
        else:
            print('Слишком маленькое число!')
        guess(count+1, random_num)


guess()
