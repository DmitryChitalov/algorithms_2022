"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


import random


def number_guessing_program(current_guessing_attempt, custom_number, hidden_number):
    if current_guessing_attempt <= 10 and custom_number == hidden_number:
        print(f"Вы угадали число. Это число:")
        return custom_number
    elif current_guessing_attempt <= 10 and custom_number != hidden_number:
        if custom_number > hidden_number:
            print(f"Вы не угадали. Загаданное число меньше  {custom_number}.")
            custom_number = int(input("Введите число от 0 до 100: "))
            return number_guessing_program(current_guessing_attempt + 1, custom_number, hidden_number)
        else:
            print(f"Вы не угадали. Загаданное число больше  {custom_number}.")
            custom_number = int(input("Введите число от 0 до 100: "))
            return number_guessing_program(current_guessing_attempt + 1, custom_number, hidden_number)
    else:
        print(f"Загаданное число равно  {hidden_number}.")
        return "Вы не угадали число за 10 попыток"


custom_number_opening_attempts_to_guess = int(input("Введите первое число от 0 до 100: "))


print(number_guessing_program(1, custom_number_opening_attempts_to_guess, random.randint(0, 100)))

