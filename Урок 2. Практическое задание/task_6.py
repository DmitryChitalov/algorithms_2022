"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess(count=1, random_num=(random.randint(1, 100))):
    user_num = int(input('Угадайте загадное число: '))
    if user_num == random_num and count <= 10:
        return print(f'Ура - победа, {count} попыток')
    elif count > 10:
        return print('Все, вы проиграли!')
    else:
        print('Много' if user_num > random_num else 'Мало')
        guess(count+1, random_num)


if __name__ == '__main__':
    guess()
