"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random

def recursive_try_a_guess(tries: int = 10, number: int = random.randint(0, 100)):
    if tries <= 0:
        print("You lose, a number was %s" % number)
        return
    try:
        user_num = int(input("Try a guess a number. You have %s tries\n" % tries))
        if user_num > number:
            print("Your number is greater")
            return recursive_try_a_guess(tries=tries - 1)
        elif user_num < number:
            print("Your number is less")
            return recursive_try_a_guess(tries=tries - 1)
        else:
            print("You won number was %s" % number)
            return
    except ValueError:
        print("Write a number, not a random shit. Tries left %s" % (tries-1) if tries > 1 else "")
        recursive_try_a_guess(tries=tries-1)

recursive_try_a_guess()