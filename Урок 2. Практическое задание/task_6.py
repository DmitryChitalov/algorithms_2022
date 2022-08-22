"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_number(number, attempt=10):
    try:
        user_number = int(input('Попробуйте угадать число от 1 до 100: '))
        attempt -= 1
        if attempt == 0:
            return print(f'Вы не отгадали число, было загадано число {number}')
        elif user_number == number:
            return print(f'Вы отгадали число! :)')
        elif user_number > number:
            if attempt > 4:
                print(f'Слишком много, осталось {attempt} попыток')
            elif attempt < 5 and attempt > 1:
                print(f'Слишком много, осталось {attempt} попытки')
            else:
                print(f'Слишком много, осталось {attempt} попытки')
        elif user_number < number:
            if attempt > 4:
                print(f'Слишком мало, осталось {attempt} попыток')
            elif attempt < 5 and attempt > 1:
                print(f'Слишком мало, осталось {attempt} попытки')
            else:
                print(f'Слишком мало, осталось {attempt} попытки')
        return guess_number(number, attempt)
    except ValueError:
        print('Введите число')
        return guess_number(number, attempt)


if __name__ == '__main__':
    guess_number(randint(0, 100))
