"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def what_num(iter_num, number):
    if iter_num == 10:
        return print(f'Попытки закончились, было загадано число {number}')
    else:
        result = int(input(f'Попытка {iter_num} введите число:\n'))
        if result == number:
            return print('Поздравляем Вы угодали!')
        elif result > number:
            iter_num += 1
            print('Загаданное число меньше введенного')
            return what_num(iter_num, number)
        elif result < number:
            iter_num += 1
            print('Загаданное число больше введенного')
            return what_num(iter_num, number)


what_num(1, randint(1, 100))
