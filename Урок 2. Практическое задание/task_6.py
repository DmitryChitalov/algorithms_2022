"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


def guess_the_number(attempts_left, right_number):
    guessed_number = int(input('Как думаете, какое число загадано? '))

    if attempts_left == 0:
        print(f'Вы проиграли, было загадано {right_number}')
        return
    if right_number == guessed_number:
        print('Вы угадали!')
        return

    else:
        if guessed_number > right_number:
            print('Вы ввели больше')
        elif guessed_number < right_number:
            print('Вы ввели меньше')
        return guess_the_number(attempts_left - 1, right_number)


if __name__ == '__main__':
    guess_the_number(attempts_left=10, right_number=45)
