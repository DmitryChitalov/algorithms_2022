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
from random import randint


# from timeit import timeit

@profile
def get_jokes(count: int) -> list:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]  # len(5)
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # len(5)
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # len(5)
    list_out = []
    for x in range(0, count):
        list_out.append("%s %s %s" % (nouns[randint(0, len(nouns) - 1)],
                                      adverbs[randint(0, len(adverbs) - 1)],
                                      adjectives[randint(0, len(adjectives) - 1)]))
    return list_out


def get_joke(count):
    nouns = ("автомобиль", "лес", "огонь", "город", "дом")  # len(5)
    adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")  # len(5)
    adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")  # len(5)
    for x in range(0, count):
        yield nouns[randint(0, len(nouns) - 1)], \
              adverbs[randint(0, len(adverbs) - 1)], \
              adjectives[randint(0, len(adjectives) - 1)]


# Generator
@profile
def get_jokes_2(count: int):
    return get_joke(count)


print(get_jokes(1000))
print(get_jokes_2(1000))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     19.4 MiB     19.4 MiB           1   @profile
    38                                         def get_jokes(count: int) -> list:
    39     19.4 MiB      0.0 MiB           1       nouns = ["автомобиль", "лес", "огонь", "город", "дом"] 
    40     19.4 MiB      0.0 MiB           1       adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"] 
    41     19.4 MiB      0.0 MiB           1       adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] 
    42     19.4 MiB      0.0 MiB           1       list_out = []
    43     19.5 MiB      0.1 MiB        1001       for x in range(0, count):
    44     19.5 MiB      0.1 MiB        2000           list_out.append("%s %s %s" % (nouns[randint(0, len(nouns) - 1)],
    45     19.5 MiB      0.0 MiB        1000                                         adverbs[randint(0, len(adverbs) - 1)],
    46     19.5 MiB      0.0 MiB        1000                                         adjectives[randint(0, len(adjectives) - 1)]))
    47     19.5 MiB      0.0 MiB           1       return list_out

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    59     19.7 MiB     19.7 MiB           1   @profile
    60                                         def get_jokes_2(count: int):
    61     19.7 MiB      0.0 MiB           1       return get_joke(count)


<generator object get_joke at 0x000002AB7CAB6350>
"""

# print(
#     timeit(
#         "get_jokes(100)",
#         setup='from __main__ import get_jokes',
#         number=1000))
# print(
#     timeit(
#         "get_jokes_2(100)",
#         setup='from __main__ import get_jokes_2',
#         number=1000))

"""
    timeit
    0.2490052
    0.00022299999999997322
    
    Аналитика:
        Заменили стандартный цикл на генератор, он позволяет уменьшить потребляемое кол-во памяти,
        а также заменили массивы на кортежи, что также позволяет сократить потребляемую память
"""
