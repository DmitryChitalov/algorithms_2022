"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def process(number: int, input_counter=1):
    if input_counter > 10:
        return f'Неудача. Загаданное число: {number}'
    num_txt = input(f'Попытка {input_counter}. Введите число: ')
    if not num_txt.isdecimal():
        print('Некорректный ввод')
        return process(number, input_counter)
    else:
        num_ = int(num_txt)
        if number == num_:
            return f'Победа!'
        elif number > num_:
            print('Введено число меньше загаданного')
        else:
            print('Введено число больше загаданного')
        return process(number, input_counter + 1)


if __name__ == '__main__':
    print(process(random.randint(0, 100)))

