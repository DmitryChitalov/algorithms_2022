"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

result_num = randint(0, 100)

def guess_number(counter: int = 0):
    if counter < 10:
        user_num = int(input('Введите число: '))
        if user_num < result_num:
            print('Введенное число, меньше загаданного')
            return guess_number(counter = counter + 1)
        elif user_num > result_num:
            print('Введенное число, больше загаданного')
            return guess_number(counter = counter + 1)
        elif user_num == result_num:
            return 'Вы отгадали загаданное число!'
    else:
        return f'Вы проиграли, загаданное число - {result_num}'

print(guess_number())