"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guessNumber(userNumber=-1, randomNumber=False, i=0):
    if not randomNumber:
        randomNumber = random.randint(0,100)
        print(randomNumber)
    if userNumber == randomNumber:
        return print('Вы угадали число!')
    elif i == 10:
        return print('Вы не угадали число за 10 попыток!')
    else:
        userNumber = int(input('Введите число: '))
        return guessNumber(userNumber, randomNumber, i + 1)

guessNumber();