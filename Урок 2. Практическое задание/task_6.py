"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess_num(r_num, count):
    answer = int(input("Ваше число: "))
    if count == 0:
        return "Вы проиграли, попытки исчерпаны"
    elif answer != r_num and answer < r_num:
        count -= 1
        print(f"Не угадали! Число больше {answer} Попробуйте еще раз!")
        return guess_num(r_num, count)
    elif answer != r_num and answer > r_num:
        count -= 1
        print(f"Не угадали! Число меньше {answer} Попробуйте еще раз!")
        return guess_num(r_num, count)
    elif answer == r_num:
        return "Вы угадали!"
    else:
        return "Как так, что же пошло не так.."


if __name__ == "__main__":
    r_num = random.randint(0, 100)
    print(r_num)
    print(guess_num(r_num, 10))