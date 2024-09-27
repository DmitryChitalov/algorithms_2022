"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. Решение через цикл не принимается.
"""

from random import randrange


def game_random_num(attempt, random_num, count=1):
    if attempt == count:
        return print(f'Вы не отгадали число {random_num}')
    else:
        user_answer = int(input('Угадай число от 0 до 100: '))
        if user_answer > random_num:
            print(f'робот загадал меньшее число\n осталось {attempt - count} попыток')
            return game_random_num(attempt, random_num, count + 1)
        elif user_answer < random_num:
            print(f'робот загадал большее число\n осталось {attempt - count} попыток')
            return game_random_num(attempt, random_num, count + 1)
        else:
            return print(f'ОУ ты вангуешь?!\nУгадано с {count} попытки')


game_random_num(10, randrange(1, 100))