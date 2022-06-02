"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random


def guess_number(num, attempt):
    user_num = int(input('Введите любое число: '))
    if user_num == num:
        return f'Вы угадали с {11 - attempt} попытки! Это было число {num}.'
    elif attempt == 1:
        return f'Вы истратили 10 попыток. Компьютер загадал число {num}.'
    elif user_num < num:
        attempt -= 1
        print(f'Загаданное число больше. Осталось {attempt} попыток.')
        return guess_number(num, attempt)
    elif user_num > num:
        attempt -= 1
        print(f'Загаданное число меньше. Осталось {attempt} попыток.')
        return guess_number(num, attempt)


comp_num = random.randint(0, 100)
print(comp_num)
print('Компьютер загадал число от 1 до 100. Попробуйте его отгадать! У вас 10 попыток.')
print(guess_number(comp_num, 10))
