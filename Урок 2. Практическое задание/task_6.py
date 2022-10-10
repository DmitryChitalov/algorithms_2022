"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

def guess_num(number=-1, hidden_number=random.randint(0, 100), attempts=10):
    if number != hidden_number and attempts > 0:
        number = int(input('Введите число: '))
        attempts -= 1
        if number > hidden_number:
            print(f'Загаданное число меньше, осталось {attempts} попыток')
        elif number < hidden_number:
            print(f'Загаданное число больше, осталось {attempts} попыток')
        return guess_num(number, hidden_number, attempts)
    elif number == hidden_number:
        return 'Вы угадали!'
    else:
        return f'Ваши попытки исчерпаны. Загаданное число: {hidden_number}'

print(guess_num())