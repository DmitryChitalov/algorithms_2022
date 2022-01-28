"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random


def good_number(count=1, random_number=(random.randint(1, 100))):
    try:
        my_number = int(input('Угадайте, какое число я загадал: '))
        if my_number == random_number and count <= 10:
            return print(f'Вы победили! Я действительно загадал {my_number}, вы справились с {count} попытки!')
        elif count > 10:
            return print('Вы проиграли! Попытки закончились Т_Т')
        else:
            if my_number > random_number:
                print('Я загадал число меньше!!!')
            else:
                print('Я загадал число больше!!!')
            good_number(count + 1, random_number)
    except ValueError:
        print('Вы ввели строку, введите число')
        good_number()


good_number()
