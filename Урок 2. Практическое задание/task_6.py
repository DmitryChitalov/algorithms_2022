"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

random_number = round(random.random() * 100)


def mystery(data):
    global tries
    user_choice = int(input(f"Угадай число от 0 до 100 (У тебя {10 - tries} попыток)? >>> "))
    if tries == 10:
        print(f"Проигрыш! Наше число >>> {data}")
        exit()
    elif user_choice > data:
        print("Слишком много")
    elif user_choice < data:
        print("Слишком мало")
    else:
        print(f"Победа! И впрямь {data} ;)")
        exit()
    tries += 1
    return mystery(data)


tries = 0
mystery(random_number)
