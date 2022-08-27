"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_game(try_counter=10, random_number=None):
    if random_number is None:
        random_number = randint(0, 100)
    if try_counter > 0:
        try:
            user_number = int(input('Введите число от 0 до 100: '))
            if user_number != random_number:
                try_counter -= 1
                if try_counter != 0:
                    print(f'Вы не угадали, у Вас осталось {try_counter} жизней')
                    if user_number > random_number:
                        print('Загаданное число меньше')
                    else:
                        print('Загаданное число больше')
                guess_game(try_counter, random_number)
            if user_number == random_number:
                print('Поздравляю, вы победили!')
        except ValueError:
            print('Вы ввели не целое число. Попробуйте ещё раз.')
            guess_game(try_counter, random_number)
    elif try_counter == 0:
        print(f'Вы проиграли\nЗаданное число: {random_number}')


if __name__ == '__main__':
    guess_game()
