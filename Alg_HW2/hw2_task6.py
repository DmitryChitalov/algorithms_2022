import random


def find_number(number, attempts=1):
    if attempts > 10:
        print(f'Неудача. Попытки кончились. А надо было вот бинарным поиском.'
              f' Загаданное число {number}')
        return 0
    inp_num = int(input(f'Попытка {attempts}: Угадайте число от 0 до 100.'
                        f' Оставшихся попыток: {11 - attempts} '))
    if inp_num == number:
        print(f'Поздравляю вы угадали число {number}')
        return 0
    elif inp_num < number:
        print('Загаданное число больше')
        find_number(number, attempts + 1)
    else:
        print('Загаданное число меньше')
        find_number(number, attempts + 1)


num = random.randint(0, 100)
find_number(num)
