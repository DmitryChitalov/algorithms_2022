"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def check_your_lucky(num=random.randint(0, 101), got_lucky=False, attempts=10):
    if got_lucky:
        return 'Поздравляю! Ты победил'
    elif attempts == 0:
        return f'Ты проиграл :( Загаднное число {num}'
    else:
        user_num = int(input(f'Попробуй угадай! :) '))
        if user_num == num:
            got_lucky = True
        return check_your_lucky(num=num, got_lucky=got_lucky, attempts=attempts - 1)


if __name__ == '__main__':
    print(check_your_lucky())