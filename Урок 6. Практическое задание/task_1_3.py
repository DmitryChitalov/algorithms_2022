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

Это файл для третьего скрипта
"""

# Доработанная задача № 5 из 3 урока по курсу "Алгоритмы и структуры данных на Python"
import random
from pympler import asizeof


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# ИСХОДНОЕ
def get_jokes(count, repeat=True, **kwargs) -> list:
    list_out = []
    if repeat:
        for i in range(count):
            list_out.append(' '.join(random.choice(kwargs[j]) for j in kwargs.keys()))
    else:
        for i in range(count):
            noun, adverb, adjective = [random.choice(kwargs[j]) for j in kwargs.keys()]
            list_out.append(' '.join([noun, adverb, adjective]))
            kwargs['nouns'].remove(noun)
            kwargs['adverbs'].remove(adverb)
            kwargs['adjectives'].remove(adjective)

    return list_out


# ОПТИМИЗИРОВАННЫЙ
def create_joke(*args, **kwargs):
    count = 0
    for i in kwargs.keys():
        if count < 2:
            print(f'{random.choice(kwargs[i])}', end=' ')
            count += 1
        else:
            print(f'{random.choice(kwargs[i])}')


def get_jokes_1(count, repeat=True):
    if repeat:
        for i in range(count):
            create_joke(count, nouns=nouns, adverbs=adverbs, adjectives=adjectives)
    else:
        dict_jokes = dict(nouns=nouns, adverbs=adverbs, adjectives=adjectives)
        for i in range(count):
            noun, adverb, adjective = (random.choice(dict_jokes[j]) for j in dict_jokes.keys())
            print(f'{noun} {adverb} {adjective}')
            dict_jokes['nouns'].remove(noun)
            dict_jokes['adverbs'].remove(adverb)
            dict_jokes['adjectives'].remove(adjective)


print(asizeof.asized(get_jokes(4, nouns=nouns, adverbs=adverbs, adjectives=adjectives), detail=1).format())
print(asizeof.asized(get_jokes_1(4), detail=1).format())

"""
['огонь позавчера мягкий', 'город вчер....чью утопичный', 'город ночью веселый'] size=560 flat=88
    'огонь позавчера мягкий' size=120 flat=120
    'город вчера утопичный' size=120 flat=120
    'огонь ночью утопичный' size=120 flat=120
    'город ночью веселый' size=112 flat=112
город вчера веселый
огонь позавчера мягкий
город ночью утопичный
город сегодня яркий
None size=16 flat=16

Вывод:
Использование f-строк заместо создания списка позволяет экономить память.
"""
