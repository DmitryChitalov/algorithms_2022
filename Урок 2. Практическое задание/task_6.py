"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def transform_word(n):
    if 10 < n % 100 < 15:
        return 'попыток'
    elif n % 10 == 1:
        return 'попытка'
    elif 1 < n % 10 < 5:
        return 'попытки'
    else:
        return 'попыток'


def guess_the_number(num, guess_counter=10):
    guess = int(input('Ваше число: '))
    guess_counter -= 1

    if num == guess:
        print(f'Вы выиграли! Потрачено {10 - guess_counter} {transform_word(10 - guess_counter)}')
        return

    if guess_counter == 0:
        print(f'Вы проиграли. Попытки кончились. Загаданное число: {num}')
        return

    if guess > num:
        print(f'Неверно! Ваше число больше загаданного, осталось {guess_counter} {transform_word(guess_counter)}')
    elif guess < num:
        print(f'Неверно! Ваше число меньше загаданного, осталось {guess_counter} {transform_word(guess_counter)}')
    return guess_the_number(num, guess_counter)


if __name__ == '__main__':
    num = randint(0, 100)
    print('Загадано число от 0 до 100, у тебя 10 попыток его отгадать. Поехали!')
    guess_the_number(num)
