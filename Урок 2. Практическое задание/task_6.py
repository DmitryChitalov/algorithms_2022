"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random


def game(minimum, maximum, attempts, answer=''):
    if answer == '':
        print('Угадайте число')
        answer = random.randint(minimum, maximum)
    user_answ = int(input("Осталось попыток: %s. Число находится в диапазоне от %s до %s , введите ответ " % (
        attempts, minimum, maximum)))
    attempts -= 1
    if user_answ > answer:
        print("Неправильно, ваш ответ больше загаданного")
        if attempts == 0:
            print('Попытки закончились, ответ был %s' % answer)
            exit()
        game(minimum, user_answ, attempts, answer)
    elif user_answ < answer:
        print("Неправильно, ваш ответ меньше загаданного")
        if attempts == 0:
            print('Попытки закончились, ответ был %s' % answer)
            exit()
        game(user_answ, maximum, attempts, answer)
    elif user_answ == answer:
        print('ПРАВИЛЬНО!')
        exit()


mins = 1
maxs = 100
atte = 2
game(mins, maxs, atte)
