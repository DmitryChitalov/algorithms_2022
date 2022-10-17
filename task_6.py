from random import randint


def game(number, num):
    num_1 = input('Введите число от 0 до 100: ')
    try:
        num_1 = int(num_1)
    except ValueError:
        print(f'Ошибка! Вы вместо числа ввели строку: {num_1}! Минус 1 попытка :)')
        return game(number - 1, num)
    if num_1 == num:
        print(f'Поздравляем, Вы выиграли! Загаданное число: {num}')
        print(f'Попробуйте ещё раз!')
        return True
    elif num_1 > num:
        print('Не угадал! Ваше число больше загаданного.')
    else:
        print('Не угадал! Ваше число меньше загаданного.')

    if number == 0:
        print(f'Какой ужас, Вы проиграли! Загаданное число: {num}')
        print(f'Попробуйте ещё раз!')
        return True
    game(number - 1, num)


print('Вы открыли игру  - "Угадай число"')
print('Мы загадали число от 0 до 100, у Вас 10 попыток его отгадать!')
game(9, randint(0, 100))
