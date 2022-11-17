"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

def guess_number(counter: int=10, number: int=randint(0,100)) -> str:
    # Угадать число за 10 попыток
    if counter == 0:
        return "You lose!"
    try:
        guess: int = int(input(f"Try to guess the number from 0 to 100! You have {counter} tries: "))
    except ValueError as exc:
        print(f'{exc.args[0].split()[-1]} is not a number! you lost the try.')
        return guess_number(counter-1, number=number)
    if guess == number:
        return "\nCongratulations! You guessed!!!"
    print("Too little.") if number > guess else print("Too much.")
    return guess_number(counter-1, number=number)

if __name__ == "__main__":
    print("""  _____             _                                   
 |_   _| __ _   _  | |_ ___     __ _ _   _  ___ ___ ___ 
   | || '__| | | | | __/ _ \   / _` | | | |/ _ / __/ __|
   | || |  | |_| | | || (_) | | (_| | |_| |  __\__ \__ \\
   |_||_|   \__, |  \__\___/   \__, |\__,_|\___|___|___/
            |___/              |___/                    
            """)
    print(guess_number())
