"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_num(num, count):
    print('У вас', count, 'попыток! Отгадайте число от 1 до 100.')
    user_num = int(input('Введите число: '))
    if count == 1:
        print('Вы проиграли, загаданное число -', num)
    elif user_num == num:
        print('Вы отгадали число, загаданное число -', num)
    elif user_num > num:
        count -= 1
        print('Ваше число больше загаданного')
        guess_num(num, count)
    else:
        count -= 1
        print('Ваше число меньше загаданного')
        guess_num(num, count)


num = random.randint(1, 101)
guess_num(num, 10)
