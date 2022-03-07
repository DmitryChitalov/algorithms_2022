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

Это файл для пятого скрипта
"""

from memory_profiler import profile
import random
from pympler.asizeof import asizeof


@profile
def original(number: int) -> list:
    nouns = ("автомобиль", "лес", "огонь", "город", "дом")
    adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
    adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
    result = []
    i = 0
    while i != number:
        joke = ' '.join((random.choice(nouns), random.choice(adverbs), random.choice(adjectives)))
        result.append(joke)
        i += 1
    del nouns
    del adverbs
    del adjectives
    del i
    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


@profile
def optimize(num):
    jokes = []
    for i in range(num):
        cur_noun = random.choice(nouns)
        cur_adverb = random.choice(adverbs)
        cur_adjective = random.choice(adjectives)
    jokes.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
    return jokes


if __name__ == '__main__':
    print(asizeof(original(5)))
    del original
    print(asizeof(optimize(5)))
    del optimize


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     39     40.3 MiB     40.3 MiB           1   @profile
#     40                                         def original(number: int) -> list:
#     41     40.3 MiB      0.0 MiB           1       nouns = ("автомобиль", "лес", "огонь", "город", "дом")
#     42     40.3 MiB      0.0 MiB           1       adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
#     43     40.3 MiB      0.0 MiB           1       adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
#     44     40.3 MiB      0.0 MiB           1       result = []
#     45     40.3 MiB      0.0 MiB           1       i = 0
#     46     40.3 MiB      0.0 MiB           6       while i != number:
#     47     40.3 MiB      0.0 MiB           5           joke = ' '.join((random.choice(nouns), random.choice(adverbs), random.choice(adjectives)))
#     48     40.3 MiB      0.0 MiB           5           result.append(joke)
#     49     40.3 MiB      0.0 MiB           5           i += 1
#     50     40.3 MiB      0.0 MiB           1       del nouns
#     51     40.3 MiB      0.0 MiB           1       del adverbs
#     52     40.3 MiB      0.0 MiB           1       del adjectives
#     53     40.3 MiB      0.0 MiB           1       del i
#     54     40.3 MiB      0.0 MiB           1       return result
#
#
# 704
##
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     62     40.3 MiB     40.3 MiB           1   @profile
#     63                                         def optimize(num):
#     64     40.3 MiB      0.0 MiB           1       jokes = []
#     65     40.3 MiB      0.0 MiB           6       for i in range(num):
#     66     40.3 MiB      0.0 MiB           5           cur_noun = random.choice(nouns)
#     67     40.3 MiB      0.0 MiB           5           cur_adverb = random.choice(adverbs)
#     68     40.3 MiB      0.0 MiB           5           cur_adjective = random.choice(adjectives)
#     69     40.3 MiB      0.0 MiB           1       jokes.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
#     70     40.3 MiB      0.0 MiB           1       return jokes
#
#
# 208

#Использование генератора впозволило сократить объем памяти в 3,5 раза.