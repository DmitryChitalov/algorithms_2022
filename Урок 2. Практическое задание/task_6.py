"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_num(num=randint(0, 100), cur_qty=10):
    num_cur = num
    qty = cur_qty
    if qty == 0:
        print(f'Вы не угадали и закончились попытки. Правильное число: {num_cur}')
    else:
        tar_num = int(input("Введите число от 0 до 100:  "))
        if tar_num == num_cur:
            print(f'Вы угадали правильное число: {num_cur}')
            return
        elif tar_num > num_cur:
            qty -= 1
            print(f'Вы не угадали. Правильное число меньше введенного. Осталось попыток: {qty}')
            return guess_num(num_cur, qty)
        else:
            qty -= 1
            print(f'Вы не угадали. Правильное число больше введенного. Осталось попыток: {qty}')
            return guess_num(num_cur, qty)


guess_num()
