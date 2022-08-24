"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guessy(n, user_try=10):
    if user_try > 0:
        if n == int(input(f'Tries left: {user_try}. Type your guess 0 to 100: ')):
            return f'Hooray! Congrays, you did it. The answer {n} is correct'
        else:
            print(f'Nope. Try again.')
            return guessy(n, user_try - 1)
    else:
        return f'No tries left. You lost. The right answer is {n}'

print(guessy(randint(0, 100)))
# print(guessy(50))
