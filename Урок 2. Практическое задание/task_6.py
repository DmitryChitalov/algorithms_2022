"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guess_number(number=None, num_iter=1):

    if number is None:
        number = randint(0, 100)

    try:
        user_num = int(input('Введите число: '))
    except ValueError:
        print('Это не число')
        guess_number(number, num_iter)
        return

    if num_iter == 10:
        print(f'Попытки закончились. Вы проиграли. Было загадано число: {number}')
        return

    if user_num > number:
        print('Введенное число больше')
    elif user_num < number:
        print('Введенное число меньше')
    elif user_num == number:
        print('Поздравляем вы угадали число!!!')
        return

    guess_number(number, num_iter + 1)


if __name__ == '__main__':

    guess_number()

