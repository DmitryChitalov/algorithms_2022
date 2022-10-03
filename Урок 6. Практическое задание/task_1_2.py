"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

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

Это файл для второго скрипта
"""

from memory_profiler import profile
from recordclass import recordclass
from random import choice


@profile
def get_jokes():
    """Эта функция генерирует шутки для канала ТНТ"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    quantity = input('Сколько шутеек пошутить? ')
    if quantity.isdigit():
        quantity = int(quantity)
        jokes = []
        for i in range(quantity):
            jokes.append(' '.join([str(i + 1), choice(nouns), choice(adverbs), choice(adjectives)]))
        return jokes
    else:
        get_jokes()


# for i in get_jokes():
#     print(i)

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    39     17.9 MiB     17.9 MiB           1   @profile
    40                                         def get_jokes():
    41                                             """Эта функция генерирует шутки для канала ТНТ"""
    42     17.9 MiB      0.0 MiB           1       source = {
    43     17.9 MiB      0.0 MiB           1           'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
    44     17.9 MiB      0.0 MiB           1           'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
    45     17.9 MiB      0.0 MiB           1           'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}
    46                                         
    47     17.9 MiB      0.0 MiB           1       quantity = input('Сколько шутеек пошутить? ')
    48     17.9 MiB      0.0 MiB           1       if quantity.isdigit():
    49     17.9 MiB      0.0 MiB           1           quantity = int(quantity)
    50     17.9 MiB      0.0 MiB           4           for i in range(quantity):
    51     17.9 MiB      0.0 MiB           3               print(f"{i + 1}. {choice(source['nouns'])} "
    52                                                           f"{choice(source['adverbs'])} "
    53                                                           f"{choice(source['adjectives'])}")
    54                                             else:
    55                                                 get_jokes()
'''


@profile
def get_jokes(words):
    quantity = input('Сколько шутеек пошутить? ')
    if quantity.isdigit():
        quantity = int(quantity)
        return (f'{i + 1}. {choice(words.nouns)} ' \
                f'{choice(words.adverbs)} {choice(words.adjectives)}'
                for i in range(quantity))
        # for i in range(quantity):
        #     yield f'{i + 1}. {choice(words.nouns)} ' \
        #           f'{choice(words.adverbs)} {choice(words.adjectives)}'
    else:
        get_jokes()


rc = recordclass('source', ('nouns', 'adverbs', 'adjectives'))
db = rc(
    nouns=("автомобиль", "лес", "огонь", "город", "дом"),
    adverbs=("сегодня", "вчера", "завтра", "позавчера", "ночью"),
    adjectives=("веселый", "яркий", "зеленый", "утопичный", "мягкий")
)

for i in get_jokes(db):
    print(i)

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    82     16.7 MiB     16.7 MiB           1   @profile
    83                                         def get_jokes(words):
    84     16.8 MiB      0.0 MiB           1       quantity = input('Сколько шутеек пошутить? ')
    85     16.8 MiB      0.0 MiB           1       if quantity.isdigit():
    86     16.8 MiB      0.0 MiB           1           quantity = int(quantity)
    87     16.8 MiB      0.0 MiB           2           return (f'{i + 1}. {choice(words.nouns)} ' \
    88                                                         f'{choice(words.adverbs)} {choice(words.adjectives)}'
    89     16.8 MiB      0.0 MiB           1                   for i in range(quantity))
    90                                             else:
    91                                                 get_jokes()
'''

# удалось незначительно оптимизировать функцию.
# вынес массив с источников слов за пределы функции и перевёл его в
# recordclass вместо массива. ещё был вариант использовать yield,
# но не сообразил, как сделать его замеры с profile