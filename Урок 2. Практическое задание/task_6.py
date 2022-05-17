"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def number_game(gen_num, attempt=10):
    if attempt > 0:
        print(f'Осталось попыток: {attempt}')
        user_num = int(input('Введите целое число от 0 до 100: '))
        if user_num > gen_num:
            print(f'Введенное число {user_num} больше загаданного!')
            number_game(gen_num, attempt - 1)
        elif user_num < gen_num:
            print(f'Введенное число {user_num} меньше загаданного!')
            number_game(gen_num, attempt - 1)
        else:
            print(f'Вы угадали число {gen_num} с попытки {10 - attempt}!')
    else:
        print(f'Вы проиграли! Загаданное число - {gen_num}')


def start_number_game():
    gen_num = randint(0, 100)
    print('Да начнется игра!\n'
          'У Вас 10 попыток что бы отгадать случайное число от 0 до 100!')
    number_game(gen_num)


if __name__ == '__main__':
    start_number_game()
