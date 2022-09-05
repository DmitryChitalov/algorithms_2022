"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def guess_number(counter, random_num):
    try:
        user_num = int(input('Введите предположительное целое число: '))
        if user_num == random_num:
            return f'Вы выиграли! Было загадано число: {user_num}'
        elif counter == 1:
            return f'Вы проиграли! Было загадано число: {random_num}'

        else:
            if user_num > random_num:
                print(f'Ух, слишком много! Пропробуй еще раз. Осталось попыток: {counter - 1}')
            else:
                print(f'Маловато, возьми больше! Осталось попыток: {counter - 1}')
            return guess_number(counter - 1, random_num)

    except ValueError:
        print('Неверное значение ввода, повторите ввод числа!')
        return guess_number(counter, random_num)


print(guess_number(10, randint(0, 100)))
