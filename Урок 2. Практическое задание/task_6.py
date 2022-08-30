"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


from random import randint


def guess_number(rand_num=randint(0, 100), i=0):
    if i <= 10:
        num = int(input('Введите число от 0 до 100: '))
        if num < rand_num:
            print('Загаданное число больше.')
            i += 1
            print(f'Осталось попыток {10 - i}')
            return guess_number(rand_num, i)
        if num > rand_num:
            print('Загаданное число меньше')
            i += 1
            print(f'Осталось попыток {10 - i}')
            return guess_number(rand_num, i)
        if num == rand_num:
            print('Вы угадали')
    else:
        print('Вы исчерпали количесто попыток')


print(guess_number())
