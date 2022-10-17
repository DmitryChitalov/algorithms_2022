"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_the_num_recur(number=-1, tries=10):
    if number < 0:
        number = randint(0, 101)

    if tries == 0:
        print("You lose you out ouf tries")
        return

    user_guess = int(input("Input the number : "))
    if user_guess == number:
        print("You Win \nNumber is " + str(user_guess))
        return

    elif user_guess > number:
        print('Your number is  bigger')

    elif user_guess < number:
        print('Your number is smaller')

    return guess_the_num_recur(number, tries=tries - 1)

if __name__ == '__main__':
    guess_the_num_recur()