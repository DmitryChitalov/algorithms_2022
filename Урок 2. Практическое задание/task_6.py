"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def divine_number(num, cur_attempt=1):
    """
    Угадать число за 10 попыток
    :param num: загаданное число
    :param cur_attempt: текущая попытка
    :return: угадал или нет
    """
    print('Надо угдать число от 0 до 100 за 10 попыток')
    print(f'Текущая попытка - {cur_attempt}')
    try:
        cur_answer = int(input('Введите число от 0 до 100: '))
    except ValueError:
        print('Вы ввели не число, но количество попыток уменьшилось')
        return divine_number(num, cur_attempt + 1)
    else:
        if cur_attempt == 10 or cur_answer == num:
            if cur_answer == num:
                return print(f'Все верно загаданное число {num}')
            return print(f'У вас закончились попытки. Загаданное число: {num}')
        else:
            if cur_answer > num:
                print(f'Загаданное число меньше чем {cur_answer}')
            else:
                print(f'Загаданное число больше чем {cur_answer}')
            divine_number(num, cur_attempt + 1)


if __name__ == '__main__':
    divine_number(randint(0, 100))
