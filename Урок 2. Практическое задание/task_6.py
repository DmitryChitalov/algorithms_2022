"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def user_quest(to_guess: int, attempt: int):
    user_in = input(f'you have {attempt} attempts. Enter number to guess: \n')
    if user_in.isdigit() and int(user_in) == to_guess:
        print('Guessed')
    elif attempt == 1:
        print("Looser, The number is ", to_guess)
        return
    elif not user_in.isdigit():
        print("это не число")
        user_quest(to_guess, attempt)
    user_quest(to_guess, attempt - 1)



if __name__ == "__main__":
    to_guess = random.randint(0, 100)
    print(user_quest(to_guess, 10))
