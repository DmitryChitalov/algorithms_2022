"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


from random import randint


number = randint(1, 100)
count = 9

def guessing_game(number, count):
    answer = int(input('Введите число: '))
    if count == 0:
        return print(f'Попытки закончились, заганное число было {number}')
    elif answer == number:
        return print('Вы угадали!!!')
    elif answer < number:
        print('Вы не угадали, введите большее число')
        count -= 1
        guessing_game(number, count)
    elif answer > number:
        print('Вы не угадали, введите меньшее число')
        count -= 1
        guessing_game(number, count)


guessing_game(number, count)