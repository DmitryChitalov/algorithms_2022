"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random

def ugadai_chislo(kolichestvo, chislo):
    print(f'Попытка номер: {kolichestvo}')
    vopros = int(input('Введите пожалуйста число 0 до 100: '))
    if kolichestvo == 10 or vopros == chislo:
        if vopros == chislo:
            print('Вы угадали!')
        print(f'Загаданное число: ')
    else:
        if vopros > chislo:
            print(f'Загаданное число меньше чем {chislo}')
        else:
            print(f'Загаданное число больше чем {chislo}')
        ugadai_chislo(kolichestvo + 1, chislo)


ugadai_chislo(1, random.randint(0, 100))
