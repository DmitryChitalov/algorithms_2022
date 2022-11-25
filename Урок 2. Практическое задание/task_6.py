"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_number(tries=10, number=None):
    if tries == 0:
        print(f"You are out of tries number was {number}")
        return

    if not number:
        number = randint(0, 101)

    try:
        user_number = int(input('Input number: '))
    except ValueError:
        return guess_number(tries=tries, number=number)

    if user_number == number:
        print(f"You have won, number is {number}")
        print(f"It took {10 - tries} tries")
        return True
    elif user_number > number:
        print("Your number is higher")
    elif user_number < number:
        print("Your number is lower")

    print(f"tries left {tries - 1}")
    return guess_number(tries - 1, number=number)


if __name__ == '__main__':
    guess_number()
