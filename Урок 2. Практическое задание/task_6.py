"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess(num, trys=10):
    user_num = int(input('Введите число: '))

    if trys == 1:
        return print('Было загадано число: ', num)
    elif user_num == num:
        return print('Угадал!')
    else:
        if user_num > num:
            print('Меньше!')
        if user_num < num:
            print('Больше!')
        trys -= 1
    return guess(num, trys)


num = round(random.random() * 100)
print(num)
guess(num)
