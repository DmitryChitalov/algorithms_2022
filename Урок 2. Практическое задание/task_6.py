"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random
random_digit = random.randint(0, 100)


def guesser(user_input=None, counter=0):
    digit_to_guess = random_digit
    # print(random_digit)

    if digit_to_guess == user_input:
        return print(f"ТОЧНО! ЭТО БЫЛО ЧИСЛО {digit_to_guess}.")
    elif counter == 10:
        return print(f"ТЫ НЕ УГАДАЛ ЗА {counter} ПОПЫТОК И ПРОИГРАЛ!")

    counter += 1
    user_input = int(input(f"Попытка №{counter}: Введите число от 0 до 100: "))
    if user_input > random_digit:
        print("Меньше!")
    else:
        print("Больше!")
    return guesser(user_input, counter)

guesser()
