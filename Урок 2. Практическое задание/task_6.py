"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


r = randint(0,100)


def guessNum(n = 10):
    if n == 0:
        print(f"Вы проиграли, число - {r}")
        return
    num = int(input("Введите число"))
    if num > r:
        print(f"Ваше число больше")
        return guessNum(n-1)
    elif num < r:
        print(f"Ваше число меньше")
        return guessNum(n-1)
    elif num == r:
        print(f"Правильно")


guessNum()

