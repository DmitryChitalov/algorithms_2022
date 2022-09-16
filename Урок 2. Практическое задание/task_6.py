"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


import random

number = random.randint(0, 100)
amount = 0
def guess_number(attempt):
    attempt += 1
    your_number = int(input('Попробуйте угадать загаданное число: '))
    if your_number == number or attempt == 10:
        return number
    else:
        if your_number > number:
            #attempt += 1
            print('Вы ввели число больше загаданного.')
        else:
            print('Вы ввели число меньше загаданного.')
            #attempt += 1
        return guess_number(attempt)

print(f'Загаданное число: {guess_number(amount)}')