"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import random

def game(number,attempt):
     if attempt == 0:
        return(print('Вы исчерпали все попытки угадать число. Было загадано: ', number))
     else:
        number_user = int(input('Введите число. Попытка: ' + str(attempt)))
        if number_user > number:
           print('Загаданное число меньше')
           attempt = attempt - 1
           return(game(number,attempt))
        if number_user < number:
           print('Загаданное число больше')
           attempt = attempt - 1
           return(game(number,attempt))
        if number_user == number:
           return(print('Вы Угадали! С попытки: ', attempt ))


number = round(random() * 100)
attempt = 10
game(number,attempt)
