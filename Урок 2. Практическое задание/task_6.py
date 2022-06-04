"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

num = randint(0, 100)


def attempt(n=num):
    att = int(input('Insert number : '))
    if att < n:
        return f'The answer is larger'
    elif att > n:
        return f'The answer is less'
    else:
        return f'='


def game(cnt=10, n=num):
    att = attempt()
    if cnt == 1:
        if att == '=':
            print('You won')
        else:
            print(f'You lose, answer = {n}')
    else:
        if att == '=':
            print('You won')
        else:
            print(f'{att}. Try again')
            cnt -= 1
            return game(cnt)


game()