"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random
i = 0
hidden_number = random.randint(0, 100)
user_number = None
def random_number():
    global i
    global hidden_number
    global user_number
    if i == 10 or hidden_number == user_number:
        return print(hidden_number)
    else:
        user_number = int(input('Введите число: '))
        if user_number > hidden_number:
            print('Ваше число больше загаданного')
        elif user_number < hidden_number:
            print('Ваше число меньше загаданного')
        i += 1
    return random_number()

random_number()

