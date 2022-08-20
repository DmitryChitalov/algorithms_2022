"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_number(number=randint(0, 50), count=1):
    try:
        shot = int(input('Ваша {} попытка угадать число: '.format(count)))
    except ValueError:
        print('Попробуйте всё-таки ввести число: ')
        return guess_number(number)
    count += 1
    if shot == number:
        print('Вы угадали, это число {}!'.format(number))
    elif shot > number and count < 10:
        print('Ваше число больше')
        return guess_number(number, count)
    elif shot < number and count < 10:
        print('Ваше число меньше')
        return guess_number(number, count)
    elif shot != number and count == 10:
        print('Не угадали, это было число {}'.format(number))


guess_number()
