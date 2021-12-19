"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random


def guess_the_number(guess_num, count):
    print(guess_num)
    if count > 10:
        print("Попытки закончились =(")
        return
    num = input("Введите число:\n")
    if not num.isdigit():
        print(f"вы ввели не число! Осталось попыток {10 - count}")
        return guess_the_number(guess_num, count + 1)
    num = int(num)
    if guess_num > num:
        print(f"Загаданное число больше. Осталось попыток {10 - count}")
    elif guess_num < num:
        print(f"Загаданное число меньше. Осталось попыток {10 - count}")
    elif num == guess_num:
        print(f"Вы отгадали число {guess_num}.Поздравляю")
        return
    guess_the_number(guess_num, count + 1)


guess_the_number(random.randint(0, 101), 1)


