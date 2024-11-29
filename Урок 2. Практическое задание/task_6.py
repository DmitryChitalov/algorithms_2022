"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import sample


def guess_number(hid_num, counting_attempts=1):
    """
    Функция - игра отгадывания числа рандомно выбранное компьютером от 0 до 100
    """
    n = hid_num
    user_number = int(input('Введите число: '))
    if counting_attempts == 10:
        return f'Вы проиграли((( Загаданное число {n}'
    if user_number == n:
        return f'Победа!!! Загаданное число {n}'
    elif user_number > n:
        print('Загаданное число меньше')
        return guess_number(n, counting_attempts + 1)
    elif user_number < n:
        print('Загаданное число больше')
        return guess_number(n, counting_attempts + 1)


hidden_num = sample(range(0, 100), 1)
print(guess_number(hidden_num[0]))
