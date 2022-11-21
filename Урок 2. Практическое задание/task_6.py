"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def fn_guess_number(number=0, attempt=10, result=0):
    if result == 1:
        print(f"Поздравляем! Вы угадали число: {number}")
    else:
        if attempt == 0 and result == 0:
            print(f"Вы использовали все попытки, но не угадали число. Загаданное число: {number}")
        else:
            guess_number = input(f"Угадайте число от 0 до 100, у вас {attempt} попыток:")
            if guess_number.isdigit():
                guess_number = int(guess_number)
                if guess_number == number:
                    result = 1
                else:
                    attempt -= 1
            else:
                print("Вы ввели строку, необходимо вводить число!")
            return fn_guess_number(number, attempt, result)


rand_number = randint(1, 100)
fn_guess_number(rand_number)
