"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess_num(try_count, num):
    print(f"{try_count} try.")
    answer = int(input("Guess a number: "))
    if try_count == 10 or answer == num:
        if answer == num:
            print(f"You've got it.")
        print(f"The number is {num}.")
    else:
        if answer > num:
            print(f"The guess number is less than {answer}")
        else:
            print(f"The guess number is more than {answer}")
        guess_num(try_count + 1, num)


guess_num(1, random.randint(0, 100))
