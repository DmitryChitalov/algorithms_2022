"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def user_names(num=0):
    if num == user_count:
        return
    user_name = input(f'Введите имя пользователя {num+1}: ')
    users.append(user_name)
    user_names(num+1)


# сделал в одну
def game(user, count, number, i=0):
    i += 1
    if count > max_count:
        print('Users lost')
        return
    if user == users[0]:
        print(f"Attempt №{count}")
    print(f"{user}'s turn")
    user_number = int(input('Enter the number: '))
    if user_number == number:
        print(f'Winner is {user}')
        return
    else:
        if user_number < number:
            print('Your number is less than hidden')
        else:
            print('Your number is greater than hidden')
        if user == users[-1]:
            return game(users[0], count + 1, number)
        return game(users[0+i], count, number, i)


levels = {1: 10, 2: 5, 3: 3}
level = int(input('Choose the difficulty level: '))
max_count = levels[level]
user_count = int(input('Enter the number of players: '))
users = []
user_names()
print(users)
game(users[0], 1, random.randint(0, 100))
