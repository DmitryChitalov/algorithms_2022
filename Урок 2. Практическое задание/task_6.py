"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""


from random import randint


def play_rand_numbers(secret_num=randint(0, 100), user_attemts=10):
    if user_attemts > 0:
        user_inp = int(input('Введите загаданное число от 0 до 100: '))
        if user_inp == secret_num:
            print('Молодец, угадал')
            return 0
        elif user_inp > secret_num:
            print('Введено число больше заданного')
        else:
            print('Введено число меньше заданного')
        return play_rand_numbers(secret_num, user_attemts-1)
    print('!!!LOOSER!!!')
    return 0


if __name__ == '__main__':
    play_rand_numbers()
