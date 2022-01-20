"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
from random import randint


def find_digit_game(digit, attempt=10):
    if attempt == 0:
        return digit
    else:
        try:
            human_ch = int(input("Введите цифру от 0 до 100: "))
        except ValueError:
            print("Ввели не число ")
            return find_digit_game(digit, attempt)
        if human_ch == digit:
            return digit
        else:
            attempt -= 1
            if human_ch < digit:
                print("Больше")
            elif human_ch > digit:
                print("Меньше")
            return find_digit_game(digit, attempt)


digit = randint(0, 100)
print(f'Правильный ответ: {find_digit_game(digit)}')


