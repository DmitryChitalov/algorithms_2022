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

from pympler import asizeof
from random import choice, randint
from collections import defaultdict
from recordclass import recordclass


# def hangman_1():
#     """
#     Функция - имитация игры "Виселица".
#     Рандомно выбирается слово из скиска word_list.
#     Нужно угадать слово, вводя по букве.
#     """
#     word_list = ['вирус', 'программа', 'компьютер', 'хакер', 'взлом']
#     random_number = randint(0, 4)
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
#     print(asizeof.asizeof(hangman_1()))  # 16


# def hangman_2():
#     """
#     Функция - имитация игры "Виселица".
#     Рандомно выбирается слово из скиска.
#     Нужно угадать слово, вводя по букве.
#     """
#     word = choice(['вирус', 'программа', 'компьютер', 'хакер', 'взлом'])  # сокращаем код
#     stages = ['',
#               '________      ',
#               '|      |      ',
#               '|      0      ',
#               '|     /|\     ',
#               '|     / \     ',
#               '|']
#     remaining_letters = list(word)
#     letter_board = ["__"] * len(word)
#     print('Добро пожаловать на казнь\n')
#     wrong = 0
#     while wrong < 6:  # этапы можно записать числом
#         guess = input('Введите букву: ')
#         if guess in remaining_letters:
#             character_index = remaining_letters.index(guess)
#             letter_board[character_index], remaining_letters[character_index] = guess, '$'
#         else:
#             wrong += 1
#         print(' '.join(letter_board), '\n'.join(stages[0: wrong + 1]))  # сокращаем строки кода
#         if '__' not in letter_board:
#             print(f'Вы выиграли! Было загадано слово:\n{" ".join(letter_board)}')  # через f-строку
#             break
#         else:  # убираем флаги, вставляем в условие
#             print('\n'.join(stages[0: wrong]))
#             print(f'Вы проиграли! Было загадано слово: {word}')  # через f-строку
#
#
# if __name__ == '__main__':
#     print(asizeof.asizeof(hangman_2()))  # 16
#

# Не совсем с курса основ, но в ходе курса познакомился с кодом в книге Кори Альтхоффа "Сам себе программист".
# Небольшой выйгрыш за счет применения, главным образом, f-строки.
# Результат: 16 - ниже сделать уже не получилось, неудачный выбрал пример.


# Альгоритмы, урок 5, задание 1
# def add_firms(firms_count):
#     """
#     Функция создает на основе коллекции defaultdict словарь
#     с введенными пользователем названием фирмы и ее прибыли по кварталам.
#     Количество фирм передается в аргументе функции.
#     """
#     d = defaultdict(int)
#     while firms_count != 0:
#         firms_info = [(input('Введите название фирмы: '),
#                        (input('Введите прибыль фирмы за каждый квартал через пробел: ').split()))]
#         for key, val in firms_info:
#             val = sum([int(el) for el in val])
#             d[key] = val
#         firms_count -= 1
#     return d
#
#
# def count_firm_prof():
#     """
#     Функция запускает другую функцию - add_firms
#     для получения данных о данных по фирмам,
#     затем рассчитыват среднюю прибыль за год по всем фирмам
#     и выводит списки фирм с прибылью больше и меньше среднегодовой.
#     """
#     f_count = int(input('Введите количество фирм для расчета прибыли: '))
#     f_info = add_firms(f_count)
#     average_prof = float(sum(f_info.values()) / f_count)
#     return f'Средняя годовая прибыль всех предприятий: {average_prof}\n' \
#            f'Предприятия, с прибылью выше среднего значения: {[k for k, v in f_info.items() if v > average_prof]}\n' \
#            f'Предприятия, с прибылью ниже среднего значения: {[k for k, v in f_info.items() if v < average_prof]}'
#
#
# if __name__ == '__main__':
#     print(asizeof.asizeof(count_firm_prof()))  # 384


def add_firms():
    t = recordclass('t', ('name', 'prof'))
    name = input('Введите название фирмы: '),
    prof = input('Введите прибыль фирмы за каждый квартал через пробел: ').split()
    s_prof = sum([int(el) for el in prof])
    t.firm = t(name, s_prof)
    return t.firm


def count_firm_prof():
    f_count = int(input('Введите количество фирм для расчета прибыли: '))
    profs = 0
    firms = []
    for _ in range(f_count):
        f_info = add_firms()
        profs += f_info.prof
        firms.append(f_info)
    average_prof = profs / f_count
    return f'Средняя годовая прибыль всех предприятий: {average_prof}\n' \
           f'Предприятия с прибылью выше среднего значения: {[el.name for el in firms if el.prof > average_prof]}\n' \
           f'Предприятия с прибылью ниже среднего значения: {[el.name for el in firms if el.prof < average_prof]}'


if __name__ == '__main__':
    print(asizeof.asizeof(count_firm_prof()))  # 392


# Попробовал recordclass. Тоже неудачный пример получился. В конце кода пришлось вернуться к спискам.

