"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_number(num=randint(0, 100), i=1):
    try:
        user_num = int(input(f'Попытка {i} Введите число от 0 до 100: '))
    except ValueError:
        print(f'Это не число')
        return guess_number(num, i)
    if num == user_num:
        print(f'Поздравляю, {num} - верное число!')
    elif i == 10:
        print(f'Не повезло, верное число: {num}')
    elif user_num < num:
        print(f'Попробуй число больше')
        return guess_number(num, i + 1)
    elif user_num > num:
        print(f'Попробуй число меньше')
        return guess_number(num, i + 1)


if __name__ == '__main__':
    guess_number()
