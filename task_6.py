from random import randint

random_num = randint(0, 100)


def guess_num(count=1):
    user_num = int(input('Введите число от 0 до 100: '))
    if user_num == random_num or count == 10:
        if user_num == random_num:
            print('Поздравляю! Вы победили.')
        else:
            print('К сожалению, вы не угадали число.')
    else:
        count += 1
        if user_num > random_num:
            print('Введенное число больше загаданного')
        else:
            print('Введенное число меньше загаданного')
        return guess_num(count)


guess_num()
