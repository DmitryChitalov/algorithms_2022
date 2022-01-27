"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random

def guess_number(num = random.randint(0, 100),count = 10):
    n = int(input(f"У вас {count} попыт(-ок,-ки, -ка),что бы угадать загаданное число. Введите число: "))
    if count == 1:
        return print(f"Вы не угадали, было загаданно {num}.")
    if n > num:
        count -= 1
        print('Ваше число больше загадонного, введите число меньше.')
        return guess_number(num, count)
    elif n < num:
        count -= 1
        print('Ваше число меньше загадонного, введите число больше.')
        return guess_number(num, count)
    else:
        print(f"Вы угадали число с {11 - count}-ой попытки, было загаданно {num}.")


guess_number()





