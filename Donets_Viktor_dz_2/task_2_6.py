"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randrange


def guess_number(n, attempt=9):
    try:
        x = int(input('Введите число: '))
    except ValueError:
        print('Вы вместо числа ввели строку')
        return guess_number(n, attempt)

    if attempt == 0 and x != n:
        print(f'Вы не угадали число!!! Загаданое число: {n}')
    else:
        if x == n:
            print(f'Вы угадали!!! Загаданое число: {x}')
        elif x < n:
            print(f'Загаданое число: Больше!')
            attempt -= 1
            return guess_number(n, attempt)
        elif x > n:
            print(f'Загаданое число: Меньше!')
            attempt -= 1
            return guess_number(n, attempt)


guess_number(randrange(0, 100))
