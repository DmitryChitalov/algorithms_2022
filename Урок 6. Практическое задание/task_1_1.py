"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

from memory_profiler import memory_usage
import random
from recordclass import recordclass


def decor(func):
    def wrapper():
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# @decor
# def hangman_1():
#     """
#     Функция - имитация игры "Виселица".
#     Рандомно выбирается слово из скиска word_list.
#     Нужно угадать слово, вводя по букве.
#     """
#     word_list = ['вирус', 'программа', 'компьютер', 'хакер', 'взлом']
#     random_number = random.randint(0, 4)
#     word = word_list[random_number]
#     wrong = 0
#     stages = ["",
#               "________      ",
#               "|      |      ",
#               "|      0      ",
#               "|     /|\     ",
#               "|     / \     ",
#               "|"]
#     remaining_letters = list(word)
#     letter_board = ["__"] * len(word)
#     win = False
#     print('Добро пожаловать на казнь')
#     while wrong < len(stages) - 1:
#         print()
#         guess = input('Введите букву: ')
#         if guess in remaining_letters:
#             character_index = remaining_letters.index(guess)
#             letter_board[character_index] = guess
#             remaining_letters[character_index] = '$'
#         else:
#             wrong += 1
#         print((' '.join(letter_board)))
#         print('\n'.join(stages[0: wrong + 1]))
#         if '__' not in letter_board:
#             print('Вы выиграли! Было загадано слово:')
#             print(' '.join(letter_board))
#             win = True
#             break
#     if not win:
#         print('\n'.join(stages[0: wrong]))
#         print('Вы проиграли! Было загадано слово: {}'.format(word))
#
#
# if __name__ == '__main__':
#     res, mem_diff = hangman_1()
#     print(mem_diff)  # 0.01953125


@decor
def hangman_2():
    """
    Функция - имитация игры "Виселица".
    Рандомно выбирается слово из скиска word_list.
    Нужно угадать слово, вводя по букве.
    """
    word_list = ['вирус', 'программа', 'компьютер', 'хакер', 'взлом']
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Добро пожаловать на казнь')
    while wrong < len(stages) - 1:
        print()
        guess = input('Введите букву: ')
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong += 1
        print(' '.join(letter_board))
        print('\n'.join(stages[0: wrong + 1]))
        if '__' not in letter_board:
            print(f'Вы выиграли! Было загадано слово:\n{" ".join(letter_board)}')  # через f-строку
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print(f'Вы проиграли! Было загадано слово: {word}')  # через f-строку


if __name__ == '__main__':
    res, mem_diff = hangman_2()
    print(mem_diff)  # 0.015625

#  Не совсем с курса основ, но в ходе курса познакомился с кодом в книге Кори Альтхоффа "Сам себе программист".
#  Небольшой выйгрыш за счет применения f-строки в двух строчках.
#  Результат: 0.01953125 против 0.015625 с использованием f-строки.
