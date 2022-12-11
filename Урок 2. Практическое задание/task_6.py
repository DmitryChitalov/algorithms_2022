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


def guess_number(num, us_num=0, count=0):
    us_num = int(input('Введите число от 0 до 100: '))
    if num == us_num:
        return f'Загаданное число - {num}, вы угадали!\nПоздравляю!'
    elif count == 11:
        return f'Загаданное число - {num}, вы проиграли((('
    else:
        if us_num > num:
            count += 1
            print('Ваше число больше загаданного.')
            return guess_number(num, us_num, count)
        elif us_num < num:
            count += 1
            print('Ваше число меньше загаданного.')
            return guess_number(num, us_num, count)


print(guess_number(number))