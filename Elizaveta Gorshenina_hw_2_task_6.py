"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guess_number():
    def check(a_try, a_number, tries_num=9):
        if a_try == a_number:
            return print('Поздравляем! Вы отгадали!')
        else:
            if tries_num == 0:
                if a_try < a_number:
                    return print(f'Загаданное число: {the_num}. Вы не отгадали.')
                else:
                    return print(f'Загаданное число: {the_num}. Вы не отгадали.')
            else:
                if a_try < a_number:
                    a_try = int(input(
                        f'Введенное число меньше, чем то, что загадано. Попробуйте еще раз. У Вас {tries_num} попыток: '))
                else:
                    a_try = int(input(
                        f'Введенное число больше, чем то, что загадано. Попробуйте еще раз. У Вас {tries_num} попыток: '))
            tries_num -= 1
        return check(a_try, a_number, tries_num)

    the_num = randint(0, 100)
    the_try = int(input('Отгадайте число от 0 до 100. У Вас 10 попыток: '))
    return check(the_try, the_num)


guess_number()
