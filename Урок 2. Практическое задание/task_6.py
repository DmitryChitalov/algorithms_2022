"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def search(num, n):
    if n == 0:
        print(f'Попытки закончились, загаданное число: {num}')
        return
    val = int(input('Введите число: '))
    if val > num:
        print('число меньше')
    elif val < num:
        print('число больше')
    else:
        print('верно')
        return
    search(num, n - 1)


search(randint(0, 100), 10)
