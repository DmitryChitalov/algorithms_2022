"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random

n = random.randint(0, 100)
print(n)

def get_guess(i):
    ask = int(input('Введите загаданное число от 0 до 100: '))
    if ask == n or i == 0:
        return f'Игра окончена, верное число {n}'
    elif ask < n:
        print('Введите число больше!')
        return get_guess(i - 1)
    else:
        print('Введите число меньше!')
        return get_guess(i - 1)

print(get_guess(10))