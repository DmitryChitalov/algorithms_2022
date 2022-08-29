"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_number():
    hidden_num = randint(1, 100)
    print('Попробуйте отгадать число от 1 до 100 за 10 попыток.')

    def guess_number_1(count=1):
        if count < 11:
            answer = int(input(f'Попытка № {count}: '))
            count += 1
            if answer == hidden_num:
                print(f'Поздравляю! Вы угадали загаданное число с {count - 1} попытки!')
            elif answer > hidden_num:
                print(f'Неверный ответ. Загадано меньшее число.')
                return guess_number_1(count)
            elif answer < hidden_num:
                print(f'Неверный ответ. Загадано большее число.')
                return guess_number_1(count)
        else:
            print('Увы, Вы использовали все попытки.')
    return guess_number_1()


if __name__ == '__main__':
    guess_number()
