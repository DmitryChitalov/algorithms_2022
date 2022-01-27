"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


def user_names(num=0):
    if num == user_count:
        return
    user_name = input(f'Введите имя пользователя {num+1}: ')
    users.append(user_name)
    user_names(num+1)


def start(attempt_count):
    if attempt_count > max_count:
        print('Пользователи проиграли')
        return
    attempt_count += 1
    print(f'Attempt №{attempt_count}')
    game(users[0], attempt_count, 0)


def game(user, a_c, i):
    i += 1
    print(f"{user}'s turn")
    user_number = int(input('Enter the number: '))
    if user_number == number:
        print(f'Winner is {user}')
        return
    elif number < user_number:
        print('Your number is greater than hidden')
    else:
        print('Your number is less than hidden')
    if user == users[-1]:
        return start(a_c)
    return game(users[0+i], a_c, i)


number = random.randint(1, 100)
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Choose the difficulty level: '))
max_count = levels[level]
user_count = int(input('Enter the number of players: '))
users = []
user_names()
print(users)
start(0)
