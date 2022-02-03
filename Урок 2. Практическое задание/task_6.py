"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
from random import randint


def guess_number(answer=randint(0, 100), attempt=10):
    user_answer = int(input(f"Попробуйте угадать число: "))
    if attempt == 1:
        return print(f"Увы, не в этот раз, было загаданно {answer}")
    elif user_answer > answer:
        print('Попробуйте ввести число поменьше.')
        return guess_number(answer, attempt - 1)
    elif user_answer < answer:
        print('Попробуйте ввести число побольше.')
        return guess_number(answer, attempt - 1)
    print(f"Победа! Вы угадали! Это число {answer}!")


guess_number()
