"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from os import urandom as _urandom

#  version 1
# def random_number():
#     random = int(int.from_bytes(_urandom(7), 'big')) >> 5
#     list = [n for n in range(0, 101)]
#     return list[random % 100]
#
#
# secret = random_number()
# i = 1
# while i <= 10:
#     print(f'Попытка №{i:2} из 10')
#     user_number = int(input('Введите число от 1 до 100: '))
#     if user_number == secret:
#         print('Загаданное число угадано')
#         break
#     elif user_number > secret:
#         print(f'Ваше число {user_number} больше загаданного')
#     else:
#         print(f'Ваше число {user_number} меньше загаданного')
#     i += 1
# if i > 10:
#     print(f'Не угадано! Загаданное число {secret}')

#  version 2

import random

def recurs_meth(count, numb):
    print(f'Попытка №{count}')
    answer = int(input('Введите число от 1 до 100: '))
    if count == 10 or answer == numb:
        if answer == numb:
            print('Верно!')
        print(f'Загаданное число {numb}')
    else:
        if answer > numb:
            print(f'Ваше число {answer} меньше загаданного')
        else:
            print(f'Ваше число {answer} больше загаданного')
        recurs_meth(count + 1, numb)


recurs_meth(1, random.randint(0, 100))
