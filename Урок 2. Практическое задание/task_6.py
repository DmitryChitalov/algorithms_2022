"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_the_number(nmb=None, hidden_number=None,  attempts=10, max_number=100):
    if nmb is None:
        nmb = int(input(f'Загадано число от 0 до {max_number}. \nПопробуйте его угадать. У вас {attempts} попыток.'
                        f'\nВведите число: '))
    if hidden_number is None:
        hidden_number = randint(0, max_number)

    attempts -= 1

    match attempts:
        case 1:
            sentence = f'осталась {attempts} попытка'
        case (2 | 3 | 4):
            sentence = f'осталось {attempts} попытки'
        case (5 | 6 | 7 | 8 | 9):
            sentence = f'осталось {attempts} попыток'

    if nmb == hidden_number:
        return 'Молодец! Вы угадали!'
    elif attempts == 0:
        return f'Очень жаль, но попытки закончились! \nБыло загадано число {hidden_number}.'
    elif nmb < hidden_number:
        nmb = int(input(f'Введеное число меньше загаданного \n{sentence}. \nВведите число: '))
        return guess_the_number(nmb, hidden_number, attempts, max_number)
    else:
        nmb = int(input(f'Введеное число больше загаданного \n{sentence}. \nВведите число: '))
        return guess_the_number(nmb, hidden_number, attempts, max_number)


if __name__ == '__main__':
    max_number = 100
    attempts = 10
    print(guess_the_number(attempts=attempts, max_number=max_number))
