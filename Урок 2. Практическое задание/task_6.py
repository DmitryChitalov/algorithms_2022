"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def random_game(user_number=None, attempt=1, game_number=None):
    if attempt == 1:
        print('Программа загадала случайное число, от 1 до 10 попробуйте его угадать.')
        game_number = randint(1, 10)
    if attempt < 10:
        user_number = int(input('Введите число: '))
        if user_number == game_number:
            return f'Вы угалали! Я загадывал {game_number}'
        elif user_number < game_number:
            print(f'Загаданное число больше чем {user_number}. У вас осталось {10 - attempt} попыток.')
            return random_game(user_number, attempt + 1, game_number)
        elif user_number > game_number:
            print(f'Загаданное меньше чем {user_number}. У вас осталось {10 - attempt} попыток.')
            return random_game(user_number, attempt + 1, game_number)
    return f'У вас закончились попытки. Я загадывал {game_number}'


if __name__ == '__main__':
    print(random_game())
