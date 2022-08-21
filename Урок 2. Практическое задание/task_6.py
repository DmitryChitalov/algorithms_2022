"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guess_number(number, tries=10):
    if not tries:
        print(f'Попытки закончились. Загаданное число - {number}')
        return
    user_choice = int(input('Введите число:'))
    if user_choice == number:
        print(f'Вы угадали!')
        return
    elif user_choice > number:
        print(f'Неверно. Введенное чило {user_choice} больше загаданного')
        guess_number(number, tries - 1)
    else:
        print(f'Неверно. Введенное число {user_choice} меньше загаданного.')
        guess_number(number, tries - 1)


if __name__ == '__main__':
    number = randint(0, 100)
    guess_number(number)