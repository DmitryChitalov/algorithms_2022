"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

def guess_number(n, r):
    if n == 0:
        return r
    res = int(input())
    if res < r:
        print(f'меньше')
    elif res > r:
        print('больше')
    elif res == r:
        return 'угадал'
    return guess_number(n-1, r)

random = random.randint(0, 100)
print(guess_number(4, random))



