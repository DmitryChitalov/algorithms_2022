"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


from random import randint


def check_number(counter=10, number=None, flag=True):
    if counter == 0:
        print(f'Вы не справились с заданием. Загаданное число равнялось {number}')
        return

    if flag:
        number = randint(0, 100)
        print('Отгадайте число от 0 до 100. У Вас есть 10 попыток')

    try:
        value = int(input(f'Осталось {counter} попыток. Введите число: '))
    except ValueError:
        print('Хм, кажется Вы ввели не число, а что-то другое. Попробуйте ещё раз.')
        check_number(counter, number=number, flag=False)
    else:
        if value == number:
            print(f'Вы справились и угадали! Загаданное число равнялсось {number}.')
            return
        elif value < number:
            print('Загаданное число больше')
            return check_number(counter - 1, number=number, flag=False)
        else:
            print('Загаданное число меньше')
            return check_number(counter - 1, number=number, flag=False)


check_number()
