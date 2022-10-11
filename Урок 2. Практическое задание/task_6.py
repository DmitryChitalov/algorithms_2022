"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass


def guess_number(hidden_number, number_attempts=10):
    try:
        user_number = int(input(f'Осталось {number_attempts} попыток. Введите число:'))
        if hidden_number == user_number:
            print('Вы угадали!')
        elif user_number != hidden_number and number_attempts == 1:
            print(f'Попытки закончились, загаданное число {hidden_number}')
        elif user_number < hidden_number:
            raise ValueTooSmallError
        elif user_number > hidden_number:
            raise ValueTooLargeError
    except ValueTooSmallError:
        number_attempts -= 1
        print(f"Это число меньше загаданного, у Вас осталось {number_attempts} попыток\n")
        guess_number(hidden_number, number_attempts)
    except ValueTooLargeError:
        number_attempts -= 1
        print(f"Это число больше загаданного, у Вас осталось {number_attempts} попыток\n")
        guess_number(hidden_number, number_attempts)
    except ValueError:
        print('Ошибка, доступны только числа от 1 до 100')
        guess_number(hidden_number, number_attempts)


if __name__ == '__main__':
    number = random.randint(0, 101)
    print('Угадай число')
    guess_number(number)