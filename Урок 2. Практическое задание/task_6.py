"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random

from task_3 import enter_a_number

count = 0
random_number = random.randint(0, 100)
# print('random_number ', random_number)


def comparing_numbers(estimated_number=enter_a_number()):
    global count
    if estimated_number == random_number:
        print('Вы угадали :)')
    else:
        my_lim = 9 - count
        if my_lim > 0:
            count += 1
            print('Ваше число больше загаданного.') if estimated_number > random_number else print(
                'Ваше число меньше загаданного.')
            print(f'Оставшиеся попытки: {my_lim}.')
            comparing_numbers(enter_a_number())
        else:
            print('Попытки закончились :(')


if __name__ == '__main__':
    comparing_numbers()
