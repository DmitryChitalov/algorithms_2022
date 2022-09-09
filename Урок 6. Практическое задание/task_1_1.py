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

Это файл для первого скрипта
"""
# Основы Python. Урок 3, задание №5

#Иcходный код
import random
from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    i = 0
    list_out = []
    while i < count:
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        i += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, repeats: bool) -> list:
    """Возвращает список шуток в количестве count
    :count: количество шуток
    :repeats: условие повторения или оригинальности слов в шутках
    """
    if count > len(nouns):
        print('максимальное количество оригинальных шуток:', len(nouns))
        count = len(nouns)
    i = 0
    list_out = []
    if repeats == True:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        while i < count:
            list_out.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
            i += 1
    else:
        while i < count:
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
    return list_out


print(get_jokes_adv(2,False))
print(get_jokes_adv(5,True))
print(get_jokes_adv(7,True))
print(get_jokes_adv(4,()))

# Оптимизированный код
from pympler import asizeof

def create_joke(count, **kwargs):
    ww = 0
    for j in kwargs.keys():
        if ww < 2:
            print(f'{random.choice(kwargs[j])}', end=' ')
            ww += 1
        else:
            print(f'{random.choice(kwargs[j])}')


def get_jokes_1(count, repeat=True) -> list:
    if repeat:
        for i in range(count):
            create_joke(count, nouns=nouns, adverbs=adverbs, adjectives=adjectives)

    elif not repeat:
        dict_jokes = dict(nouns=nouns, adverbs=adverbs, adjectives=adjectives)
        for i in range(count):
            noun, adverb, adjective = (random.choice(dict_jokes[j]) for j in dict_jokes.keys())
            print(f'{noun} {adverb} {adjective}')
            dict_jokes['nouns'].remove(noun)
            dict_jokes['adverbs'].remove(adverb)
            dict_jokes['adjectives'].remove(adjective)


print(asizeof.asized(get_jokes_adv(4, True)))
print(asizeof.asized(get_jokes_1(4), detail=1).format())

# Удалось достичь экономии памяти за счёт того, что улучшенная функция не создает много новых объектов.